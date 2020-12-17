from abc import ABC, abstractmethod
from Constants import EPSILON
import math


class ImplicitConstraint(ABC):
    """
    Class which represents behaviour of an implicit constraint.
    """

    def __init__(self, equation):
        """
        Initialization method.
        """
        # is the constraint an equation
        self._equation = equation

    @abstractmethod
    def calculate_value(self, point):
        """
        Abstract method for the constraint evaluation.
        :param point: Point which will be evaluated
        :return: Evaluation
        """
        pass

    def check(self, point):
        """
        Method which checks if the point is within the constraint range.
        :param point: Point which will be checked
        :return: True if within the range, False otherwise
        """
        value = self.calculate_value(point)

        if self._equation:
            if math.fabs(value) > EPSILON:
                return False
            return True
        else:
            if value >= 0:
                return True
            return False

    @property
    def equation(self):
        """
        Property getter.
        :return: Is the constraint an equation
        """
        return self._equation


class ImplicitConstraint1(ImplicitConstraint):
    """
    Class which represents implicit constraint x2 - x1 >= 0
    """

    def calculate_value(self, point):
        x, y = point
        res = y - x
        return res


class ImplicitConstraint2(ImplicitConstraint):
    """
    Class which represents implicit constraint 2 - x1 >= 0
    """

    def calculate_value(self, point):
        x, y = point
        res = 2 - x
        return res


class ImplicitConstraint3(ImplicitConstraint):
    """
    Class which represents implicit constraint x2 - 1 >= 0
    """

    def calculate_value(self, point):
        x, y = point
        res = y - 1
        return res


class ImplicitConstraint4(ImplicitConstraint):
    """
    Class which represents implicit constraint 3 - x1 - x2 >= 0
    """

    def calculate_value(self, point):
        x, y = point
        res = 3 - x - y
        return res


class ImplicitConstraint5(ImplicitConstraint):
    """
    Class which represents implicit constraint 3 + 1.5*x1 - x2 >= 0
    """

    def calculate_value(self, point):
        x, y = point
        res = 3 + 1.5*x - y
        return res
