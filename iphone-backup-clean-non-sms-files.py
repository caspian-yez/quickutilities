#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

import os
import time
import signal
import sqlite3
import argparse
import send2trash

sigint = False


def signal_handler(sig, frame):
    print("SIGINT")
    global sigint
    sigint = True


def main(args):
    print("backup path: {}".format(args.path))
    print("trash or permanent delete: {}".format(args.trash))

    signal.signal(signal.SIGINT, signal_handler)

    connection = sqlite3.connect(os.path.join(args.path, "Manifest.db"))
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM "Files"')

    rows = cursor.fetchall()

    database_touched = False

    # CREATE TABLE Files (
    # fileID TEXT PRIMARY KEY,
    # domain TEXT,
    # relativePath TEXT,
    # flags INTEGER,
    # file BLOB
    # )
    for row in rows:
        if sigint:
            break
        if "SMS" in row["relativePath"] and 1 == row["flags"]:
            continue
        else:
            path_to_delete = os.path.join(args.path, row["fileID"][0:2], row["fileID"])
            if os.path.exists(path_to_delete):
                if 0 == args.trash:
                    os.remove(path_to_delete)
                else:
                    send2trash.send2trash(path_to_delete)
                    time.sleep(0.02)
            cursor.execute(
                'DELETE FROM "Files" WHERE "fileID" = \'{}\''.format(row["fileID"])
            )
            database_touched = True

    if database_touched:
        cursor.execute("COMMIT")

    connection.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # define each option with: parser.add_argument
    parser.add_argument("-p", "--path", required=True, help="iPhone backup path")
    parser.add_argument(
        "-t",
        "--trash",
        required=True,
        type=int,
        help="Trash file or permanent delete, 0 is permanent delete, otherwise trash",
    )
    args = parser.parse_args()  # automatically looks at sys.argv
    main(args)
