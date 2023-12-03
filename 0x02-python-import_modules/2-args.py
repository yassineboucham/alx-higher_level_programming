#!/usr/bin/python3
v = 0
import sys
arguments = sys.argv[1:]
print(f"{len(arguments)} argument:")
for i in arguments:
    v += 1
    print(f"{v}: {i}")