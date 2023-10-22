from dataclasses import dataclass
from pathlib import Path
from typing import Union, List

from audio_features import *

@dataclass
class DownloadedSong:
    path: Path

@dataclass
class GeneratedSong:
    path: Path


@dataclass
class SongMeta:
    id: str
    song_name: str
    song_main_artist: str

    lyrics: str

    danceability: Danceability
    energy: Energy
    loudness: Loudness
    speechiness: Speechiness
    instrumentalness: Instrumentalness
    valence: Valence
    acousticness: Acousticness
    song_bpm: Tempo
    genres: list[str]

    preview_url: str
