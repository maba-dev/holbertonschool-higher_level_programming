#!/usr/bin/python3
""" manage urllib.error.HTTPError exceptions and print: Error code:"""


import requests
import sys
if __name__ == "__main__":
    data = requests.get(sys.argv[1])
    try:
        if data.status_code >= 400:
            print("Error code:", data.status_code)
        else:
            print(data.text)
    except KeyError:
        pass
