#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id"""


import requests
import sys
if __name__ == "__main__":
    header = requests.get(sys.argv[1])
    print(header.headers.get("X-Request-Id"))
