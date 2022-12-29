from flask import Flask

def create_app(config_filename="config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    from youtube_direct_download.api_index import api_index
    app.register_blueprint(api_index)

    from youtube_direct_download.youtube_download import youtube_download
    app.register_blueprint(youtube_download)

    return app


