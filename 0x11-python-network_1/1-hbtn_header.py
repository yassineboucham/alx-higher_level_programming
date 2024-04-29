#!/usr/bin/python3
import sys
import urllib.request
url = sys.argv[1]
if url:
   with urllib.request.urlopen(url) as html:
       value = html.getheader('X-Request-Id')
print('{}'.format(value))
