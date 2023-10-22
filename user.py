import spotipy
from typing import List, Tuple
from dataclasses import dataclass

@dataclass
class User:
    user_id: str

    def get_user_top_tracks(
        self, sp: spotipy.Spotify, n_songs: int
    ) -> List[str]:
        """
            Returns a list of strings containing the top 'n_songs' from specified user.
            The strings corresponds to each track ID.
            The return value is sorted in ascending order.
        """
        top_tracks_response = sp.current_user_top_tracks(limit=n_songs)
        return [track["id"] for track in top_tracks_response["items"]]