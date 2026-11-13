#!/usr/bin/env python3
# SPDX-License-Identifier: MIT


def main():
    delimiter = "\t"
    header = []

    file = open("/proc/crypto", "r")
    for line in file:
        clean_line = line.strip("\n").strip("\r").strip()
        if 0 == len(clean_line):
            continue

        key = clean_line.split(":")[0].strip()
        value = clean_line.split(":")[1].strip()

        if key not in header:
            header.append(key)

    file.close()
    # print(header)
    for x in header:
        print("{}".format(x), end=delimiter)
    print("")

    row = []
    for x in header:
        row.append("")
    # print(len(row))
    file = open("/proc/crypto", "r")
    for line in file:
        clean_line = line.strip("\n").strip("\r").strip()
        if 0 == len(clean_line):
            for i in range(len(row)):
                print("{}".format(row[i]), end=delimiter)
                row[i] = ""
            print("")
            continue

        key = clean_line.split(":")[0].strip()
        value = clean_line.split(":")[1].strip()

        index = header.index(key)
        # print("index:{}".format(index))
        row[index] = value
    file.close()


if __name__ == "__main__":
    main()
