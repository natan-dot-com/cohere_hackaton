from dataclasses import dataclass

@dataclass
class Danceability:
    value: int

    def __str__(self) -> str:
        mapping = ["very_low", "low", "mid", "high", "very_high"]
        assert self.value < len(mapping)

        s = "danceability="
        return s + mapping[self.value]

@dataclass
class Energy:
    value: int

    def __str__(self) -> str:
        mapping = ["very_low", "low", "mid", "high", "very_high"]
        assert self.value < len(mapping)

        s = "energy="
        return s + mapping[self.value]

@dataclass
class Loudness:
    value: int

    def __str__(self) -> str:
        mapping = ["low", "mid", "high"]
        assert self.value < len(mapping)

        s = "loudness="
        return s + mapping[self.value]

@dataclass
class Speechiness:
    value: int

    def __str__(self) -> str:
        mapping = ["low", "mid", "high"]
        assert self.value < len(mapping)

        s = "speechiness="
        return s + mapping[self.value]

@dataclass
class Instrumentalness:
    value: int

    def __str__(self) -> str:
        mapping = ["low", "high"]
        assert self.value < len(mapping)

        s = "instrumentalness="
        return s + mapping[self.value]

@dataclass
class Valence:
    value: int

    def __str__(self) -> str:
        mapping = ["very_low", "low", "mid", "high", "very_high"]
        assert self.value < len(mapping)

        s = "valence="
        return s + mapping[self.value]

@dataclass
class Acousticness:
    value: int

    def __str__(self) -> str:
        mapping = ["low", "mid", "high"]
        assert self.value < len(mapping)

        s = "acousticness="
        return s + mapping[self.value]

@dataclass
class Tempo:
    value: float

    def __str__(self) -> str:
        s = "tempo="
        return s + self.musical_class()

    def musical_class(self) -> str:
        if self.value < 40:
            return "Largissimo"
        elif self.value <= 60:
            return "Largo"
        elif self.value <= 66:
            return "Larghetto"
        elif self.value <= 76:
            return "Adagio"
        elif self.value <= 108:
            return "Andante"
        elif self.value <= 120:
            return "Moderato"
        elif self.value <= 168:
            return "Allegro"
        elif self.value <= 200:
            return "Presto"
        else:
            return "Prestissimo"
