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
    for item in metadata["items"]:
        # print(item)
        if "content_hash" in item.keys() and "name" in item.keys():
            if os.path.exists(item["name"]):
                sha1 = hashlib.sha1(open(item["name"], "rb").read()).hexdigest()
                # print(sha1)
                if sha1 == item["content_hash"].lower():
                    print("File SHA1 OK: {}".format(item["name"]))
                else:
                    print("File SHA1 mismatch: {}".format(item["name"]))
            else:
                print("File do not exists: {}".format(item["name"]))


if __name__ == "__main__":
    main()
