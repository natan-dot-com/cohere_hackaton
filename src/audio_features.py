class Danceability:
    def to_string(label: int) -> str:
        mapping = ["very_low", "low", "mid", "high", "very_high"]
        assert label < len(mapping)
        
        s = "danceability="
        return s + mapping[label] + " "

class Energy:
    def to_string(label: int) -> str:
        mapping = ["very_low", "low", "mid", "high", "very_high"]
        assert label < len(mapping)

        s = "energy="
        return s + mapping[label] + " "

class Loudness:
    def to_string(label: int) -> str:
        mapping = ["low", "mid", "high"]
        assert label < len(mapping)

        s = "loudness="
        return s + mapping[label] + " "

class Speechiness:
    def to_string(label: int) -> str:
        mapping = ["low", "mid", "high"]
        assert label < len(mapping)

        s = "speechiness="
        return s + mapping[label] + " "

class Instrumentalness:
    def to_string(label: int) -> str:
        mapping = ["low", "high"]
        assert label < len(mapping)

        s = "instrumentalness="
        return s + mapping[label] + " "

class Valence:
    def to_string(label: int) -> str:
        mapping = ["very_low", "low", "mid", "high", "very_high"]
        assert label < len(mapping)

        s = "valence="
        return s + mapping[label] + " "

class Acousticness:
    def to_string(label: int) -> str:
        mapping = ["low", "mid", "high"]
        assert label < len(mapping)

        s = "acousticness="
        return s + mapping[label] + " "

class Tempo:
    def to_string(bpm: float) -> str:
        s = "tempo="
        return s + str(bpm) + " "
