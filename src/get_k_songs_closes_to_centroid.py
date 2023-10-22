import numpy as np
from sklearn.metrics import pairwise_distances
from sklearn.cluster import KMeans

def get_k_songs_closes_to_centroid(
    kmeans: KMeans,
    cluster_idx: int, 
    embeddings: np.ndarray,
    k: int
) -> np.ndarray:
    center = kmeans.cluster_centers_[cluster_idx]
    dist = pairwise_distances(center.reshape(1,-1), embeddings, metric='cosine')[0]
    return np.argpartition(dist, k)[:k]

