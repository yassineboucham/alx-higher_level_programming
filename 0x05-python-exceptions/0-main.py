#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = [1, 2, 3, 4]
x = 0

nb_print = safe_print_list(my_list, x)
print("{:d}".format(nb_print))