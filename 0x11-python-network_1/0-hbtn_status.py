#!/usr/bin/python3

if __name__ == "__main__":
    """Python script that fetches https://alx-intranet.hbtn.io/status"""
    import urllib.request
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as r:
        html = r.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
