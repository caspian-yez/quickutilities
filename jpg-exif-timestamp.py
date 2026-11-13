#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
import os
import exifread
import datetime
import stat


def process_one_file(filename: str):
    f = open(filename, "rb")
    tags = exifread.process_file(f)
    f.close()
    # print(tags)
    # print(type(tags["Image DateTime"]))
    list_time_strings = tags["EXIF DateTimeOriginal"].values.split(" ")
    # print(list_time_strings)
    str_iso_datetime = "{}T{}+08:00".format(
        list_time_strings[0].replace(":", "-"), list_time_strings[1]
    )
    print(str_iso_datetime)
    timestamp = datetime.datetime.fromisoformat(str_iso_datetime)
    creation_time = timestamp.timestamp()
    os.utime(filename, (creation_time, creation_time))
    # change permissions
    os.chmod(
        filename,
        stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH,
    )


def main():
    files = os.listdir()
    for file in files:
        if file.lower().endswith(".jpg"):
            process_one_file(file)


if __name__ == "__main__":
    main()
