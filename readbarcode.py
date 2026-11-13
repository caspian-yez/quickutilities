#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
import sys
import cv2
from pyzbar.pyzbar import decode


def main():
    img = cv2.imread(sys.argv[1])
    decode_result = decode(img)
    if not decode_result:
        print("No barcode detected")
    else:
        for barcode in decode_result:
            x, y, w, h = barcode.rect
            cv2.rectangle(
                img, (x - 10, y - 10), (x + w + 10, y + h + 10), (255, 0, 0), 2
            )
            if barcode.data != "":
                print(barcode.data)
                print(barcode.type)

    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
