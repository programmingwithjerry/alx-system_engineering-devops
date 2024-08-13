#!/usr/bin/python3
"""
Recursive function to query the Reddit API and collect
titles of all hot articles for a specified subreddit.
Returns None if the subreddit is invalid or no results are found.
"""

import requests

def recurse(subreddit, titles_list=[], next_after=""):
    """
    Retrieves and returns a list of titles for all hot articles
    from the specified subreddit.
    
    - Returns None if the subreddit is not valid.
    """
    api_endpoint = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Custom"}
    params = {"after": next_after}

    response = requests.get(api_endpoint, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json().get("data", {})
        posts = data.get("children", [])
        for post in posts:
            post_data = post.get("data", {})
            title = post_data.get("title")
            titles_list.append(title)
        
        next_after = data.get("after")
        
        if next_after:
            return recurse(subreddit, titles_list, next_after)
        else:
            return titles_list
    else:
        return None
