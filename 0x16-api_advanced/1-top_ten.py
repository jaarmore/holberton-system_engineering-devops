#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the 
titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Function that uses a reddit API to prints the
    titles of the first 10 host post.

    Args
        URL: url of the API, formatted with subreddit to search
        header: custom header to avoid error Too Many Requests
        param: the variables to pass at URL
    """
    URL = 'https://api.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {'User-Agent': 'Custom-User'}
    param = {'limit': '10'}

    resp = requests.get(URL, headers=header, params=param).json()
    try:
        for i in range(10):
            print('{}'.format(resp['data']['children'][i]['data']['title']))
    except Exception:
        print(None)
