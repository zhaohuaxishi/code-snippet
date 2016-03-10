#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class DataHanlder():
    """The default crawl data handler."""

    def handle(self, data):
        if not data:
            return None

        # print book info
        print("=========================================")
        print("{book_name:} : {rate:}".format(**data))
        for key, val in data['metas'].items():
            print('- {:10} : {}'.format(key, val))
        print("=========================================")


def main():
    data = {
        'book_name': '我脑袋里的怪东西',
        'rate': '8.6',
        'metas': {
            '出版社': '上海人民出版社',
            '作者': '[土耳其] 奥尔罕·帕慕克'
        }
    }

    datahandler = DataHanlder()
    datahandler.handle(data)

    datahandler.handle(None)

    print("-- {:30} : {} --".format(__file__, 'PASS'))

if __name__ == "__main__":
    main()
