#!/usr/bin/python3
"""  a Python script that fetches https://intranet.hbtn.io/status"""


import requests
with requests.get('https://intranet.hbtn.io/status') as response:
    html = response.text
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
