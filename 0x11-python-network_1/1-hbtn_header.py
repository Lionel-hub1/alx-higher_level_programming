#!/usr/bin/python3
import sys
import urllib.request

"""This script fetches a URL and displays the value of the X-Request-Id"""

url = sys.argv[1]

with urllib.request.urlopen(request) as response:
    print(dict(response.headers).get("X-Request-Id"))

