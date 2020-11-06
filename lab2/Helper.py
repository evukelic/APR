import copy
from Constants import *
from Function import *

"""
Static helper methods.
"""


def search(xp, delta, function):
    """
    Searches for the next point when given previous one.
    :param xp: Initial point
    :param delta: Shift
    :param function: Function which will be minimized
    :return: Next point
    """
    try:
        x = list(xp)
    except TypeError:
        x = [xp]

    for i in range(len(x)):
        P = function.calculate(x)
        x[i] = x[i]+delta
        N = function.calculate(x)
        if N > P:
            x[i] = x[i]-2*delta
            N = function.calculate(x)
            if N > P:
                x[i] = x[i]+delta

    return tuple(x)


def get_list(point):
    """
    Transforms the point in the list.
    :param point: Point as tuple or double value
    :return: Point as list
    """
    try:
        x = list(point)
    except TypeError:
        x = [point]
    return x


def simplex(point, move):
    """
    Calculates starting simplex for given point and move.
    :param point: Point
    :param move: The shift
    :return: Simplex points
    """
    points = []
    x = get_list(point)
    points.append(x)
    for i in range(len(x)):
        p = copy.deepcopy(x)
        p[i] = x[i]+move
        points.append(p)

    return points


def minmax_index(points, function, min=True):
    """
    Finds index of the point from given set of points for which will the function have the biggest/smallest value.
    :param points: Set of the points
    :param function: Function
    :param min: is min or max index
    :return: Min or max index
    """
    index = 0
    value = function.calculate(points[0])
    for i in range(len(list(points))):
        if i == 0:
            continue
        new = function.calculate(points[i])
        if min:
            if new < value:
                index = i
                value = new
        else:
            if new > value:
                index = i
                value = new
    return index


def centroid(points, index, n):
    """
    Calculates centroid for the given point list.
    :param points: Points
    :param index: point which will be skipped
    :return: Centroid
    """
    cent = [0 for i in range(n)]
    for i in range(len(list(points))):
        if i != index:
            res = points[i]
            cent = [a+b for a, b in zip(cent, res)]

    cent = [c/n for c in cent]

    return cent


def rec(xc, x, const):
    """
    Calculates either reflection, expansion or contraction.
    :param xc: Centroid
    :param x: Second point
    :param const: Constant needed for the operation
    :return: Result of the operation
    """
    res = []
    for i in range(len(list(xc))):
        if const == ALPHA:
            elem = (1 + const) * xc[i] - const * x[i]
        elif const == GAMMA:
            elem = (1 - const) * xc[i] + const * x[i]
        else:
            elem = (1 - const) * xc[i] + const * x[i]
        res.append(elem)
    return res


def should_stop(points, xc, function):
    """
    Stop condition for the Nelder-Mead algorithm.
    :param points: Points
    :param xc: Centroid
    :param function: Function
    :return: Should the algorithm stop
    """
    res = 0
    for i in range(len(list(points))):
        res += math.pow((function.calculate(points[i])-function.calculate(xc)), 2)
    val = math.sqrt(res/len(list(points)))
    return val <= EPSILON


def shrink(xl, points):
    new = []
    for i in range(len(list(points))):
        xi = points[i]
        p = []
        for j in range(len(list(xl))):
            p.append(xl[j]*(1-SIGMA)-SIGMA*xi[j])

        new.append(p)
    return new


def write_to_file(data, file):
    rows = [line.strip().split(' ') for line in data]
    cols = zip(*rows)
    col_widths = [max(len(value) for value in col) for col in cols]
    format = ' '.join(['%%%ds' % width for width in col_widths])
    for row in rows:
        file.write(format % tuple(row))
        file.write("\n")
