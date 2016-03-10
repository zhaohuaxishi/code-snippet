#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import sys
import os


def main():
    """A game to help me to remember musical scale.

    It return a random number in range[1-7], and you wile have to input
    the corresponding char represent of its, i.e.

        1 -> d (do)
        2 -> r (re)
        3 -> m (mi)
        4 -> f (fa)
        5 -> s (so)
        6 -> l (la)
        7 -> x (xi)

    Just for fun.
    """

    quit_strs = ['q', 'quit', 'e', 'exit']
    clear_strs = ['c', 'cls', 'clear']
    number_represent = [1, 2, 3, 4, 5, 6, 7]

    # put empty string at index 0, so we can use number
    # to index char derectly
    char_represent = ['', 'd', 'r', 'm', 'f', 's', 'l', 'x']

    count = 1
    while count <= 20:
        number = random.choice(number_represent)
        char = input("[{:2d}] {}: ".format(count, number))

        while char is not char_represent[number]:
            if char in clear_strs:
                os.system('clear')
                char = input("[{:2d}] {}: ".format(count, number))
                continue

            if char in quit_strs:
                sys.exit()

            char = input("[{:2d}] retry({}): ".format(count, number))

        count += 1

if __name__ == "__main__":
    main()
