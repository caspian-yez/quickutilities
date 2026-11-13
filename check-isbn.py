#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
import isbnlib
import os


def main():
    HEADER___ = "\033[95m"
    OKBLUE___ = "\033[94m"
    OKGREEN__ = "\033[92m"
    WARNING__ = "\033[93m"
    FAIL_____ = "\033[91m"
    ENDC_____ = "\033[0m"
    BOLD_____ = "\033[1m"
    UNDERLINE = "\033[4m"
    for file in os.listdir():
        str13 = file[0:13]
        str10 = file[0:10]
        if isbnlib.is_isbn13(str13):
            print("{}{}{} {}".format(OKGREEN__, "ISBN      OK:", ENDC_____, file))
        elif isbnlib.is_isbn10(str10):
            str13 = isbnlib.to_isbn13(str10)
            newfilename = str13 + file[10:]
            os.rename(file, newfilename)
            print(
                "{}{}{} {}".format(OKGREEN__, "ISBN      OK:", ENDC_____, newfilename)
            )
        else:
            print("{}{}{} {}".format(FAIL_____, "ISBN Invalid:", ENDC_____, file))


if __name__ == "__main__":
    main()
