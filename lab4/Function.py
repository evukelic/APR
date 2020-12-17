from abc import ABC, abstractmethod
import math
from decimal import Decimal


class Function(ABC):
    """
    Abstract class which represents a function.
    """

    def __init__(self, dimension):
        """
        Initialization method.
        """
        self._dimension = dimension
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

    @property
    def dimension(self):
        """
        Property getter.
        :return: How many times has the function been called
        """
        return self._dimension


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

        res = Decimal(100*Decimal(math.pow(Decimal(coordinates[1]) - Decimal(math.pow(coordinates[0], 2)), 2)) + Decimal(math.pow(1 - coordinates[0], 2)))

        self._called += 1
        self._calc_values[tuple(coordinates)] = res
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


class Function6(Function):
    """
    Function which represents Schaffer's Function6
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


class Function7(Function):
    """
    Function which represents almost Schaffer's Function7
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

        final = math.pow(res, 0.25) * (1 + math.pow(math.sin(50 * math.pow(res, 0.1)), 2))
        self._called += 1
        self._calc_values[tuple(coordinates)] = final
        return final


class FitnessFunction(Function):
    """
    Function which represents fitness function.
    """
    def __init__(self, function):
        super().__init__(function.dimension)
        self._func = function

    # point is chromosome
    def calculate(self, point):

        return self._func.calculate(point)

