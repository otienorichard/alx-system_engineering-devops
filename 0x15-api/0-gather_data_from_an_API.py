#!/usr/bin/python3
"""Fetch employee todos info
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee id>")
        exit()
    user = requests.get(
                     "https://jsonplaceholder.typicode.com/users/{}"
                     .format(argv[1])
                    ).json()
    if not user:
        exit()
    else:
        name = user.get('name')
    all = requests.get(
                     "https://jsonplaceholder.typicode.com/todos?userId={}"
                     .format(argv[1])
                    ).json()
    dones = [i for i in all if i.get('completed')]
    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(dones), len(all)))
    for d in dones:
        print("\t {}".format(d.get('title')))
