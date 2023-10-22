import spotipy
import spotipy.util as util
import os
import cohere
from dotenv import load_dotenv
from user import User
from song_meta import SongMeta
from embedding import generate_embedding_string
from get_lyrics_embedding import get_lyrics_embeddings
from find_best_cluster import find_best_cluster
from sklearn.cluster import KMeans

REDIRECT_URI = "http://localhost:8888/callback/"
SCOPE = "user-top-read"

def generate_song_from_user(user_id: str, prompt: str):
    user = User(user_id)
    
    load_dotenv("../.env")
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    co = cohere.Client(os.getenv('COHERE_API_KEY'))
    sp = spotipy.Spotify(auth=util.prompt_for_user_token(
        user_id, scope=SCOPE, client_id=client_id, 
        client_secret=client_secret, redirect_uri=REDIRECT_URI
    ))

    top_tracks_id = user.get_user_top_tracks(sp, 5)
    
    trackmeta_list = []
    embedding_string_list = []
    for track_id in top_tracks_id:
        track = SongMeta(user_id, track_id)
        if not track.has_preview(sp):
            continue
        
        track.extract_metadata(sp)

        trackmeta_list.append(track)
        embedding_string_list.append(generate_embedding_string(track))

    embeddings = get_lyrics_embeddings(co, embedding_string_list)
    
    kmeans = KMeans(n_clusters=2)
    kmeans.fit(embeddings)

    best_cluster = find_best_cluster(co, kmeans, prompt)
    print(best_cluster)


    

    


if __name__ == "__main__":
    generate_song_from_user("p84rppfqm6cyn6phuxc3p41w7", "foda")