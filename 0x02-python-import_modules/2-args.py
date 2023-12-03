#!/usr/bin/python3
if __name__ == "__main__":
    v = 0
    import sys
    arguments = sys.argv[1:]
    num_arg = len(arguments)
    if (num_arg == 0):
        print("0 arguments.")
    else:
        if (num_arg == 1):
            print("{} argument:".format(num_arg))
        else:
            print("{} arguments:".format(num_arg))
        for i in arguments:
            v += 1
            print("{}: {}".format(v, i))
