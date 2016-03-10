#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re
from bs4 import BeautifulSoup


class DefaultHTMLParser:

    def _find_new_links(self, soup):
        """Find all book links in this page.

        Current book link form:

            http://book.douban.com/subject/26701959/."""

        href_pattern = re.compile(r'http://book.douban.com/subject/\d+.*')
        link_nodes = soup.find_all('a', href=href_pattern)

        new_links = set()
        for node in link_nodes:
            new_links.add(node['href'])

        return new_links

    def _find_book_meta_info(self, book_node):
        """Find the basic information about the book.

        All meta info looks like this:

            <span class='pl'>出版社：</span> " 上海人民出版社"<br>
        """

        meta_info = {}
        spans = book_node.find_all('span', class_='pl')

        # 作者译者和丛书需要单独处理

        need_find_link = ['作者', '译者']
        for span in spans:
            key_str = span.string.strip()

            if key_str in need_find_link:
                value_str = span.find_next_sibling('a').string.strip()
            else:
                key_str = key_str[:key_str.find(':')]
                value_str = span.next_sibling.strip()

            meta_info[key_str] = value_str

        if '丛书' in meta_info:
            serial_pattern = re.compile('http://book.douban.com/series/\d+')
            serial = book_node.find('a', href=serial_pattern)
            meta_info['丛书'] = serial.string
        return meta_info

    def _find_rate_info(self, book_node):
        """
        Find the rate of this book
        """

        strong_tag = book_node.find(
            'strong', class_="ll rating_num ", property="v:average")
        return strong_tag.string.strip()

    def _find_usageful_infomation(self, soup):
        useful_info = {}

        book_name = soup.find('div', id='wrapper').find('h1').find(
            'span', property="v:itemreviewed").get_text().strip()
        useful_info['book_name'] = book_name

        subjectwrap = soup.find('div', class_='subjectwrap')

        metas = self._find_book_meta_info(subjectwrap)
        useful_info['metas'] = metas

        rate = self._find_rate_info(subjectwrap)
        useful_info['rate'] = rate

        return useful_info

    def parse(self, url, content):
        """Parse the conent, find new links and useful information."""

        soup = BeautifulSoup(content)

        new_links, useful_info = None, None

        try:
            new_links = self._find_new_links(soup)
        except Exception:
            print("can not find new links")

        try:
            useful_info = self._find_usageful_infomation(soup)
        except Exception:
            print("can not find useful infomation")

        return new_links, useful_info


def main():
    from htmldownloader import DefaultHTMLDownloader

    test_html = 'http://book.douban.com/subject/26701959/'
    downloader = DefaultHTMLDownloader()
    test_content = downloader.download(test_html)

    htmlparser = DefaultHTMLParser()
    new_links, useful_info = htmlparser.parse(test_content)

    # print new links
    for links in new_links:
        print(links)

    # print book info
    print("=========================================")
    print("{book_name:} : {rate:}".format(**useful_info))
    for key, val in useful_info['metas'].items():
        print('- {:10} : {}'.format(key, val))
    print("=========================================")

    print("-- {:30} : {} --".format(__file__, 'PASS'))

if __name__ == "__main__":
    main()
