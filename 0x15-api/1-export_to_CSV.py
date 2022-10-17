#!/usr/bin/python3
"""Fetch employee todos info and export into csv format
"""
import csv
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
    with open('{}.csv'.format(argv[1]), 'w') as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["userId", "username", "completed", "title"],
            quoting=csv.QUOTE_ALL
        )
        for d in all:
            writer.writerow({
                "userId": argv[1],
                "username": username,
                "completed": d.get('completed'),
                "title": d.get('title')
            })
