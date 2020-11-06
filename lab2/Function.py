from abc import ABC, abstractmethod
import math
from numpy import identity


class Function(ABC):
    """
    Abstract class which represents a function.
    """

    def __init__(self):
        """
        Initialization method.
        """
        # how many times has the function been called
        self._called = 0
        # dictionary for the calculated values
        self._calc_values = {}

    @abstractmethod
    def calculate(self, point):
        """
        Abstract method for the function evaluation.
        :param point: Point which will be evaluated
        :return: Evaluation
        """
        pass

    @property
    def called(self):
        """
        Property getter.
        :return: How many times has the function been called
        """
        return self._called


class Function1(Function):
    """
    Class which represents Function1; 100*(x2-x1^2)^2+(1-x1)^2
    """

    def calculate(self, point):

        try:
            coordinates = list(point)
        except TypeError:
            coordinates = []
            coordinates[0] = point
            coordinates[1] = 0.0

        if tuple(coordinates) in self._calc_values:
            return self._calc_values[tuple(coordinates)]

        res = 100*math.pow(coordinates[1] - math.pow(coordinates[0], 2), 2) + math.pow(1 - coordinates[0], 2)
        self._called += 1
        self._calc_values[tuple(coordinates)] = res
        return res


class Function2(Function):
    """
    Class which represents Function2; (x1-4)^2+4*(x2-2)^2
    """

    def calculate(self, point):
        if tuple(point) in self._calc_values:
            return self._calc_values[tuple(point)]

        self._called += 1
        x, y = point
        res = math.pow((x-4), 2) + 4*math.pow((y-2), 2)
        self._calc_values[tuple(point)] = res
        return res


class Function3(Function):
    """
    Function which represents Function3; sum(xi-i)^2
    """

    def calculate(self, point):
        try:
            coordinates = list(point)
        except TypeError:
            coordinates = [point]

        if tuple(coordinates) in self._calc_values:
            return self._calc_values[tuple(coordinates)]

        result = 0.0
        for i in range(len(coordinates)):
            result += math.pow((coordinates[i]-3), 2)

        self._called += 1
        self._calc_values[tuple(coordinates)] = result
        return result


class Function4(Function):
    """
    Class which represents Function4;
    """

    def calculate(self, point):
        if tuple(point) in self._calc_values:
            return self._calc_values[tuple(point)]

        self._called += 1
        x, y = point
        res = math.fabs((x-y)*(x+y)) + math.sqrt(x*x + y*y)
        self._calc_values[tuple(point)] = res
        return res


class Function6(Function):
    """
    Function which represents Function6
    """

    def calculate(self, point):
        try:
            coordinates = list(point)
        except TypeError:
            coordinates = [point]

        if tuple(coordinates) in self._calc_values:
            return self._calc_values[tuple(coordinates)]

        res = 0.0
        for i in range(len(coordinates)):
            res += math.pow((coordinates[i]), 2)

        final = 0.5 + (math.pow(math.sin(math.sqrt(res)), 2) - 0.5) / math.pow(1 + 0.001 * res, 2)
        self._called += 1
        self._calc_values[tuple(coordinates)] = final
        return final


class CoordinateFunction(Function):
    """
    Function which is used in the Coordinate search algorithm.
    """

    def __init__(self, func, x0, row):
        """
        Init method.
        :param func: Initial function which will evaluate the point
        :param x0: Point for the evaluation
        :param row: wanted row of the unit matrix
        """
        super().__init__()
        self._func = func
        self._x0 = x0
        self._row = row

    def calculate(self, point):
        self._called += 1
        unit = identity(len(list(self._x0)))
        transformed = []

        try:
            p = point[0]
        except TypeError:
            p = point

        for i in range(len(list(self._x0))):
            transformed.append((unit[self._row][i]*p) + self._x0[i])

        return self._func.calculate(tuple(transformed))
