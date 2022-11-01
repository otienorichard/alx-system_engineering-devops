#!/usr/bin/python3
"""Fetch number of subscribers of a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """get number of subscribers of a subreddit
    """
    data = {
        'User-agent': 'Iamabot'
    }
    r = requests.get("https://www.reddit.com/r/{}/about.json"
                     .format(subreddit),
                     headers=data,
                     allow_redirects=False
                     )
    if r.status_code != 200 or r.json().get('kind') != 't5':
        return 0
    else:
        return r.json().get('data').get('subscribers')