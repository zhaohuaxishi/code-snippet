#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob


def scan_source():
    source_list = []

    source_list += glob.glob("*.cpp")
    source_list += glob.glob("*.c")

    return source_list


def generate_makefile(source_file_list, argv):
    compile_flags = " ".join(["-Wall", "-Werror", "-std=c++11"] + argv[1:])

    with open("Makefile", "w") as makefile:
        program_name_str = " ".join([name.split(".")[0]
                                     for name in source_file_list])
        print("all: " + program_name_str, file=makefile)
        print(file=makefile)

        for fname in source_file_list:
            program_name, ext = fname.split(".")
            print(program_name + ": " + fname, file=makefile)

            if ext == "cpp":
                cc = "g++"
            elif ext == "c":
                cc = "gcc"
            else:
                print("WTF: " + ext)
                continue

            tokens = ["g++", compile_flags, fname, "-o", program_name]
            print("\t" + " ".join(tokens), file=makefile)
            print(file=makefile)

        print(".PHONY: clean", file=makefile)
        print("clean:", file=makefile)
        print("\trm " + program_name_str, file=makefile)


def main(argv):
    """auto generate makefile for this directory

    each source file(.cpp, .c) in this directory is treated as a seperate
    program source
    """

    # scan source file
    source_file_list = scan_source()

    # generate Makefile
    generate_makefile(source_file_list, argv)

if __name__ == "__main__":
    import sys
    main(sys.argv)
