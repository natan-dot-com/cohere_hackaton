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
