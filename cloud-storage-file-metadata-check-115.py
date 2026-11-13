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
    # print(metadata["data"])
    for item in metadata["data"]:
        # print(item)
        if "sha" in item:
            if os.path.exists(item["n"]):
                sha1 = hashlib.sha1(open(item["n"], "rb").read()).hexdigest()
                # print(sha1)
                if sha1 == item["sha"].lower():
                    print("File SHA1 OK: {}".format(item["n"]))
                else:
                    print("File SHA1 mismatch: {}".format(item["n"]))
            else:
                print("File do not exists: {}".format(item["n"]))


if __name__ == "__main__":
    main()
