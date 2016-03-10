#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class DefaultUlrManger:
    """Use set to implement the urlmanger
    """

    def __init__(self):
        self.urls_to_crawl = set()
        self.urls_crawled = set()

    def _is_valid_url(self, url):
        if url is None or len(url) == 0:
            return False

        if not url.startswith('http'):
            return False

        return True

    def clear(self):
        self.urls_to_crawl.clear()

    def has_new_url(self):
        return len(self.urls_to_crawl) != 0

    def get_new_url(self):
        new_url = self.urls_to_crawl.pop()
        self.urls_crawled.add(new_url)
        return new_url

    def add_url(self, url):
        assert self._is_valid_url(url), 'url invalid'

        if url in self.urls_crawled:
            return

        self.urls_to_crawl.add(url)

    def add_urls(self, urls):
        assert urls, 'urls is None: {}'.format(__file__)

        for url in urls:
            self.add_url(url)


def main():
    url_manger = DefaultUlrManger()
    url_manger.add_url("http://book.douban.com/")
    url_list = ['http://book.douban.com/',
                'http://book.douban.com/',
                'http::/www.baidu.com']
    url_manger.add_urls(url_list)

    while url_manger.has_new_url():
        print(url_manger.get_new_url())

    print("-- {:30} : {} --".format(__file__, 'PASS'))

if __name__ == "__main__":
    main()
