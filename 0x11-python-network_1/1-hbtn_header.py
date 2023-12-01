#!/usr/bin/python3
import urllib.request
import sys

"""This script fetches a URL and displays the value of the X-Request-Id"""

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.getheader('X-Request-Id')
        print(header)
