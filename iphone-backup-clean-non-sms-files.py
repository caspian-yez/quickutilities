#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

import sys
import os
import sqlite3
import send2trash


def main():
    print("backup path: {}".format(sys.argv[1]))

    base_dir = sys.argv[1]
    connection = sqlite3.connect(os.path.join(base_dir, "Manifest.db"))
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM "Files"')

    rows = cursor.fetchall()

    # CREATE TABLE Files (
    # fileID TEXT PRIMARY KEY,
    # domain TEXT,
    # relativePath TEXT,
    # flags INTEGER,
    # file BLOB
    # )
    for row in rows:
        if "SMS" in row["relativePath"]:
            continue
        else:
            try:
                path_to_delete = os.path.join(
                    base_dir, row["fileID"][0:2], row["fileID"]
                )
                send2trash.send2trash(path_to_delete)
                cursor.execute(
                    'DELETE FROM "Files" WHERE "fileID" = \'{}\''.format(row["fileID"])
                )
            except FileNotFoundError:
                print("{} Not Found.".format(path_to_delete))

    cursor.execute("COMMIT")

    connection.close()


if __name__ == "__main__":
    main()
