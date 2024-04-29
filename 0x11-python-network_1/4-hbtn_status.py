#!/usr/bin/python3
"""
 Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as html:
    fetch = html.read()
print("Body response:")
print("\t- type: {}".format(type(fetch)))
print("\t- content: {}".format(fetch.decode("utf-8")))
