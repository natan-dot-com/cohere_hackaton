import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from utils import discretize
from get_lyrics import get_lyrics
from typing import Union, List

class SongMeta:
    def __init__(self, user_id: str, song_id: str):
        self.song_id = song_id
        self.user_id = user_id
        self.song_name = None
        self.song_main_artist = None

        self.lyrics = None

        self.danceability = None
        self.energy = None
        self.loudness = None
        self.speechiness = None
        self.instrumentalness = None
        self.valence = None
        self.acousticness = None
        self.song_bpm = None


    def extract_metadata(self, sp: spotipy.Spotify):
        track_response = sp.track(track_id=self.song_id)

        self.song_name = track_response["name"]
        self.song_main_artist = track_response["artists"][0]["name"]
        self.lyrics = get_lyrics(self.song_name, self.song_main_artist)
        
        features_response = sp.audio_features([self.song_id])[0]
        
        self.danceability = discretize(range=(0, 1), n_bins=5, value=features_response["danceability"])
        self.energy = discretize(range=(0, 1), n_bins=5, value=features_response["energy"])
        self.loudness = discretize(range=(-60, 0), n_bins=3, value=features_response["loudness"])
        self.speechiness = discretize(range=(0, 1), n_bins=3, value=features_response["speechiness"])
        self.instrumentalness = discretize(range=(0, 1), n_bins=2, value=features_response["instrumentalness"])
        self.valence = discretize(range=(0, 1), n_bins=5, value=features_response["valence"])
        self.acousticness = discretize(range=(0, 1), n_bins=3, value=features_response["acousticness"])
        self.song_bpm = features_response["tempo"]


    def get_audio_features(self) -> List[Union[int, float]]:
        return [
            self.danceability,
            self.energy,
            self.loudness,
            self.speechiness,
            self.instrumentalness,
            self.valence,
            self.acousticness,
            self.song_bpm
        ]
        

def main():
    load_dotenv("../.env")
    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

    client_credentials_manager  = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    song = SongMeta("id_usuario_qlqr", "6zRBNkFmcNLgb3mOLmUK8i")
    song.extract_metadata(sp)
    print(song.get_audio_features())


if __name__ == "__main__":
    main()