from song import SongMeta
from audio_features import *

def generate_embedding_string(meta: SongMeta) -> str:
    return f"{meta.danceability}{meta.energy}{meta.loudness}{meta.instrumentalness}" \
         + f"{meta.valence}{meta.acousticness}{meta.song_bpm}{meta.lyrics}"
