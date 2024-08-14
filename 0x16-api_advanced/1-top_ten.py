#!/usr/bin/python3
"""
Fetches and prints the titles of the top 10 hot posts
from a specified subreddit using the Reddit API.
"""

import requests


def top_ten(subreddit):
    """
    Retrieves and displays the titles of the top 10 hot posts for the given subreddit.
    - Prints None if the subreddit is invalid.
    """
    api_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Custom"}
    params = {"limit": 10}

    response = requests.get(api_url, headers=headers, params=params)

    if response.status_code == 200:
        posts = response.json().get("data", {}).get("children", [])
        for post in posts:
            post_data = post.get("data", {})
            title = post_data.get("title")
            print(title)
    else:
        print(None)
