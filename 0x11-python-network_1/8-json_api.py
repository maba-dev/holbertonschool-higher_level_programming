#!/usr/bin/python3
""" Search API """
import sys
import requests


if len(sys.argv) == 1:
    q = ""
else:
    q = sys.argv[1]
result = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})

try:
    data = result.json()
    if data:
        print("[{}] {}".format(data["id"], data["name"]))
    else:
        print("No result")
except:
    print("Not a valid JSON")
