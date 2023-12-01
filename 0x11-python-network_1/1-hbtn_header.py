#!/usr/bin/python3
import sys
import urllib.request

"""This script fetches a URL and displays the value of the X-Request-Id"""

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.headers['X-Request-Id'])

