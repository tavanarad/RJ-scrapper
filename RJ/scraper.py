import json
import re
from requests import get
from bs4 import BeautifulSoup

class WebScrapper (object):

    def __init__(self, playlist_id):
        self._playlist_array = []
        self._default_download_url = 'https://host%d.rjmusicmedia.com/media/mp3/mp3-256/%s.mp3?playlist=' + playlist_id
        self._html = None
        self._playlist_id = playlist_id
        self._playlist_url = 'https://www.radiojavan.com/mp3s/playlist_start?id=%s' % playlist_id

        self._get_html()
        self._find_playlist_array()
        self._find_playlist_name()

    def _get_html(self):
        try:
            self._html = get(self._playlist_url)
        except Exception as err:
            raise Exception(
                '''
                Error:
                    Cannot fetch the page %s: 
                    %s
                ''' % (self._playlist_url, err)
            )

    def _find_playlist_array(self):
        try:
            script = BeautifulSoup(self._html.text, features="html.parser").find('script', text=re.compile('RJ.relatedMP3'))
            self._playlist_array = json.loads(re.compile(r'(\[.*\])').search(script.get_text()).group(1))
        except Exception as err:
            raise Exception(
                '''
                Error:
                    Cannot find the playlist's items: 
                    %s
                ''' % err
            )

    def _find_playlist_name(self):
        try:
            breadcrumbs = BeautifulSoup(self._html.text, features='html.parser').find('ul', {'class': 'breadcrumbs'})
            self._playlist_name = breadcrumbs.find('a', {'href': re.compile(self._playlist_id)}).get_text()
        except Exception as err:
            raise Exception(
                '''
                Error:
                    Cannot find the playlist's name: 
                    %s
                ''' % err
            )

    def _get_download_urls(self, item):
        return({
            'url1': self._default_download_url % (1, item['next']),
            'url2': self._default_download_url % (2, item['next']),
        })

    def get_playlist(self):
        return list(map(lambda p: self._get_download_urls(p), self._playlist_array))

    def get_playlist_name(self):
        return self._playlist_name
