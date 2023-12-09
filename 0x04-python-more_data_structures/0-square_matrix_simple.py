#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result_list = list(map(lambda row: list(map(lambda a: a**2, row)), matrix))
    return (result_list)
