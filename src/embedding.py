from song_meta import SongMeta
from audio_features import *

def generate_embedding_string(metadata: SongMeta) -> str:
    embedding_string = ""
    embedding_string += Danceability.to_string(metadata.danceability)
    embedding_string += Energy.to_string(metadata.energy)
    embedding_string += Loudness.to_string(metadata.loudness)
    embedding_string += Speechiness.to_string(metadata.speechiness)
    embedding_string += Instrumentalness.to_string(metadata.instrumentalness)
    embedding_string += Valence.to_string(metadata.valence)
    embedding_string += Acousticness.to_string(metadata.acousticness)
    embedding_string += Tempo.to_string(metadata.song_bpm)
    embedding_string += metadata.lyrics

    return embedding_string

