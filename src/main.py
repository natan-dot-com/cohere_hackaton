import os
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
    print(body)
    return flask.jsonify({ "result": "ok" })

def main():
    load_dotenv("../.env")


if __name__ == '__main__':
    main()
