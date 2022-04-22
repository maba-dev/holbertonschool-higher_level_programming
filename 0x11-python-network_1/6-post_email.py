#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    data = requests.post(values)
    data = data.encode('ascii')
    req = requests.post(url, data).text
    print(req)
