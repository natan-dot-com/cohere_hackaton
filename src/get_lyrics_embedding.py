import typing as t
import cohere
from get_lyrics import get_lyrics
import numpy as np

def get_lyrics_embeddings(
    co: cohere.Client,
    texts: t.List[str]
) -> np.ndarray:
    assert len(texts) > 0, "lyrics list is empty"
    assert len(texts) <= 96, "Maximum number of texts per call is 96"
    response = co.embed(
        texts=texts,
        model='small',
        truncate='START'
    )

    embeddings = response.embeddings
    return np.array(embeddings)

if __name__ == '__main__':
    from dotenv import load_dotenv
    import os
    load_dotenv()
    list_lyrics = []
    songs = [
        ('Free Bird', 'Lynyrd Skynyrd'),
        ('Oh! Darling', 'The Beatles')
    ]
    for music, artist in songs:
        list_lyrics.append(get_lyrics(music, artist))

    cohere_token = os.getenv('COHERE_API_KEY')
    co = cohere.Client(cohere_token)
    embeddings = get_lyrics_embeddings(co, list_lyrics)
    print(type(embeddings))
    print(embeddings.shape)
    assert embeddings.shape == (2, 1024)