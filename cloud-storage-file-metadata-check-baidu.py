#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
import sys
import os
import json
import hashlib


def main():
    if 2 != len(sys.argv):
        print("Please pass the json file after {}".format(sys.argv[0]))
        return
    f = open(sys.argv[1], "r")
    metadata = json.load(f)
    # print(metadata["list"])
    for file_metadata in metadata["list"]:
        if 1 != file_metadata["isdir"]:
            filename = os.path.basename(file_metadata["path"])
            if os.path.exists(filename):
                # print(filename)
                md5sum = hashlib.md5(open(filename, "rb").read()).hexdigest()
                # print("file md5: {}".format(md5sum))
                # print("metadata md5: {}".format(file_metadata["md5"]))
                if md5sum == file_metadata["md5"].lower():
                    print("File MD5 OK: {}".format(filename))
                else:
                    print("File MD5 mismatch: {}".format(filename))
            else:
                print("File do not exists: {}".format(filename))


if __name__ == "__main__":
    main()
