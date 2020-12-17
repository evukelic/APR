from Function import *
from Matrix import *

import random

"""
Optimisation algorithms.
"""


def gradient_descent(point, function, is_golden_section):
    """
    Gradient descent optimisation algorithm.
    :param point: Starting point
    :param function: Function which will be minimised
    :param is_golden_section: Should the golden ratio be used
    :return: Optimisation result
    """
    current = copy.deepcopy(point)
    cnt = 0
    best_eval = function.calculate(current)

    while True:
        gradient = function.calculate_first_derivative(current)

        if is_golden_section:
            _lambda = golden_ratio(FunctionLambda(gradient, function, current), 1, 0)
            move = [_lambda*grad for grad in gradient]
        else:
            move = [grad * -1 for grad in gradient]

        current = tuple([list(current)[i]+move[i] for i in range(len(move))])

        # check the stop condition
        norm = math.sqrt(math.pow(gradient[0], 2) + math.pow(gradient[1], 2))
        if norm < EPSILON:
            break

        # check for the divergence
        current_eval = function.calculate(current)
        if current_eval < best_eval:
            best_eval = current_eval
            cnt = 0
        else:
            cnt += 1
            if cnt == MAX_ITERATIONS:
                print("The method has diverged!")
                return -1

    return current


def newton_raphson(point, function, is_golden_section):
    """
    Newton-Raphson optimisation algorithm.
    :param point: Starting point
    :param function: Function which will be minimised
    :param is_golden_section: Should the golden ratio be used
    :return: Minimisation result
    """
    current = copy.deepcopy(point)
    cnt = 0
    best_eval = function.calculate(current)

    while True:
        gradient = function.calculate_first_derivative(current)
        hessian = function.get_hessian_matrix(current)

        mat = Matrix()
        mat.init_matrix_from_data(np.array(hessian))
        b = Matrix()
        b.init_matrix_from_data(np.array([gradient]).transpose())
        solution_matrix = find_solution(mat, b)
        solution = [val[0] for val in solution_matrix.data]

        if is_golden_section:
            func = FunctionLambda(solution, function, current)
            _lambda = golden_ratio(func, 1, 0)
            move = [val*_lambda for val in solution]
        else:
            move = [grad * -1 for grad in gradient]
        current = tuple([current[i]+move[i] for i in range(len(move))])

        # check the stop condition
        norm = math.sqrt(math.pow(move[0], 2) + math.pow(move[1], 2))
        if norm < EPSILON:
            break

        # check for the divergence
        current_eval = function.calculate(current)
        if current_eval < best_eval:
            best_eval = current_eval
            cnt = 0
        else:
            cnt += 1
            if cnt == MAX_ITERATIONS:
                print("The method has diverged!")
                return -1

    return current


def box_algorithm(point, function, explicit_constraints, implicit_constraints):
    """
    Box optimisation algorithm.
    :param point: Starting point
    :param function: Function which will be minimised
    :param explicit_constraints: List of the explicit constraints
    :param implicit_constraints: List of the implicit constraints
    :return: Result of the minimisation
    """
    for constraint in explicit_constraints:
        res = constraint.check(point)
        if not res:
            raise ValueError()

    for constraint in implicit_constraints:
        res = constraint.check(point)
        if not res:
            raise ValueError()

    x0 = list(copy.deepcopy(point))
    xc = list(copy.deepcopy(x0))
    points = [tuple(x0)]

    cnt = 0
    best_eval = function.calculate(point)
    t = 1
    while True:
        if t >= 2*len(point):
            break

        xt = random_point(explicit_constraints[0].lower, explicit_constraints[0].upper, len(point))
        while True:
            implicit = True

            for constraint in implicit_constraints:
                res = constraint.check(xt)
                if not res:
                    implicit = False
            if not implicit:
                xt[0] = xt[0]+xc[0]
                xt[1] = xt[1]+xc[1]
                xt = [val*0.5 for val in xt]
            else:
                break

        points.append(tuple(xt))
        h = minmax_index(points, function, False)
        xc = centroid(points, h, len(x0))

        t += 1

    while True:
        h = minmax_index(points, function, False)
        h2 = get_h2(points, function, h)

        xc = centroid(points, h, len(x0))
        xr = rec(xc, points[h], ALPHA)

        for i in range(len(x0)):
            xr_i = xr[i]
            if xr_i < explicit_constraints[0].lower:
                xr[i] = explicit_constraints[0].lower
            elif xr_i > explicit_constraints[0].upper:
                xr[i] = explicit_constraints[0].upper

        while True:
            implicit = True

            for constraint in implicit_constraints:
                res = constraint.check(xr)
                if not res:
                    implicit = False
            if not implicit:
                xr[0] = xr[0]+xc[0]
                xr[1] = xr[1]+xc[1]
                xr = [val*0.5 for val in xr]
            else:
                break

        xr_evaluated = function.calculate(xr)
        h2_evaluated = function.calculate(points[h2])
        if xr_evaluated > h2_evaluated:
            xr[0] = xr[0]+xc[0]
            xr[1] = xr[1]+xc[1]
            xr = [val*0.5 for val in xr]

        points[h] = tuple(xr)

        # check the stop condition
        if should_stop(points, xc, function):
            return xc

        # check for the divergence
        current_eval = function.calculate(xc)
        if current_eval < best_eval:
            best_eval = current_eval
            cnt = 0
        else:
            cnt += 1
            if cnt == MAX_ITERATIONS:
                print("The method has diverged!")
                return -1


def no_constraints_transformation(point, function, implicit_constraints):
    """
    Transformation to the no constraints problem followed by Hooke-Jeeves for the new, no-constraints
    problem optimisation.
    :param point: Starting point
    :param function: Function which will be minimized
    :param implicit_constraints: List of the implicit constraints
    :return: Result of the minimisation
    """

    implicit = True
    for constraint in implicit_constraints:
        res = constraint.check(point)
        if not res:
            implicit = False
    if not implicit:
        func = FunctionInnerPoint(implicit_constraints, T)
        point = hooke_jeeves(point, func)

    current = copy.deepcopy(point)
    func = FunctionTransform(current, function, implicit_constraints, T)

    cnt = 0
    best_eval = function.calculate(current)

    while True:
        before_move = copy.deepcopy(current)
        current = hooke_jeeves(current, func)

        # check the stop condition
        if should_transformation_stop(before_move, current):
            break

        # check for the divergence
        current_eval = function.calculate(current)
        if current_eval < best_eval:
            best_eval = current_eval
            cnt = 0
        else:
            cnt += 1
            if cnt == MAX_ITERATIONS:
                print("The method has diverged!")
                return -1

        func.current = current
        func.t = func.t*10

    return current



