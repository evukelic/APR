from abc import ABC, abstractmethod
from Matrix import *
from Constants import *
import math


class NumericIntegration(ABC):
    """
    Abstract class NumericIntegration represent one numeric integration method.
    """
    def __init__(self, A, B, X0, r, T, t_max, i_print):
        """
        Initialization method.
        :param A: matrix A
        :param B: matrix B
        :param X0: matrix X0
        :param r: impulse
        :param T: period
        :param t_max: time interval boundary
        :param i_print: after how many iterations would it be printed out
        """
        self._A = A
        self._B = B
        self._X0 = X0
        self._r = r
        self._T = T
        self._t_max = t_max
        self._i_print = i_print

    @abstractmethod
    def calculate_next(self, xk, tk):
        """
        Abstract method for calculating the value in the next time period.
        :param xk: value in the current time period
        :param tk: current time period
        :return: wanted value
        """
        pass

    @abstractmethod
    def prediction(self, xk, tk):
        """
        Abstract method for the prediction.
        :param xk: value in the current time period
        :param tk: current time period
        :return: wanted value
        """
        pass

    @abstractmethod
    def correction(self, xk, tk, next_x):
        """
        Abstract method for the correction.
        :param xk: value in the current time period
        :param tk: current time period
        :param next_x: value in the next time period
        :return: wanted value
        """
        pass

    def make_r_matrix(self, t):
        """
        Method which makes the matrix out of the given impulse.
        :param t: time period
        :return: wanted matrix
        """
        R = Matrix()
        R.init_matrix(len(self._r), 1)

        for i in range(len(self._r)):
            R.set(i, 0, self._r[i].calculate(t))

        return R

    def print_solution(self, file, err=False):
        """
        Method which prints one row of the solution into the given file.
        :param file: file in which the solution will be written
        """
        i = 1
        tK = self._T
        xK = self._X0
        data = [HEADER]
        error = 0.0
        while True:
            if tK >= self._t_max:
                break
            next = self.calculate_next(xK, tK)
            if err:
                x1 = self._X0.get(0, 0) * math.cos(tK) + self._X0.get(1, 0) * math.sin(tK)
                x2 = self._X0.get(1, 0) * math.cos(tK) - self._X0.get(0, 0) * math.sin(tK)
                error += math.fabs(x1 - next.get(0, 0)) + math.fabs(x2 - next.get(1, 0))
            if i % self._i_print == 0:
                line = '  '.join(("{:.6f}".format(tK), "|", "{:.6f}".format(xK.data[0][0]), "{:.6f}".format(xK.data[1][0]), "|", "{:.6f}".format(next.data[0][0]), "{:.6f}".format(next.data[1][0])))
                data.append(line)
            tK += self._T
            xK = next
            i += 1

        write_to_file(data, file)
        if err:
            error_line = 'ERROR: ' + str(error)
            file.write(error_line)


class Euler(NumericIntegration):
    """
    Class Euler represents Euler's numeric integration method.
    """
    def __init__(self, A, B, X0, r, T, t_max, i_print):
        super().__init__(A, B, X0, r, T, t_max, i_print)
        # M matrix
        self._M = self.calculate_M()
        # N matrix
        self._N = self.calculate_N()

    def calculate_M(self):
        """
        Method for calculating the M matrix.
        :return: M matrix
        """
        unit = self._A.get_unit_matrix()
        A_copy = copy.deepcopy(self._A)
        A_copy.multiply_by_scalar(self._T)
        unit.operate(Operation.ADD, A_copy)
        return unit

    def calculate_N(self):
        """
        Method for calculating the N matrix.
        :return: N matrix
        """
        if self._B is not None:
            B_copy = copy.deepcopy(self._B)
            B_copy.multiply_by_scalar(self._T)
            return B_copy
        return None

    def calculate_next(self, xk, tk):
        next = self._M.multiply(self._M, xk)

        if self._N is not None:
            R = self.make_r_matrix(tk)
            temp = self._N.multiply(self._N, R)
            next.operate(Operation.ADD, temp)

        return next

    def prediction(self, xk, tk):
        return self.calculate_next(xk, tk)

    def correction(self, xk, tk, next_x):
        pass


class ReversedEuler(NumericIntegration):
    """
    Class ReversedEuler represents reversed Euler's numeric integration method.
    """
    def __init__(self, A, B, X0, r, T, t_max, i_print):
        super().__init__(A, B, X0, r, T, t_max, i_print)
        # P matrix
        self._P = self.calculate_P()
        # Q matrix
        self._Q = self.calculate_Q()

    def calculate_P(self):
        """
        Method for calculating the P matrix.
        :return: P matrix
        """
        unit = self._A.get_unit_matrix()
        A_copy = copy.deepcopy(self._A)
        A_copy.multiply_by_scalar(self._T)
        unit.operate(Operation.SUBTRACT, A_copy)
        return unit.inverse_matrix()

    def calculate_Q(self):
        """
        Method for calculating the Q matrix.
        :return: Q matrix
        """
        if self._B is not None:
            P_copy = copy.deepcopy(self._P)
            P_copy.multiply_by_scalar(self._T)
            return P_copy.multiply(P_copy, self._B)
        return None

    def calculate_next(self, xK, tK):
        next = self._P.multiply(self._P, xK)

        if self._Q is not None:
            tK_next = tK + self._T
            R = self.make_r_matrix(tK_next)
            Qr = self._Q.multiply(self._Q, R)
            next.operate(Operation.ADD, Qr)

        return next

    def prediction(self, xk, tk):
        pass

    def correction(self, xk, tk, next_x):
        nextAx = self._A.multiply(self._A, next_x)

        if self._B is not None:
            tkNext = tk + self._T
            R = self.make_r_matrix(tkNext)
            Br = self._B.multiply(self._B, R)
            nextAx.operate(Operation.ADD, Br)

        nextAx.multiply_by_scalar(self._T)
        nextAx.operate(Operation.ADD, xk)
        return nextAx


class Trapezoid(NumericIntegration):
    """
    Class Trapezoid represents trapezoid numeric integration method.
    """
    def __init__(self, A, B, X0, r, T, t_max, i_print):
        super().__init__(A, B, X0, r, T, t_max, i_print)
        # R matrix
        self._R = self.calculate_R()
        # helper R1 matrix
        self._R1 = self.calculate_R(True)
        # S matrix
        self._S = self.calculate_S()

    def calculate_R(self, r1=False):
        """
        Method for calculating R matrix.
        :return: R matrix
        """
        unit = self._A.get_unit_matrix()
        A_copy = copy.deepcopy(self._A)
        A_copy.multiply_by_scalar(self._T*0.5)
        unit_copy = copy.deepcopy(unit)
        unit.operate(Operation.SUBTRACT, A_copy)
        first = unit.inverse_matrix()

        unit_copy.operate(Operation.ADD, A_copy)

        if r1:
            temp = copy.deepcopy(first)
            return temp

        return first.multiply(first, unit_copy)

    def calculate_S(self):
        """
        Method for calculating S matrix.
        :return: S matrix
        """
        if self._B is not None:
            self._R1.multiply_by_scalar(self._T * 0.5)
            return self._R1.multiply(self._R1, self._B)
        return None

    def calculate_next(self, xk, tk):
        next_res = self._R.multiply(self._R, xk)

        if self._S is not None:
            next_tK = tk + self._T

            current = self.make_r_matrix(tk)
            next = self.make_r_matrix(next_tK)

            current.operate(Operation.ADD, next)
            Sr = self._S.multiply(self._S, current)
            next_res.operate(Operation.ADD, Sr)

        return next_res

    def prediction(self, xk, tk):
        pass

    def correction(self, xk, tk, next_x):
        temp = self._A.multiply(self._A, xk)
        temp2 = self._A.multiply(self._A, next_x)

        if self._B is not None:
            t_next = tk + self._T
            R = self.make_r_matrix(tk)
            R_next = self.make_r_matrix(t_next)
            Br = self._B.multiply(self._B, R)
            Br_next = self._B.multiply(self._B, R_next)

            temp.operate(Operation.ADD, Br)
            temp2.operate(Operation.ADD, Br_next)

        temp.operate(Operation.ADD, temp2)
        temp.multiply_by_scalar(0.5 * self._T)
        temp.operate(Operation.ADD, xk)

        return temp

    @property
    def R1(self):
        return self._R1

    @R1.setter
    def R1(self, r1):
        self._R1 = r1


class RungeKutta(NumericIntegration):
    """
    Class RungeKutta represents Runge-Kutta numeric integration method.
    """
    def __init__(self, A, B, X0, r, T, t_max, i_print):
        super().__init__(A, B, X0, r, T, t_max, i_print)

    def calculate_next(self, xk, tk):
        first = self._A.multiply(self._A, xk)

        if self._B is not None:
            R = self.make_r_matrix(tk)
            temp = self._B.multiply(self._B, R)
            first.operate(Operation.ADD, temp)

        first_copy = copy.deepcopy(first)
        first_copy.multiply_by_scalar(0.5 * self._T)
        x_copy = copy.deepcopy(xk)
        x_copy.operate(Operation.ADD, first_copy)
        second = self._A.multiply(self._A, x_copy)
        if self._B is not None:
            R = self.make_r_matrix(tk + 0.5*self._T)
            temp = self._B.multiply(self._B, R)
            second.operate(Operation.ADD, temp)

        second_copy = copy.deepcopy(second)
        second_copy.multiply_by_scalar(0.5 * self._T)
        x_copy = copy.deepcopy(xk)
        x_copy.operate(Operation.ADD, second_copy)
        third = self._A.multiply(self._A, x_copy)
        if self._B is not None:
            R = self.make_r_matrix(tk + 0.5 * self._T)
            temp = self._B.multiply(self._B, R)
            third.operate(Operation.ADD, temp)

        third_copy = copy.deepcopy(third)
        third_copy.multiply_by_scalar(self._T)
        x_copy = copy.deepcopy(xk)
        x_copy.operate(Operation.ADD, third_copy)
        fourth = self._A.multiply(self._A, x_copy)
        if self._B is not None:
            R = self.make_r_matrix(tk + self._T)
            temp = self._B.multiply(self._B, R)
            fourth.operate(Operation.ADD, temp)

        second.multiply_by_scalar(2)
        third.multiply_by_scalar(2)
        first.operate(Operation.ADD, second)
        first.operate(Operation.ADD, third)
        first.operate(Operation.ADD, fourth)

        first.multiply_by_scalar(self._T/6)
        xk_copy = copy.deepcopy(xk)
        xk_copy.operate(Operation.ADD, first)

        return xk_copy

    def prediction(self, xk, tk):
        pass

    def correction(self, xk, tk, next_x):
        pass


class PECE2(NumericIntegration):
    """
    Class PECE2 represents Predictor-Corrector numeric integration method where the predictor is
    Euler's method and corrector Reversed Euler's method.
    """
    def __init__(self, A, B, X0, r, T, t_max, i_print, s):
        super().__init__(A, B, X0, r, T, t_max, i_print)
        # number of iterations
        self._s = s
        # predictor
        self._predictor = self.get_predictor()
        # corrector
        self._corrector = self.get_corrector()

    def get_predictor(self):
        """
        Method which initializes the predictor.
        :return: the predictor
        """
        A_copy = copy.deepcopy(self._A)
        predictor = Euler(A_copy, self._B, self._X0, self._r, self._T, self._t_max, self._i_print)
        return predictor

    def get_corrector(self):
        """
        Method which initializes the corrector.
        :return: the corrector
        """
        A_copy = copy.deepcopy(self._A)
        corrector = ReversedEuler(A_copy, self._B, self._X0, self._r, self._T, self._t_max, self._i_print)
        return corrector

    def calculate_next(self, xk, tk):
        next = self._predictor.prediction(xk, tk)

        for i in range(self._s):
            next = self._corrector.correction(xk, tk, next)

        return next

    def prediction(self, xk, tk):
        pass

    def correction(self, xk, tk, next_x):
        pass


class PECE(NumericIntegration):
    """
    Class PECE represents Predictor-Corrector numeric integration method where the predictor is
    Euler's method and corrector Trapezoid method.
    """
    def __init__(self, A, B, X0, r, T, t_max, i_print, s):
        super().__init__(A, B, X0, r, T, t_max, i_print)
        # number of iterations
        self._s = s
        # predictor
        self._predictor = self.get_predictor()
        # corrector
        self._corrector = self.get_corrector()

    def get_predictor(self):
        """
        Method which initializes the predictor.
        :return: the predictor
        """
        A_copy = copy.deepcopy(self._A)
        predictor = Euler(A_copy, self._B, self._X0, self._r, self._T, self._t_max, self._i_print)
        return predictor

    def get_corrector(self):
        """
        Method which initializes the corrector.
        :return: the corrector
        """
        A_copy = copy.deepcopy(self._A)
        corrector = Trapezoid(A_copy, self._B, self._X0, self._r, self._T, self._t_max, self._i_print)
        return corrector

    def calculate_next(self, xk, tk):
        next = self._predictor.prediction(xk, tk)

        for i in range(self._s):
            next = self._corrector.correction(xk, tk, next)

        return next

    def prediction(self, xk, tk):
        pass

    def correction(self, xk, tk, next_x):
        pass
