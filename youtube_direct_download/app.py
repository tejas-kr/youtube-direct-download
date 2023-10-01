from flask import Flask

app = Flask(__name__)

from api_index import api_index
app.register_blueprint(api_index)

from youtube_download import youtube_download
app.register_blueprint(youtube_download)


@app.route("/health_check", methods=["GET"])
def health_check():
    return "Service is up and running"


