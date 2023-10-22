import os
import lyricsgenius as lg

def get_lyrics(music: str, artist: str):
    token = os.getenv('GENIUS_ACCESS_TOKEN')
    genius = lg.Genius(token)
    song = genius.search_song(music, artist)

    return song.lyrics

if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()
    lyrics = get_lyrics('Free Bird', 'Lynyrd Skynyrd')
    print(f'type: {type(lyrics)}')
    print(lyrics)

