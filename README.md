# Cohere Hackaton -- Mashup Generator

## Brief Description

Mashup Generator is a web application than can generate a mashup track from the most listened songs on your Spotify profile. It uses Cohere and Spotify APIs working together in order to achieve good performance on selecting the tracks that will be used on the mashup. Mashup Generator also takes into account the semantic meaning of the track's lyrics, as well as many descriptors used on audio analysis (such as instrumentalness, speechiness, tempo, etc), in order to provide a mashup with similar tracks in structure.


## Installation & How to Use

### Installation using venv

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

#### Installing ffmpeg

- Download ffmpeg from [the download page](https://ffmpeg.org/download.html)
- Prefer the static version
- Unpack the binary
- Store it in a directory listed in the `PATH` environment variable

### Running the server locally (dev mode)

```bash
python3 -m flask --app src/main.py --debug run --port 8888
```

Our applications need some APIs in order to get the work done (such as Cohere, Spotify and Genius).
It's necessary to fill an `.env` file with the environment variables as follows, including the keys to the respective APIs:
```
SPOTIFY_CLIENT_ID=
SPOTIFY_CLIENT_SECRET=
COHERE_API_KEY=
GENIUS_ACCESS_TOKEN=
```

1. The user must log in their spotify account to be able to extract from the API the most listened musics.
2. The user should provide a prompt related to the desired song.
3. The final audio will be made available to download in the page itself.
