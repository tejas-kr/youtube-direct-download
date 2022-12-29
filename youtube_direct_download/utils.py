import youtube_dl


class LinkExtract:
    """ Class encapsulting methods of link extraction and downloads """

    _main_link: str
    _vid_info: dict
    _all_vid_links: dict = {
        'audio': [],
        'video': []
    }

    def __init__(self, main_link: str):
        self._main_link = main_link


    def get_download_links(self):
        
        self._vid_info = LinkExtract.get_video_all_info(self._main_link)

        for each_format in self._vid_info['formats']:
            temp: list 
            if 'audio only' in each_format['format']:
                temp = self._all_vid_links['audio']
            else:
                temp = self._all_vid_links['video']
            temp.append([ each_format['url'],each_format['format'] ])
        
        return self._all_vid_links

    @staticmethod
    def get_video_all_info(main_link: str):
        with youtube_dl.YoutubeDL({}) as ydl:
            info = ydl.extract_info(main_link, download=False)
        return info
