#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re
from bs4 import BeautifulSoup


def get_content():
    with open("test.html") as source:
        return source.read()


def extract_headers(soup, tagname, pattern):
    headers = []
    header_tags = soup.find_all('tr', class_="t-dsc")
    for tag in header_tags:
        headnametag = tag.find(tagname)
        if headnametag:
            match = pattern.match(headnametag.contents[0])
            headername = match.group(1)
            if headername in headers:
                continue

            headers.append(headername)

    return headers


def main():
    from htmldownloader import DefaultHTMLDownloader
    downloader = DefaultHTMLDownloader()

    cppreference = 'http://en.cppreference.com/w/cpp/header'
    content = downloader.download(cppreference)
    soup = BeautifulSoup(content, 'lxml')

    # find header name like: '<string>' or '<experimental/any>
    headers = extract_headers(soup, 'tt', re.compile(r'<(\w+|\w+/\w+)>'))
    with open("cppheaderlist.txt", 'w') as headersfile:
        for header in sorted(headers):
            print(header, file=headersfile)

    creference = 'http://en.cppreference.com/w/c/header'
    content = downloader.download(creference)
    soup = BeautifulSoup(content, 'lxml')

    headers = extract_headers(soup, 'b', re.compile(r'<(\w+\.h)>'))
    with open("cheaderlist.txt", 'w') as headersfile:
        for header in sorted(headers):
            print(header, file=headersfile)

if __name__ == "__main__":
    main()
