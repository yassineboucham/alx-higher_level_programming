#!/usr/bin/python3
if __name__ == "__main__":
    v = 0
    import sys
    arguments = sys.argv[1:]
    if (len(arguments) == 0):
        print("{} argument.".format(len(arguments)))
    else:
        print("{} argument:".format(len(arguments)))
        for i in arguments:
            v += 1
            print("{}: {}".format(v, i))
