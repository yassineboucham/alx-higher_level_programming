#!/usr/bin/python3
import sys
import urllib.request
if __name__ == "__main__":
    url = sys.argv[1]
    if url:
        with urllib.request.urlopen(url) as html:
            html = html.info()
            value = html.get('X-Request-Id')
        print('{}'.format(value))
