#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        print("nb_print: {}".format(my_list[x]))
    except IndexError:
        for list in my_list:
            j += 1
            print("{}".format(list), end="")
        print("nb_print: {}".format(my_list[j]))
