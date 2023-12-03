#!/usr/bin/python3
if __name__ == "__main__":
    res = 0
    import sys
    vars = sys.argv[1:]
    for i in vars:
        res += int(i)
    print("".format(res))
