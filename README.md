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
