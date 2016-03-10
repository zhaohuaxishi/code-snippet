#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from htmldownloader import HTMLDownloadError


class Crawler:
    """Simple crawler template class"""

    def __init__(self, data_handler, url_manger, html_downloader, html_parser):
        self.data_handler = data_handler
        self.url_manger = url_manger
        self.html_downloader = html_downloader
        self.html_parser = html_parser

    def crawl(self, staring_url):
        assert staring_url, 'staring_url is None'
        assert len(staring_url) != 0, 'staring_url is empty'

        self.url_manger.clear()
        self.url_manger.add_url(staring_url)
        while self.url_manger.has_new_url():
            url = self.url_manger.get_new_url()
            try:
                content = self.html_downloader.download(url)
            except HTMLDownloadError as err:
                print('{ -- fail to download url: {}'.format(err))
            else:
                new_links, useful_info = self.html_parser.parse(url, content)

                self.url_manger.add_urls(new_links)
                self.data_handler.handle(useful_info)

    __crawl = crawl


def main():
    from datahandler import DataHanlder
    from urlmanger import UrlMangerCreator
    from htmldownloader import HTMLDownloaderCreator
    from htmlparser import HTMLParserCreator

    crawler = Crawler(DataHanlder(), UrlMangerCreator.CreateManger(),
                      HTMLDownloaderCreator.CreateDownloader(),
                      HTMLParserCreator.CreateParser())

    crawler.crawl("http://book.douban.com/")

    print("-- {:30} : {} --".format(__file__, 'PASS'))

if __name__ == "__main__":
    main()
