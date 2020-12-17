import copy
from Constants import *
from decimal import *
import numpy as np
import random

"""
Static helper methods.
"""


def unimodal(h, point, function):
    """
    Finds unimodal interval of the function for the given point.
    :param h: The shift
    :param point: Point for which the interval has been searched
    :param function: Function for which interval has been searched
    :return: Unimodal interval
    """
    try:
        p = point[0]
    except TypeError:
        p = point
    m = copy.deepcopy(p)
    left = p - h
    right = p + h
    step = 1

    fm = function.calculate(tuple(get_list(point)))
    fl = function.calculate(left)
    fr = function.calculate(right)

    if fm < fr and fm < fl:
        return left, right

    elif fm > fr:
        while True:
            left = copy.deepcopy(m)
            m = right
            step = step*2
            fm = copy.deepcopy(fr)
            right = p + h*step
            fr = function.calculate(right)
            if fm < fr:
                break
    else:
        while True:
            right = copy.deepcopy(m)
            m = left
            fm = copy.deepcopy(fl)
            step = step*2
            left = p - h*step
            fl = function.calculate(left)
            if fm < fl:
                break
    return left, right


# def nelder_mead(x0, move, function):
#     """
#     Nelder-Mead algorithm.
#     :param x0: Starting point
#     :param move: Move for starting simplex
#     :param function: Function
#     :return: Minimum
#     """
#     points = simplex(x0, move)
#     try:
#         n = len(list(x0))
#     except TypeError:
#         n = 1
#     while True:
#         l = minmax_index(points, function)
#         h = minmax_index(points, function, False)
#         xc = centroid(points, h, n)
#
#         xr = rec(xc, points[h], ALPHA)
#         fxr = function.calculate(xr)
#         fxl = function.calculate(points[l])
#         fxh = function.calculate(points[h])
#         if fxr < fxl:
#             xe = rec(xc, xr, GAMMA)
#             if function.calculate(xe) < fxl:
#                 points[h] = copy.deepcopy(xe)
#             else:
#                 points[h] = copy.deepcopy(xr)
#         else:
#             greatest = True
#             for i in range(len(list(points))):
#                 if i != h:
#                     if fxr < function.calculate(points[i]):
#                         greatest = False
#                         break
#
#             if greatest:
#                 if fxr < fxh:
#                     points[h] = copy.deepcopy(xr)
#                 xk = rec(xc, points[h], BETA)
#                 if function.calculate(xk) < fxh:
#                     points[h] = copy.deepcopy(xk)
#                 else:
#                     points = shrink(points[l], points)
#             else:
#                 points[h] = copy.deepcopy(xr)
#
#         move += 1
#         if should_stop(points, xc, function):
#             return tuple(xc)


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


# def shrink(xl, points):
#     new = []
#     for i in range(len(list(points))):
#         xi = points[i]
#         p = []
#         for j in range(len(list(xl))):
#             p.append(xl[j]*(1-SIGMA)-SIGMA*xi[j])
#
#         new.append(p)
#     return new


def golden_ratio(function, h=None, point=None, interval=False):
    """
    Method which finds minimum of a function for the given interval or point.
    :param write: Should write the result into the file
    :param file: File in which will result be written
    :param function: Function for which minimum has been searched
    :param interval: Unimodal interval
    :param h: The shift
    :param point: Point for which minimum has been searched
    :return: Golden ratio result
    """
    if not interval:
        interval = unimodal(h, point, function)

    a, b = interval
    c = b - k*(b-a)
    d = a + k*(b-a)
    fc = function.calculate(c)
    fd = function.calculate(d)

    while True:
        # algorithm
        if fc < fd:
            b = copy.deepcopy(d)
            d = copy.deepcopy(c)
            c = b - k*(b-a)
            fd = copy.deepcopy(fc)
            fc = function.calculate(c)
        else:
            a = copy.deepcopy(c)
            c = copy.deepcopy(d)
            d = a + k*(b-a)
            fc = copy.deepcopy(fd)
            fd = function.calculate(d)

        if (b-a) < EPSILON:
            break

    return (a+b)/2


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

    cent = [c/(len(list(points))-1) for c in cent]

    return cent


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


def get_h2(points, function, h):
    """
    Finds the index of the second greatest evaluated point.
    :param points: List of the points
    :param function: Evaluating function
    :param h: Index of the greatest evaluated point
    :return: h2 index
    """
    max_val = 0
    max_set = False

    for i in range(len(points)):
        if i != h:
            val = function.calculate(tuple(points[i]))
            if not max_set or val > max_val:
                max_val = val
                h2 = i
                max_set = True

    return h2


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
        res += Decimal(math.pow((Decimal(function.calculate(points[i]))-Decimal(function.calculate(xc))), 2))

    val = math.sqrt(res/len(list(points)))
    return val <= EPSILON


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


def hooke_jeeves(x0, function):
    """
    Hooke-Jeeves algorithm.
    :param x0: Initial point
    :param function: Function which will be minimized
    :return: Minimum of the function
    """
    xp = x0
    xb = x0
    delta = dx

    while True:
        xn = search(xp, delta, function)
        temp = xn
        fxn = function.calculate(xn)
        fxb = function.calculate(xb)

        if fxn < fxb:
            try:
                xp = [a*2 - b for a, b in zip(xn, xb)]
            except TypeError:
                xp = xn[0]*2 - xb
            xn = temp
            xb = xn
        else:
            delta = delta/2.0
            xp = xb

        if delta < EPSILON:
            break

    return xb


def should_transformation_stop(before, current):
    """
    Stop condition for the transformation problem.
    :param before: Point before the transformation
    :param current: After the transformation
    :return:
    """
    for i in range(len(before)):
        res = math.fabs(before[i]-current[i])
        if res >= EPSILON:
            return False
    return True


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


def random_point(lower, upper, n):
    """
    Function which returns the random point from the given interval.
    :param lower: Lower interval boundary
    :param upper: Upper interval boundary
    :param n: Dimension of the point
    :return: Randomised point
    """
    point = []
    for i in range(n):
        rand = random.random()
        value = lower+rand*(upper-lower)
        point.append(value)

    return point
