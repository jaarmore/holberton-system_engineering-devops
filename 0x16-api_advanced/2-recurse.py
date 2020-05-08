#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """
    Recursive function that queries the Reddit API.

    Args
        URL: url of the API, formatted with subreddit to search
        header: custom header to avoid error Too Many Requests
        param: the variables to pass at URL
    """
    URL = 'https://api.reddit.com/r/{}/hot'.format(subreddit)
    header = {'User-Agent': 'Custom-User'}
    param = {'after': after}

    resp = requests.get(URL, headers=header, params=param).json()
    try:
        top = resp['data']['children']
        sig = resp['data']['after']
        for item in top:
            hot_list.append(item['data']['title'])
        if sig is not None:
            recurse(subreddit, hot_list, sig)
        return hot_list
    except Exception:
        return None
