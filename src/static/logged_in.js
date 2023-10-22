
const BACKEND = "http://localhost:8888/callback/";
const CLIENT_ID = "4b01eb5194cd4aa6afb6aa9e31eca0f4";

// Local Storage key for storing spotify info
const SPOTIFY_INFO_KEY = "SPOTIFY_INFO"

const generateBtn = document.getElementById("generate");
const generateBtnContent = document.getElementById("generate-btn-content");
const loading = document.getElementById("loading");
const prompt = document.getElementById("prompt");

const info = localStorage.getItem(SPOTIFY_INFO_KEY);
if (!info) {
    window.location.replace("/")
} else {
    var { accessToken, profile } = JSON.parse(info);
}

async function generateSong() {
    startLoading();

    const song = await fetch(`/api/generate_song`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
            profileId: profile.id,
            accessToken,
            prompt: prompt.value,
        })
    });

    stopLoading();
}

function startLoading() {
    generateBtn.disabled = true;
    generateBtnContent.style.display = "none";
    loading.style.display = "block";
}


function stopLoading() {
    generateBtn.disabled = false;
    generateBtnContent.style.display = "block";
    loading.style.display = "none";
}
