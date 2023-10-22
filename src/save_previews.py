import os
import requests
from typing import Optional

import spotipy
from dotenv import load_dotenv

from song import DownloadedSong, SongMeta
from pathlib import Path

# Salva as previews das musicas da lista songs_ids
# no diretorio id_usuario/song_id.mp3
# retorna os ids das musicas que a preview esta disponivel

def save_preview(sp: spotipy.Spotify, user_id: str, song_meta: SongMeta) -> Optional[DownloadedSong]:
    path = f"./data/{user_id}"

    os.makedirs(path, exist_ok=True)

    song = requests.get(song_meta.preview_url)
    full_path = f"{path}/{song_meta.id}.mp3"
    with open(full_path, 'wb') as f:
        f.write(song.content)

    return DownloadedSong(Path(full_path))
