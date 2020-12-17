from abc import ABC, abstractmethod
from Matrix import *


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
        # how many times has the function derivative been called
        self._called_derivative = 0
        # how many times has the hessian matrix been calculated
        self._called_hessian = 0
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

    @abstractmethod
    def calculate_first_derivative(self, point):
        """
        Abstract method for the first derivative.
        :param point: Point which will be evaluated
        :return: First derivative
        """
        pass

    @abstractmethod
    def get_hessian_matrix(self, point):
        """
        Abstract method for calculating Hessian Matrix.
        :param point: Point which will be evaluated
        :return: Hessian matrix
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
    def called_derivative(self):
        """
        Property getter.
        :return: How many times has the function been called
        """
        return self._called_derivative

    @property
    def called_hessian(self):
        """
        Property getter.
        :return: How many times has the function been called
        """
        return self._called_hessian


class Function1(Function):
    """
    Class which represents Function1; 100*(x2-x1^2)^2+(1-x1)^2
    """

    def calculate(self, point):
        if tuple(point) in self._calc_values:
            return self._calc_values[tuple(point)]

        self._called += 1
        x, y = point
        res = 100*Decimal(math.pow(Decimal(y) - Decimal(x*x), 2)) + Decimal(math.pow(1 - x, 2))
        self._calc_values[tuple(point)] = res
        return res

    def calculate_first_derivative(self, point):
        x, y = point
        d_x = 2*(200*math.pow(x, 3) - 200*x*y + x - 1)
        d_y = 200*(y-math.pow(x, 2))

        self._called_derivative += 1

        return [d_x, d_y]

    def get_hessian_matrix(self, point):
        x, y = point
        f_xx = 1200*math.pow(x, 2) - y + 2
        f_xy = -400*x
        f_yx = -400*x
        f_yy = 200

        hessian = [[f_xx, f_xy], [f_yx, f_yy]]

        self._called_hessian += 1

        return hessian


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

    def calculate_first_derivative(self, point):
        x, y = point
        d_x = 2 * (x - 4)
        d_y = 8 * (y - 2)

        self._called_derivative += 1

        return [d_x, d_y]

    def get_hessian_matrix(self, point):
        x, y = point
        f_xx = 2
        f_xy = 0
        f_yx = 0
        f_yy = 8

        self._called_hessian += 1

        return [[f_xx, f_yx], [f_xy, f_yy]]


class Function3(Function):
    """
    Function which represents Function3; (x1-2)^2+(x2+3)^2
    """

    def calculate(self, point):
        try:
            coordinates = list(point)
        except TypeError:
            coordinates = [point, 0.0]

        if tuple(coordinates) in self._calc_values:
            return self._calc_values[tuple(coordinates)]

        self._called += 1
        x, y = coordinates
        res = math.pow((x-2), 2) + math.pow((y+3), 2)
        self._calc_values[tuple(coordinates)] = res
        return res

    def calculate_first_derivative(self, point):
        x, y = point
        d_x = 2 * (x - 2)
        d_y = 2 * (y + 3)

        self._called_derivative += 1

        return [d_x, d_y]

    def get_hessian_matrix(self, point):
        x, y = point
        f_xx = 2
        f_xy = 0
        f_yx = 0
        f_yy = 2

        self._called_hessian += 1

        return [[f_xx, f_yx], [f_xy, f_yy]]


class Function4(Function):
    """
    Class which represents Function4; (x1-3)^2+(x2)^2
    """

    def calculate(self, point):
        if tuple(point) in self._calc_values:
            return self._calc_values[tuple(point)]

        self._called += 1
        x, y = point
        res = math.pow((x-3), 2) + math.pow(y, 2)
        self._calc_values[tuple(point)] = res
        return res

    def calculate_first_derivative(self, point):
        x, y = point
        d_x = 2 * (x - 3)
        d_y = 2 * y

        return [d_x, d_y]

    def get_hessian_matrix(self, point):
        x, y = point
        f_xx = 2
        f_xy = 0
        f_yx = 0
        f_yy = 2

        return [[f_xx, f_yx], [f_xy, f_yy]]


class FunctionLambda(Function):
    """
    Class which represents function by lambda used in Gradient descent and Newton-Raphson methods.
    """
    def __init__(self, gradient, function, current):
        super().__init__()
        # gradient
        self._gradient = gradient
        # function by x
        self._function = function
        # current point for the evaluation
        self._current = current

    def calculate(self, point):
        self._called += 1
        try:
            x = copy.deepcopy(point[0])
        except TypeError:
            x = copy.deepcopy(point)
        eval_point = copy.deepcopy(self._current)

        temp = [x*grad for grad in self._gradient]

        return self._function.calculate(tuple([eval_point[i]+temp[i] for i in range(len(temp))]))

    def calculate_first_derivative(self, point):
        pass

    def get_hessian_matrix(self, point):
        pass


class FunctionInnerPoint(Function):
    """
    Class which represents function for the inner point calculation.
    """
    def __init__(self, implicit, t):
        super().__init__()
        # implicit constraints
        self._implicit = implicit
        # transformation parameter
        self._t = t

    def calculate(self, point):
        res = 0
        for constraint in self._implicit:
            val = constraint.calculate_value(point)
            if val < 0:
                res += val

        return res * -1

    def calculate_first_derivative(self, point):
        pass

    def get_hessian_matrix(self, point):
        pass


class FunctionTransform(Function):
    """
    Represents function used in transforming the problem with constraints into no constraints problem.
    """
    def __init__(self, current, function, implicit, t):
        super().__init__()
        # current evaluation point
        self._current = current
        # function
        self._function = function
        # implicit constraints
        self._implicit = implicit
        # transformation parameter
        self._t = t

    def calculate(self, point):
        eval = self._function.calculate(point)
        equation = []
        non_equation = []
        for constraint in self._implicit:
            if constraint.equation:
                equation.append(constraint)
            else:
                non_equation.append(constraint)

        res = Decimal(eval) + Decimal(self.calc_eq(equation, point)) + Decimal(self.calc_non_eq(non_equation, point))

        return res

    def calc_eq(self, equation, point):
        """
        Calculates values of the implicit constraints which are equations.
        :param equation: List of the equation type implicit constraints
        :param point: point which will be evaluated
        """
        sum_equation = 0
        for eq in equation:
            sum_equation += math.pow(eq.check(point), 2)
        sum_equation *= self._t
        return sum_equation

    def calc_non_eq(self, non_equation, point):
        """
        Calculates values of the implicit constraints which are non-equations.
        :param non_equation: List of the non-equation type implicit constraints
        :param point: point which will be evaluated
        """
        sum = 0
        for ne in non_equation:
            val = ne.calculate_value(point)
            if val <= 0:
                return DOUBLE_MAX
            sum += math.log(val)

        sum *= 1/self._t
        sum *= -1

        return sum

    def calculate_first_derivative(self, point):
        pass

    def get_hessian_matrix(self, point):
        pass

    @property
    def current(self):
        """
        Property getter.
        :return: Current point
        """
        return self._current

    @current.setter
    def current(self, value):
        """
        Property setter.
        :param value: Value of the current point
        """
        self._current = value

    @property
    def t(self):
        """
        Property getter.
        :return: The transformation parameter
        """
        return self._t

    @t.setter
    def t(self, t):
        """
        Property setter.
        :param t: The transformation parameter
        """
        self._t = t
