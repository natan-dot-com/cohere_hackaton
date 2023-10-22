from dataclasses import dataclass
from pathlib import Path

@dataclass
class DownloadedSong:
    path: Path

@dataclass
class GeneratedSong:
    path: Path
