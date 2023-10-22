import os
import base64
from generate_song import generate_song_from_user
from dotenv import load_dotenv

import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("index.html")

# TODO: rename to `/api/spotify_login`
@app.route("/callback/")
def handle_spotify_login():
    return flask.render_template("index.html")

@app.route("/logged_in")
def handle_logged_in():
    return flask.render_template("logged_in.html")

@app.route("/api/generate_song", methods=["POST"])
def handle_generate_song():
    body = flask.request.get_json()
    generated_song = generate_song_from_user(body["user_id"], body["prompt"])
    with open(generated_song, "rb") as infile:
        data = infile.read()
    data = base64.b64encode(data)
    return flask.jsonify({ "data": data, "result": "ok" })

def main():
    load_dotenv("../.env")


if __name__ == '__main__':
    main()
