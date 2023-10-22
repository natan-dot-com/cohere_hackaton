from datetime import timedelta
from pathlib import Path
import subprocess
import logging

from song import DownloadedSong, GeneratedSong

logger = logging.getLogger(__name__)

def merge(
    songs: list[DownloadedSong],
    fade_duration=timedelta(seconds=5),
    out="out.mp3"
) -> GeneratedSong:
    assert len(songs) > 0, "songs list is empty"

    inputs = []
    fades = []
    for i, song in enumerate(songs):
        inputs.extend(["-i", str(song.path)])
        if i > 0:
            prev = f"tmp{i-1}" if i > 1 else 0
            target = f"[tmp{i}]" if i + 1 < len(songs) else ""
            fades.append(f'[{prev}][{i}]acrossfade=d={fade_duration.total_seconds()}{target}')

    filters = ';'.join(fades)
    args = ["ffmpeg"] + inputs + ["-filter_complex", filters, out]
    logger.info("running command: '%s'", " ".join(map(lambda arg: f'"{arg}"', args)))
    proc = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        logger.error("error while running ffmpeg: %s", proc.stdout.decode())
        raise Exception("failed to run ffmpeg")

    return GeneratedSong(Path(out))


if __name__ == '__main__':
    logging.basicConfig()
    logger.setLevel(logging.DEBUG)

    songs = [
        DownloadedSong(Path("data/dertoni/Free Bird.mp3")),
        DownloadedSong(Path("data/dertoni/Summer Nights.mp3")),
        DownloadedSong(Path("data/dertoni/Upside down.mp3")),
    ]
    merge(songs)
