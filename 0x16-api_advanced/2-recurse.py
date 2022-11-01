#!/usr/bin/python3
"""Fetch top ten posts of a subreddit
"""
import requests


def recurse(subreddit, after=None, hot_list=[]):
    """get all posts of a subreddit
    """
    data = {
        'User-agent': 'Iamabot'
    }
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after:
        url += "?after={}".format(after)
    r = requests.get(url,
                     headers=data,
                     allow_redirects=False
                     )
    if r.status_code != 200:
        return None
    else:
        posts = r.json().get('data').get('children')
        for post in posts:
            hot_list.append(post.get('data').get('title'))
        if r.json().get('data').get('after'):
            return recurse(
                subreddit,
                after=r.json().get('data').get('after'),
                hot_list=hot_list
            )
        return hot_list