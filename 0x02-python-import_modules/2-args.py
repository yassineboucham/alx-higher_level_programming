#!/usr/bin/python3
if __name__ == "__main__":
    v = 0
    import sys
    arguments = sys.argv[1:]
    print(f"{len(arguments)} argument:")
    for i in arguments:
        v += 1
        print("{}: {}".format(v, i))