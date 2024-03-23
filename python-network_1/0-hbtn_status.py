#!/usr/bin/python3
"""
    script that fetches https://alu-intranet.hbtn.io/status
"""


import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as resp:
        html = resp.read()

        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf8')))
