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

Nossa aplicação utiliza algumas APIS (Cohere, Spotify, Genius).
Logo é necessario preencher as variaveis de ambiente com suas respectivas chaves em um arquivo .env, no seguinte formato:
```
SPOTIFY_CLIENT_ID=
SPOTIFY_CLIENT_SECRET=
COHERE_API_KEY=
GENIUS_ACCESS_TOKEN=
```

1-  o usuario deve logar em sua conta spotify, para a API poder extrair informações a respeito de suas musicas mais ouvidas. 
2- Deve colocar um prompt onde se deseja que a musica final seja relacionada.
3- O audio final será disponibilizado para que o usuario possa ouvir/baixar na propria pagina. 
