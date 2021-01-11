import numpy as np

"""
Static helper methods.
"""


def forward_substitution(original, L, b):
    """
    Forward substitution method.
    :param original: non decomposed matrix
    :param L: decomposed matrix
    :param b: vector of result
    :return: result of the substitution
    """
    if b.col != 1 or b.row != L.row:
        raise ValueError('Invalid dimensions!')

    for i in range(L.row):
        for j in range(i):
            value = b.get(i, 0) - (b.get(j, 0) * original.get(i, j))
            b.set(i, 0, value)

    return b


def backward_substitution(original, U, y):
    """
    Backward substitution method.
    :param original: non decomposed matrix
    :param U: decomposed matrix
    :param y: vector gotten by forward substitution
    :return: result of the substitution
    """
    if y.col != 1 or y.row != U.row:
        raise ValueError('Invalid dimensions!')

    i = U.row - 1
    while i >= 0:
        j = i + 1
        while j < U.row:
            value = y.get(i, 0) - (original.get(i, j) * y.get(j, 0))
            y.set(i, 0, value)
            j += 1
        if original.get(i, i) == 0:
            raise ValueError('Invalid parameter, division by zero not possible!')

        divided = y.get(i, 0) / original.get(i, i)
        y.set(i, 0, divided)
        i -= 1

    return y


def get_unit_data(dim):
    """
    Method for creating unit matrix.
    :param dim: dimension of the matrix
    :return: unit matrix
    """
    return np.identity(dim)


def count_permutations(P):
    """
    Method for counting how many times matrix's rows had been permuted.
    :param P: the permutation matrix
    :return: number of permutations
    """
    num = 0
    for i in range(P.row):
        for j in range(P.col):
            if i == j and P.get(i, j) != 1.0:
                num += 1
    return num


def find_solution(matrix, b, lup=False):
    """
    Method which solves the equation.
    :param lup: is lu or lup composition
    :param matrix: the matrix
    :param b: the vector of the solution
    :return: solution of the equation
    """
    if not matrix.is_lup:
        matrix.lup_decomposition(lup)
    y = forward_substitution(matrix, matrix.L, matrix.multiply(matrix.P, b))
    return backward_substitution(matrix, matrix.U, y)


def write_to_file(data, file):
    """
    Method which writes the given data into the file.
    :param data: data which will be written into the given file
    :param file: file in which given data will be written
    """
    rows = [line.strip().split(' ') for line in data]
    cols = zip(*rows)
    col_widths = [max(len(value) for value in col) for col in cols]
    format = ' '.join(['%%%ds' % width for width in col_widths])
    for row in rows:
        file.write(format % tuple(row))
        file.write("\n")
