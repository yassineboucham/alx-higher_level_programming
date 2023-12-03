#!/usr/bin/python3
res = 0
import sys
vars = sys.argv[1:]
for i in vars:
    res += int(i)
print(res)