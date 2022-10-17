#!/usr/bin/python3
"""Fetch employee todos info and export into json format
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee id>")
        exit()
    user = requests.get(
                     "https://jsonplaceholder.typicode.com/users/{}"
                     .format(argv[1])
                    ).json()
    if not user:
        exit()
    else:
        username = user.get('username')
    all = requests.get(
                     "https://jsonplaceholder.typicode.com/todos?userId={}"
                     .format(argv[1])
                    ).json()
    j = {}
    j[argv[1]] = [{
            "task": d.get('title'),
            "completed": d.get('completed'),
            "username": username
    } for d in all]
    with open("{}.json".format(argv[1]), 'w') as f:
        json.dump(j, f)
