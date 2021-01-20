#!/usr/bin/python3
""" Write a script that adds all arguments to list, save them """
from sys import argv
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if os.path.isfile("add_item.json"):
    new_list = load_from_json_file("add_item.json")
else:
    new_list = []
for i in range(1, len(argv)):
    new_list.append(argv[i])
save_to_json_file(new_list, "add_item.json")
