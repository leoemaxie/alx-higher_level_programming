#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8)
"""

if __name__ == "__main__":
    import urllib.request
    from sys import argv
    from urllib.error import HTTPError

    url = argv[1]
    try:
        with urllib.request.urlopen(url) as r:
            print(r.read().decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
