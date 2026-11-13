#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
import bs4
import sys


def main():
    f = open(sys.argv[1])
    soup = bs4.BeautifulSoup(f.read(), "html.parser")
    for link in soup.findAll("a"):
        print(link.get("href"))


if __name__ == "__main__":
    main()
