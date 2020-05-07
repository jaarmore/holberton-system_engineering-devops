#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Function that uses a reddit API to get info about
    subscribers

    Args
        URL: url of the API, formatted with subreddit to search
        header: custom header to avoid error Too Many Requests
    """
    URL = 'https://api.reddit.com/r/{}/about'.format(subreddit)
    header = {'User-Agent': 'Custom-User'}

    resp = requests.get(URL, headers=header).json()
    try:
        return resp['data']['subscribers']
    except Exception:
        return 0
