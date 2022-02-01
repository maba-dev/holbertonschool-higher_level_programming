#!/usr/bin/python3
"""a script that adds all arguments to a Python list, and then save them"""


import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
try:
    list = load_from_json_file(filename)
except:
    list = []

for arg in sys.argv[1:]:
    list.append(arg)
save_to_json_file(list, filename)
