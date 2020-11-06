from Helper import *

"""
Optimisation algorithms.
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


def golden_ratio(function, interval=False, h=None, point=None, file=None, write=True):
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
    data = [GOLDEN_RATIO_HEADER]
    while True:
        # write to file
        fa = function.calculate(a)
        fb = function.calculate(b)
        line = '  '.join(("{:.6f}".format(a), "{:.6f}".format(c), "{:.6f}".format(d), "{:.6f}".format(b),
                          "|",
                          "{:.6f}".format(fa), "{:.6f}".format(fc), "{:.6f}".format(fd), "{:.6f}".format(fb)))
        data.append(line)

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

    if write:
        write_to_file(data, file)
    return (a+b)/2


def hooke_jeeves(x0, function, file):
    """
    Hooke-Jeeves algorithm.
    :param file: File in which the result will be written
    :param x0: Initial point
    :param function: Function which will be minimized
    :return: Minimum of the function
    """
    xp = x0
    xb = x0
    delta = dx
    data = [HOOKE_JEEVES_HEADER]
    while True:
        xn = search(xp, delta, function)
        temp = xn
        fxn = function.calculate(xn)
        fxb = function.calculate(xb)
        fxp = function.calculate(xp)

        # write to file
        try:
            xb_ = xb[0]
        except TypeError:
            xb_ = xb
        try:
            xn_ = xn[0]
        except TypeError:
            xn_ = xn
        try:
            xp_ = xp[0]
        except TypeError:
            xp_ = xp
        line = '  '.join(("{:.6f}".format(xb_), "{:.6f}".format(xp_), "{:.6f}".format(xn_),
                          "|",
                          "{:.6f}".format(fxb), "{:.6f}".format(fxp), "{:.6f}".format(fxn)))
        data.append(line)
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
            write_to_file(data, file)
            break

    return xb


def nelder_mead(x0, move, function, file):
    """
    Nelder-Mead algorithm.
    :param file: File in which the result will be written
    :param x0: Starting point
    :param move: Move for starting simplex
    :param function: Function
    :return: Minimum
    """
    points = simplex(x0, move)
    data = [NELDER_MEAD_HEADER]
    try:
        n = len(list(x0))
    except TypeError:
        n = 1
    while True:
        l = minmax_index(points, function)
        h = minmax_index(points, function, False)
        xc = centroid(points, h, n)

        xr = rec(xc, points[h], ALPHA)
        fxr = function.calculate(xr)
        fxl = function.calculate(points[l])
        fxh = function.calculate(points[h])
        if fxr < fxl:
            xe = rec(xc, xr, GAMMA)
            if function.calculate(xe) < fxl:
                points[h] = copy.deepcopy(xe)
            else:
                points[h] = copy.deepcopy(xr)
        else:
            greatest = True
            for i in range(len(list(points))):
                if i != h:
                    if fxr < function.calculate(points[i]):
                        greatest = False
                        break

            if greatest:
                if fxr < fxh:
                    points[h] = copy.deepcopy(xr)
                xk = rec(xc, points[h], BETA)
                if function.calculate(xk) < fxh:
                    points[h] = copy.deepcopy(xk)
                else:
                    points = shrink(points[l], points)
            else:
                points[h] = copy.deepcopy(xr)

        # write to file
        fxc = function.calculate(xc)
        line = '  '.join(("{:.6f}".format(xc[0]), "|", "{:.6f}".format(fxc)))
        data.append(line)
        move += 1
        if should_stop(points, xc, function):
            write_to_file(data, file)
            return tuple(xc)


def coordinate_search(x0, function):
    """
    Coordinate search algorithm.
    :param x0: Starting point
    :param function: Function
    :return: Minimum
    """
    try:
        list(x0)
    except TypeError:
        x0 = [x0]
    x = list(copy.deepcopy(x0))
    while True:
        xs = copy.deepcopy(x)
        for i in range(len(list(x0))):
            func = CoordinateFunction(function, copy.deepcopy(x), i)
            point = []
            for d in range(len(list(x0))):
                point.append(0.0)
            point[i] = copy.deepcopy(x[i])
            lam = golden_ratio(func, False, 1, point, write=False)
            x[i] = lam + x[i]
        norm = 0
        for j in range(len(list(x0))):
            norm += math.pow(xs[j]-x[j], 2)
        if math.sqrt(norm) < EPSILON:
            break
    return x
