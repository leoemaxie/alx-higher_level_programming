#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    url = argv[1]
    email = argv[2]
    r = requests.post(url, data={'email': email})
    print(r.text)
