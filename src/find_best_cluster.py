import numpy as np
import cohere
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances
from get_lyrics import get_lyrics
from get_lyrics_embedding import get_lyrics_embeddings
from get_k_songs_closes_to_centroid import get_k_songs_closes_to_centroid


def find_best_cluster(
    co: cohere.Client,
    kmeans: KMeans,
    prompt: str,
    model = 'embed-english-v2.0',
    metric = 'cosine',
) -> int:
    """
        Returns the index of the best cluster
    """
    assert len(prompt) > 0, 'Cannot find best cluster from empty prompt'
    response = co.embed(
        texts=[prompt],
        model=model,
        truncate='START'
    )
    prompt_embed = np.array(response.embeddings[0])
    prompt_embed = prompt_embed.reshape(1,-1)
    centroids = kmeans.cluster_centers_
    distances = pairwise_distances(prompt_embed, centroids, metric=metric)
    closest_idx = np.argmin(distances)

    return closest_idx


if __name__ == '__main__':
    from dotenv import load_dotenv
    import os
    load_dotenv()
    list_lyrics = []
    songs = [
        ('Better Together', 'Jack Johnson'),
        ('Upside Down', 'Jack Johnson'),
        ('Duality', 'Slipknot'),
        ('Psychosocial', 'Slipknot'),
    ]
    for music, artist in songs:
        list_lyrics.append(get_lyrics(music, artist))

    cohere_token = os.getenv('COHERE_API_KEY')
    co = cohere.Client(cohere_token)
    embeddings = get_lyrics_embeddings(co, list_lyrics)
    print(type(embeddings))
    print(embeddings.shape)
    assert embeddings.shape[0] == 4

    kmeans = KMeans(n_clusters=2)
    kmeans = kmeans.fit(embeddings)
    print(f'kmeans labels: {kmeans.labels_}')

    prompt='I would like to listen to a more chilling music'
    cluster_idx = find_best_cluster(co, kmeans, prompt)

    get_k_songs_closes_to_centroid(kmeans, cluster_idx, embeddings, 2)

    prompt='I am pissed today!'
    cluster_idx = find_best_cluster(co, kmeans, prompt)
    get_k_songs_closes_to_centroid(kmeans, cluster_idx, embeddings, 2)
