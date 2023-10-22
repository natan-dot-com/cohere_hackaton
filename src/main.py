import os
import base64
from generate_song import generate_song_from_user
from dotenv import load_dotenv
import logging

import flask

load_dotenv("../.env")

logging.basicConfig();

logger = logging.getLogger("root")
logger.setLevel(logging.INFO)

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
    logger.info("generating song for user '%s'", body["profileId"])
    generated_song = generate_song_from_user(body["accessToken"], body["profileId"], body["prompt"])
    return flask.send_file(generated_song.path, mimetype="audio/mp3")
