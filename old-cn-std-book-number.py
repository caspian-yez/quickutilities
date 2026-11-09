#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

import os
import parse

# '·' is the separator


def match_and_rename_file(patten: str, file: str) -> bool:
    function_result = False
    ret = parse.parse(patten, file)
    if ret is not None:
        if ret[0].isdigit() and ret[1].isdigit():
            newfile = "{}·{:04d} {}".format(ret[0], int(ret[1]), ret[2])
            print('renaming "{}" to "{}"'.format(file, newfile))
            os.rename(file, newfile)
            function_result = True

    return function_result


def process_one_file(file: str):
    list_patten = [
        "{}·{}.{}",
        "{}.{}.{}",
        "{}-{}.{}",
        "{}·{} {}",
        "{}.{} {}",
        "{}-{} {}",
    ]
    for patten in list_patten:
        if match_and_rename_file(patten, file):
            return


def main():
    for file in os.listdir():
        if not os.path.isfile(file):
            continue

        print("processing {}".format(file))
        process_one_file(file)
        print("")


if __name__ == "__main__":
    main()
