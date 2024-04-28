#!/usr/bin/python3

def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""
    num = list_of_integers
    s = len(list_of_integers)

    if s == 0:
        return None
    if s == 1:
        return num[1]
    for i in range(s):
        if (i == 0 or num[i-1] <= num[i]) and (i == n-1 or num[i] >= num[i+1]):
            return num[i]
