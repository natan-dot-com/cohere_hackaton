import os
import spotipy
import spotipy.util as util
import json
import unittest
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
from typing import List, Tuple

USERNAME = "p84rppfqm6cyn6phuxc3p41w7"
REDIRECT_URI = "http://localhost:8888/callback/"
SCOPE = "user-top-read"


def get_user_top_tracks(spotify: spotipy.Spotify, n_songs: int) -> List[Tuple[str, str, List[str]]]:
    """
        Returns a list of tuples containing the top 'n_songs' from specified user.
        The tuples contain the name of the song alongside with the respective artists.
        The return value is sorted in ascending order.
    """
    top_tracks = []

    top_tracks_response = spotify.current_user_top_tracks(limit=n_songs)
    for track in top_tracks_response["items"]:
        track_name = track["name"]
        track_artists = [artist["name"] for artist in track["artists"]]
        track_id = track["id"]
        top_tracks.append((track_id, track_name, track_artists))

    return top_tracks
    

def main():
    load_dotenv("../.env")

    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    token = util.prompt_for_user_token(USERNAME, scope=SCOPE, client_id=client_id, client_secret=client_secret, redirect_uri=REDIRECT_URI)
    spotify = spotipy.Spotify(auth=token)
    
    top_tracks = get_user_top_tracks(spotify, 50)

    print(top_tracks)
    assert len(top_tracks) == 50


if __name__ == "__main__":
    main()