#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

import os
import sys
import time


def main():
    while os.path.exists(sys.argv[1]):
        print("{} exists".format(sys.argv[1]))
        time.sleep(1)

    os.system("reboot")


if __name__ == "__main__":
    main()
