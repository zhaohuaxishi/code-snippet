#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
from bs4 import BeautifulSoup
from htmldownloader import DefaultHTMLDownloader

_prefix = "http://media.vimcasts.org/videos"

def get_video_name(content):
    soup = BeautifulSoup(content, 'lxml')

    nodes = soup.find_all('a')
    if not nodes:
        return None

    for node in nodes:
        href = node['href']
        if href.endswith('.ogv'):
            return href

    return None

def download_video(idx, name):
    url = "{prefix}/{idx}/{name}".format(prefix=_prefix, idx=idx, name=name)

    cmd = "wget {url} -O vimcasts/{idx}-{name}".format(url=url, idx=idx, name=name)
    os.system(cmd)

def main():
    downloader = DefaultHTMLDownloader()

    idx = 1
    for idx in range(1, 69):
        content = downloader.download("{}/{}".format(_prefix, idx))

        name = get_video_name(content)
        download_video(idx, name)

if __name__ == "__main__":
    main()
