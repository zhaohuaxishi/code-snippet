#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
A spider to crawl the book information from `book.douban.com`

I love reading but don't want to wast my time on terrible books. So i always
read the book rate and comment from `book.douban.com` to help me to decide
whether i should read one or not.

Sometimes i want to find some book about one area, and i want to find the
best book i can get, and i use `book.douban.com` to help me with this.

And now, since i just leaned python, i want to automate all these stuffs.

This program can:

    - Get book information from `book.douban.com`

Author: guorongfei@126.com
date: 2016-02-25
"""

from crawler import Crawler
from datahandler import DataHanlder
from urlmanger import DefaultUlrManger
from htmldownloader import DefaultHTMLDownloader
from htmlparser import DefaultHTMLParser


def main(argv):
    """The entry of crawler.

    Args:
        argv: get the staring url if provide
    """

    staring_url = 'http://book.douban.com/'
    if len(argv) > 1:
        staring_url = argv[1]

    crawler = Crawler(DataHanlder(), DefaultUlrManger(),
                      DefaultHTMLDownloader(), DefaultHTMLParser())

    try:
        crawler.crawl(staring_url)
    except Exception:
        print('******** error ********')


if __name__ == "__main__":
    import sys
    main(sys.argv)
