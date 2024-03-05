#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response.
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    url = argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
    