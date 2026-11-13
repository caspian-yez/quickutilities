#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
import os
import argparse
import libtorrent


def main(args):
    fp = open(args.filename, "rb")
    torrent_node = libtorrent.bdecode(fp.read())
    name_in_torrent = libtorrent.torrent_info(torrent_node).name() + ".torrent"
    fp.close()
    if os.access(name_in_torrent, os.W_OK):
        print(
            "ERROR:\n{}\nfile name exists:\n{}".format(args.filename, name_in_torrent)
        )
    else:
        tip = "renaming '{}' to '{}'".format(args.filename, name_in_torrent)
        print(tip)
        os.rename(args.filename, name_in_torrent)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # define each option with: parser.add_argument
    parser.add_argument("filename", help="Path to the input file")
    args = parser.parse_args()  # automatically looks at sys.argv
    main(args)
