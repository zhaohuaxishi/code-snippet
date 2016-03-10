#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import contextlib
from urllib.error import HTTPError
from urllib import request


class HTMLDownloadError(Exception):
    """The default error to represent an html page download error.

    Attributes:
        url: The url that fail to download.
        code: The error code.
        reason: The human readable reason msg
    """

    def __init__(self, url, code, reason):
        self.url = url
        self.code = code
        self.reason = reason

    def __str__(self):
        msg = ''
        if self.url:
            msg = msg + str(self.url)

        if self.reason:
            msg = '{} : {}'.format(msg, str(self.reason))

        if self.code:
            msg = '{} ({}) '.format(msg, self.code)

        return msg


class DefaultHTMLDownloader:
    """Default html downloader use urllib.request
    """

    """Download html page from given url.
    Args:
        url: the html page to download

    Returns:
        the cotent of the html page

    Raises:
        HTMLDownloadError: if error occurred when download page
    """

    def download(self, url):
        try:
            with contextlib.closing(request.urlopen(url)) as response:
                return response.read()
        except HTTPError as err:
            raise HTMLDownloadError(url, err.code, err.reason)


def main():
    downloader = DefaultHTMLDownloader()

    try:
        downloader.download("http://book.douban.com/")
        downloader.download("http://blog.guorongfei.com/type")
    except HTMLDownloadError as err:
        print(err)

    print("-- {:30} : {} --".format(__file__, 'PASS'))

if __name__ == "__main__":
    main()
