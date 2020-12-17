class ExplicitConstraint:
    """
    Class which represents behaviour of an explicit constraint.
    """

    def __init__(self, lower, upper):
        """
        Initialization method.
        """
        # lower constraint boundary
        self._lower = lower
        # upper constraint boundary
        self._upper = upper

    def check(self, point):
        """
        Abstract method for the constraint evaluation.
        :param point: Point which will be evaluated
        :return: Evaluation
        """
        x, y = point

        if x > self._upper or x < self._lower or y > self._upper or y < self._lower:
            return False

        return True

    @property
    def lower(self):
        """
        Property getter.
        :return: Lower boundary
        """
        return self._lower

    @property
    def upper(self):
        """
        Property getter.
        :return: Upper boundary
        """
        return self._upper

