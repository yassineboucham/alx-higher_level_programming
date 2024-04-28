#!/usr/bin/python3
# function that finds a peak in a list of unsorted integers
def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""
    l=list_of_integers
    for i in range(len(list_of_integers)-1):
        if l[i-1] < l[i] and l[i] < l[i+1]:
            return l[i]
    if l[0] > l[1]:
        return l[0]
    elif l[len(l) -1] > l[len(l)-2]:
        return l[len(l)]
