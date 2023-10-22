import numpy as np
import cohere
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances
from python_tsp.exact import solve_tsp_dynamic_programming

from get_lyrics import get_lyrics
from get_lyrics_embedding import get_lyrics_embeddings
from get_k_songs_closes_to_centroid import get_k_songs_closes_to_centroid
from find_best_cluster import find_best_cluster

import typing as t



def ordenate_music(
    music_idxs: np.ndarray,
    embeddings: np.ndarray
) -> int:
    target_embeddings = embeddings[music_idxs]
    distance_matrix = pairwise_distances(
        target_embeddings,
        target_embeddings,
        metric='cosine'
    )

    permutation, _ = solve_tsp_dynamic_programming(distance_matrix)
    return music_idxs[permutation]



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

    music_idxs = get_k_songs_closes_to_centroid(kmeans, cluster_idx, embeddings, 2)
    ordenated_idxs = ordenate_music(music_idxs, embeddings)
    print(ordenated_idxs)


    prompt='I am pissed today!'
    cluster_idx = find_best_cluster(co, kmeans, prompt)
    music_idxs = get_k_songs_closes_to_centroid(kmeans, cluster_idx, embeddings, 2)
    ordenated_idxs = ordenate_music(music_idxs, embeddings)
    print(ordenated_idxs)
