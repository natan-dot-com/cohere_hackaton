import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import requests

# Salva as previews das musicas da lista songs_ids
# no diretorio id_usuario/song_id.mp3
# retorna os ids das musicas que a preview esta disponivel

def save_previews(sp: spotipy.Spotify, user_id, song_ids: list):
    path = f"./data/{user_id}"

    os.makedirs(path, exist_ok=True)
    download_paths = []
    for song_id in song_ids:
        results = sp.track(track_id=song_id)
        preview_url = results["preview_url"]
        if preview_url == None:
            continue
        song = requests.get(preview_url)
        with open(f"{path}/{song_id}.mp3", 'wb') as f:
            f.write(song.content)
        download_paths.append(song_id)

    return download_paths

if __name__ == '__main__':

    load_dotenv()
    client_id = os.getenv('CLIENT_ID')
    cliente_secret = os.getenv('CLIENT_SECRET')

    client_credentials_manager  = SpotifyClientCredentials(client_id=client_id, client_secret=cliente_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    save_previews(sp, "id_usuario_qlqr", ["6zRBNkFmcNLgb3mOLmUK8i"])
