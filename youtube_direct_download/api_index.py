from flask import Blueprint, jsonify

api_index = Blueprint("api_index", __name__)

@api_index.route('/', methods=['GET'])
def index():
        api_index_dict: dict = {
            "/get_all_links?main_link=(main_youtube_link)": "Get all the download links for the video",
            "/get_all_links?main_link=(main_youtube_link)&format=(audio, video)": "Get only specified format links",
            "/get_all_links?main_link=(main_youtube_link)&<format=(audio, video)&resolution=(specified_resolution)": "Get 'video' Link of specified resolution. Ex - (480p), (720p)"
        }
        return jsonify(api_index_dict)