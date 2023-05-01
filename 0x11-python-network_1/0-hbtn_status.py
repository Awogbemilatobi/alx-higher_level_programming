#!/usr/bin/python3
"""A script that will fetch https://alx-intranet.hbtn.io/status. using urlib package
"""


if __name__ == '__main__':

    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
        content = r.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))