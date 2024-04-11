#!/usr/bin/python3

def matrix_divided(matrix, div):
    divs = []
    for mat in matrix:
        if len(mat) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        if type(div) not in (int, float):
            raise TypeError("div must be a number")
        row = []
        for element in mat:
            if div == 0:
                raise ZeroDivisionError("division by zero")
            if type(element) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            row.append(round(element / div, 2))
        divs.append(row)
    return divs
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
