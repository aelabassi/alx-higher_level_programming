#!/usr/bin/python3
"""Fetches the X-Request-Id from a URL passed as an argument."""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers.get("X-Request-Id"))
