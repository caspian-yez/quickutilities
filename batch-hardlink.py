#!/usr/bin/env sh
# SPDX-License-Identifier: MIT

import os
import sys


def main():
    # print("Argument of file: {}".format(sys.argv[1]))
    current_working_dir = os.path.abspath(os.getcwd())
    # print("Current Working Dir: {}".format(current_working_dir))
    filelist = open(sys.argv[1], 'r')
    lines = filelist.readlines()
    count = 0
    for line in lines:
        src_path = line.strip('\r').strip('\n')
        # print(os.path.basename(src_path) )
        dest = os.path.join(current_working_dir, os.path.basename(src_path))
        # print(dest)
        count += 1
        # print("Line {}: {}".format(count, src_path))
        try:
            os.link(src_path, dest)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
