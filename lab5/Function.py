from abc import ABC, abstractmethod


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

    @abstractmethod
    def calculate(self, t):
        """
        Abstract method for the function evaluation.
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
    Class which represents Function1;
    """

    def calculate(self, t):

        self._called += 1

        return 1


class Function2(Function):
    """
    Class which represents Function2;
    """

    def calculate(self, t):

        self._called += 1

        return t
