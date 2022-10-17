#!/usr/bin/python3
"""Fetch all employees todos info and export into json format
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    d = {}
    for user in users:
        tasks = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}"
            .format(user.get('id'))
        ).json()
        d[user.get('id')] = [{
            "username": user.get('username'),
            "task": task.get('title'),
            "completed": task.get('completed')
        } for task in tasks]
    with open('todo_all_employees.json', 'w') as f:
        json.dump(d, f)
