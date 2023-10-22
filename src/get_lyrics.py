import os
from pathlib import Path
from typing import Optional
import lyricsgenius as lg

from disk_cache import diskcache

@diskcache(path=".cache/get_lyrics.log")
def get_lyrics(
    music: str,
    artist: str
) -> Optional[str]:
    token = os.getenv('GENIUS_ACCESS_TOKEN')
    genius = lg.Genius(token)
    song = genius.search_song(music, artist)
    if song is None: return None
    return song.lyrics

if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()
    lyrics = get_lyrics('Free Bird', 'Lynyrd Skynyrd')
    print(f'type: {type(lyrics)}')
    print(lyrics)
