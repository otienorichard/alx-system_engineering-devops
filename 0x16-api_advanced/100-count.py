#!/usr/bin/python3
"""Fetch top ten posts of a subreddit
"""
import requests


def count_words(subreddit, word_list, after=None, d=None):
    """get all posts of a subreddit
    and count key words
    """
    data = {
        'User-agent': 'Iamabot'
    }
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after:
        url += "?after={}".format(after)
    if not d:
        d = {k.lower(): 0 for k in word_list}
    r = requests.get(url,
                     headers=data,
                     allow_redirects=False
                     )
    if r.status_code != 200:
        return None
    else:
        posts = r.json().get('data').get('children')
        for post in posts:
            twords = post.get('data').get('title').lower().split(' ')
            for tword in twords:
                if tword in word_list:
                    d[tword] += 1
        if r.json().get('data').get('after'):
            return count_words(
                subreddit,
                after=r.json().get('data').get('after'),
                word_list=word_list,
                d=d
            )
        res = [(k, v) for k, v in d.items()]
        res.sort(key=lambda x: x[1], reverse=True)
        for r in res:
            if r[1] > 0:
                print("{}: {}".format(r[0], r[1]))