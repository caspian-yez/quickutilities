#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
import os
import requests
import bs4


def main():
    dmtf_std_url = "https://www.dmtf.org/standards/published_documents"
    page = requests.get(dmtf_std_url)
    # print(type(page.text))
    # print(page.text)

    soup = bs4.BeautifulSoup(page.text, "html.parser")
    # print(type(soup))

    # DMTF Specifications
    table = soup.find("table", id="views-aggregator-datatable--2")
    # print(type(table))
    # print(table)

    for data in table.find_all("tbody"):
        for row in data.find_all("tr"):
            # print(row)
            # print(type(row))
            file_url = row.find_all("td")[0].find_all("a")[0].attrs["href"]
            print(file_url)
            # print(type(file_url))
            filename = os.path.basename(file_url)
            if os.path.exists(filename):
                continue
            else:
                response = requests.get(file_url)
                open(filename, "wb").write(response.content)


if __name__ == "__main__":
    main()
