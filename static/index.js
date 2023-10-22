
const BACKEND = "http://localhost:8888/callback/";
const CLIENT_ID = "4b01eb5194cd4aa6afb6aa9e31eca0f4";
const SCOPE = "user-read-private user-read-email user-top-read";

// Local Storage key for storing spotify info
const SPOTIFY_INFO_KEY = "SPOTIFY_INFO"

{
    const window_params = new URLSearchParams(window.location.search);
    const code = window_params.get("code");

    if (code) {
        handleLoggedIn(code);
    }
}

async function handleLoggedIn(code) {
    const accessToken = await getAccessToken(CLIENT_ID, code);
    console.log("accessToken = ", accessToken);

    const profile = await fetchProfile(accessToken);
    console.log("profileId = ", profile.id);

    const info = { accessToken, profile };
    localStorage.setItem(SPOTIFY_INFO_KEY, JSON.stringify(info));
    window.location.replace("/logged_in")
}

async function login() {
    await redirectToAuthCodeFlow(CLIENT_ID);
}

async function redirectToAuthCodeFlow(clientId) {
    const verifier = generateCodeVerifier(128);
    const challenge = await generateCodeChallenge(verifier);

    localStorage.setItem("verifier", verifier);

    const params = new URLSearchParams();
    params.append("client_id", clientId);
    params.append("response_type", "code");
    params.append("redirect_uri", BACKEND);
    params.append("scope", SCOPE);
    params.append("code_challenge_method", "S256");
    params.append("code_challenge", challenge);

    document.location = `https://accounts.spotify.com/authorize?${params.toString()}`;
}

function generateCodeVerifier(length) {
    let text = '';
    let possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';

    for (let i = 0; i < length; i++) {
        text += possible.charAt(Math.floor(Math.random() * possible.length));
    }
    return text;
}

async function generateCodeChallenge(codeVerifier) {
    const data = new TextEncoder().encode(codeVerifier);
    const digest = await window.crypto.subtle.digest('SHA-256', data);
    return btoa(String.fromCharCode.apply(null, [...new Uint8Array(digest)]))
        .replace(/\+/g, '-')
        .replace(/\//g, '_')
        .replace(/=+$/, '');
}

async function getAccessToken(clientId, code) {
    const verifier = localStorage.getItem("verifier");

    const params = new URLSearchParams();
    params.append("client_id", clientId);
    params.append("grant_type", "authorization_code");
    params.append("code", code);
    params.append("redirect_uri", BACKEND);
    params.append("code_verifier", verifier);

    const response = await fetch("https://accounts.spotify.com/api/token", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: params
    });

    const result = await response.json();
    console.log(result);
    return result.access_token;
}

async function fetchProfile(token) {
    const result = await fetch("https://api.spotify.com/v1/me", {
        method: "GET",
        headers: { Authorization: `Bearer ${token}` }
    });

    return await result.json();
}
