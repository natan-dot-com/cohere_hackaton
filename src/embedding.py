from song import SongMeta
from audio_features import *

USE_LYRICS = False

def generate_embedding_string(meta: SongMeta) -> str:
    genres = f"genres={', '.join(meta.genres)}"
    no_lyrics = f"{meta.danceability}\n{meta.energy}\n{meta.loudness}\n{meta.instrumentalness}\n" \
              + f"{meta.valence}\n{meta.acousticness}\n{meta.song_bpm}\n{genres}"

    if USE_LYRICS:
        return no_lyrics + "\nlyrics:\n{meta.lyrics}"
    else:
        return no_lyrics
