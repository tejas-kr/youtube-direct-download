from flask import Blueprint, jsonify, request, abort
from utils import LinkExtract

youtube_download = Blueprint("youtube_download", __name__)

def get_links(main_link: str):
    link_ext = LinkExtract(main_link=main_link)
    all_links = link_ext.get_download_links()

    return all_links
    

def validate_params(params: dict):
    if not params['main_link'] or params['main_link'] == '':
        abort(400, 'Please enter main_link')
    
    if params['format'] and params['format'].lower() not in ['audio', 'video']:
        abort(400, 'Format must be "audio or video"')


@youtube_download.route('/get_all_links', methods=['GET'])
def get_download_links_json():
    params = {
        'main_link': request.args.get('main_link'),
        'format': request.args.get('format'),
        'resolution': request.args.get('resolution')
    }

    validate_params(params)
    
    link_dict = {}
    link_dict = get_links(main_link=params['main_link'])
    if not link_dict or len(link_dict) == 0:
        abort(400, "Unable to get links") 

    if params['format']:
        link_dict = {
            params['format']: link_dict[params['format']]
        }

    if params['resolution']:
        if link_dict['video']:
            link_dict['video'] = [i for i in link_dict['video'] if params['resolution'] in i[1]]

    return jsonify(link_dict)
