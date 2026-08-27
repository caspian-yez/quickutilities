#!/usr/bin/env python3

# MIT License
# 
# Copyright (c) 2023 Yaofei Zheng
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sqlite3
import send2trash
import sys

def main():
    dbrootdir = r'C:\Users\Admin\AppData\Roaming\Apple Computer\MobileSync\Backup\f07c12dde64d708259d23f19ae8406b019c83a00'

    uni = list()

    con = sqlite3.connect(dbrootdir+r'\Manifest.db')
    print(con)

    c = con.cursor()

    for row in c.execute("SELECT `fileID`, `relativePath` FROM `Files`"):
        if row[1].find("SMS") == -1:
            print(row)
            uni.append(row[0])
            try:
                send2trash.send2trash(dbrootdir+'\\'+row[0][:2]+'\\'+row[0])
            except FileNotFoundError :
                print(dbrootdir+'\\'+row[0][:2]+'\\'+row[0]+' Not Found.')

    for id in uni:
        c.execute("DELETE FROM `Files` WHERE `fileID` = '{0}'".format(id))

    c.execute("COMMIT")

    con.close()

if __name__ == "__main__":
    main()
