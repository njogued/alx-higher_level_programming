#!/usr/bin/env python3
def square_matrix_simple(matrix=[]):
    mat2 = []
    for row in matrix:
        mat3 = []
        for column in row:
            mat3.append(column**2)
        mat2.append(mat3)
    return mat2
