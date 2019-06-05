import wget
import os

class Downloader (object):

    def __init__(self, urls=[], dist=''):
        self._urls = urls
        self._dist = os.path.join(os.getcwd(), 'downloads', dist)

        if not os.path.exists('downloads'):
            os.mkdir('downloads')

        if not os.path.exists(self._dist):
            os.mkdir(self._dist)

    def start(self):
        for url in self._urls:
            try:
                name = wget.download(url['url1'], self._dist, bar=wget.bar_adaptive)
            except:
                name = wget.download(url['url2'], self._dist, bar=wget.bar_adaptive)

            print(name)
