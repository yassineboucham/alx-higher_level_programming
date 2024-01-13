#!/usr/bin/python3
"""tan9alt"""


def pascal_triangle(n):
    """no9Al"""
    if n <= 0:
        return []
    list = []
    while len(list) != n:
        tri = list[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        list.append(tmp)
    return list
        