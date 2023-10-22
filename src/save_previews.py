import spotipy
import os
import requests
from typing import Optional
from song import DownloadedSong
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# Salva as previews das musicas da lista songs_ids
# no diretorio id_usuario/song_id.mp3
# retorna os ids das musicas que a preview esta disponivel

def save_preview(sp: spotipy.Spotify, user_id: str, song_id: str) -> Optional[DownloadedSong]:
    path = f"./data/{user_id}"

    os.makedirs(path, exist_ok=True)

    results = sp.track(track_id=song_id)
    preview_url = results["preview_url"]
    if not preview_url:
        return None

    song = requests.get(preview_url)
    full_path = f"{path}/{song_id}.mp3"
    with open(full_path, 'wb') as f:
        f.write(song.content)

    return full_path

if __name__ == '__main__':

    load_dotenv()
    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    cliente_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

    client_credentials_manager  = SpotifyClientCredentials(client_id=client_id, client_secret=cliente_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    save_preview(sp, "id_usuario_qlqr", "6zRBNkFmcNLgb3mOLmUK8i")
