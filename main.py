from RJ.scraper import WebScrapper
from RJ.downloader import Downloader

def main():

    playlist_id = input('Enter the id of playlist: ')

    try:
        scraper = WebScrapper(playlist_id)
        downloader = Downloader(scraper.get_playlist(), scraper.get_playlist_name())
        downloader.start()
    except Exception as err:
        print(err)


if __name__ == '__main__':
    main()
