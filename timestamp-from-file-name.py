#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
import os
import datetime
import stat


def main():
    for file in os.listdir():
        if os.path.isfile(file):
            strings = file.split(" ")
            try:
                timestamp = datetime.datetime.fromisoformat(strings[0])
                amtime = timestamp.timestamp(), timestamp.timestamp()
                os.utime(file, times=amtime)
                # change permissions
                os.chmod(
                    file,
                    stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH,
                )
            except Exception as e:
                print("Exception: {}".format(e))
                print("filename {} cannot convert to ISO date".format(file))
                continue


if __name__ == "__main__":
    main()
