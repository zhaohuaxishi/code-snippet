#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This is script that i used to convert my github pages blog source file name
to the canonical name like this:

    2016-01-01-update-blog-with-hexo.md

author: grf
date: 2016-02-24
"""

import os
import re
import glob
import shutil

def need_convert(file_name):
    canonical_name_pattern = re.compile(r'\d{4}-\d{2}-\d{2}-\w+')
    if canonical_name_pattern.match(file_name):
        return False

    return True

def add_date_to_filename(file_name, date):
    new_file_name = date + '-' + file_name
    shutil.move(file_name, new_file_name)

def do_convert(file_name):
    """Do the actual name convertion

    The file given must have date information like this form:

        date: 2014-09-06

    otherwise RuntimeError is raised
    """
    with open(file_name) as file:
        for line in file:
            if line.startswith('date:'):
                date_line = line[len('date:'):].strip()
                break
        else:
            raise RuntimeError('do not have date info in file: ', file_name)

        date_pattern = re.compile(r'(\d{4}-\d{2}-\d{2}).*')
        match = date_pattern.match(date_line)
        if not match:
            raise RuntimeError('unkonw date format', date_line)
        date = match.group(1)

        add_date_to_filename(file_name, date)

def convert_to_canonical(file_list):
    for file_name in file_list:
        if not need_convert(file_name):
            continue

        do_convert(file_name)

def main(argv):
    """Convert blog source name to canonical format.

    if arg provide use the first one as the root path.
    """

    path = '.'
    if len(argv) > 1:
        path = argv[1]

    os.chdir(path)
    file_list = glob.glob('*.md')
    convert_to_canonical(file_list)

if __name__ == "__main__":
    import sys
    main(sys.argv)
