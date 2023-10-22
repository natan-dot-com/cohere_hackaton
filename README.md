# cohere_hackaton

## Installation using venv

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### Installing ffmpeg

- Download ffmpeg from [the download page](https://ffmpeg.org/download.html)
- Prefer the static version
- Unpack the binary
- Store it in a directory listed in the `PATH` environment variable

## Running the server locally (dev mode)

```bash
python3 -m flask --app src/main.py --debug run --port 8888
```
Este projeto faz uma musica _mashup_ de forma personalizada para cada usuario. Isto é feito com base em suas musicas mais ouvidas do spotify, que serão fornecidas como entrada para aplicação. O passo seguinte é extrair informações relevantes de cada musica obtida, como a letra e metadados (utilizando a API do spotify) 
