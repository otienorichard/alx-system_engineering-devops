#!/usr/bin/python3
"""Fetch top ten posts of a subreddit
"""
import requests


def top_ten(subreddit):
    """get top ten posts of a subreddit
    """
    data = {
        'User-agent': 'Iamabot',
    }
    r = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                     .format(subreddit),
                     headers=data,
                     allow_redirects=False
                     )
    if r.status_code != 200:
        print(None)
    else:
        posts = r.json().get('data').get('children')
        for post in posts:
            print(post.get('data').get('title'))