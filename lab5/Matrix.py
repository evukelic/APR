from Constants import EPSILON
from Helper import *
from Operations import Operation
import copy
import numpy as np


class Matrix:
    """
    Class Matrix represents behaviour of a 2D array.
    """
    def __init__(self):
        """
        Default initialization method.
        """
        # first dimension
        self._row = None
        # second dimension
        self._col = None
        # 2d array which will contain the data
        self._data = None
        # is lup decomposition already done
        self._is_lup = False
        # L decomposed matrix
        self._L = None
        # U decomposed matrix
        self._U = None
        # P decomposed matrix
        self._P = None

    def __eq__(self, matrix):
        """
        Overridden equals method.
        :param matrix: Matrix for comparison
        :return: True if equals, false otherwise
        """
        if not isinstance(matrix, Matrix) and self._data.shape == matrix.data.shape:
            return False

        tuples = [(a, b) for a, b in zip(self._data.flatten(), matrix.data.flatten())]
        for a, b in tuples:
            if a != b:
                return False
        return True

    def init_matrix(self, row, col):
        """
        Initialize matrix by dimensions only.
        :param row: First dimension
        :param col: Second dimension
        """
        self._row = row
        self._col = col
        self._data = np.zeros((row, col))

    def init_matrix_from_data(self, data):
        """
        Initialize matrix by data only.
        :param data: 2d array
        """
        self._row, self._col = data.shape
        self._data = data

    def init_matrix_from_file(self, path):
        """
        Initialize matrix from the file.
        :param path: Path to the file
        """
        self._data = np.loadtxt(path, ndmin=2)
        self._row, self._col = self._data.shape

    def operate(self, operation, matrix):
        """
        Addition and subtraction matrix operations.
        :param operation: Type of the operation
        :param matrix: The second operand
        :return: Result of the operation
        """
        if self._data.shape != matrix.data.shape:
            raise ValueError("Invalid matrices dimensions!")

        flattened_first_data = self._data.flatten()
        flattened_second_data = matrix.data.flatten()

        if operation == Operation.ADD:
            self._data = np.array([(a+b) for a, b in zip(flattened_first_data, flattened_second_data)])
        elif operation == Operation.SUBTRACT:
            self._data = np.array([(a-b) for a, b in zip(flattened_first_data, flattened_second_data)])

        self._data = self._data.reshape(self._row, self._col)

    def multiply_by_scalar(self, scalar):
        """
        Multiply by scalar operation.
        :param scalar: The scalar
        :return: Result of the multiplication
        """
        self._data = np.array([(a * scalar) for a in self._data.flatten()]).reshape(self._row, self._col)

    def divide_by_scalar(self, scalar):
        """
        Multiply by scalar operation.
        :param scalar: The scalar
        :return: Result of the multiplication
        """
        if scalar == 0:
            raise ValueError('Invalid scalar, division by zero not possible!')
        self._data = np.array([(a / scalar) for a in self._data.flatten()]).reshape(self._row, self._col)

    def multiply(self, mat1, mat2):
        """
        Multiplication matrix operation.
        :param mat1: The first operand
        :param mat2: The second operand
        :return: Result of the multiplication
        """
        multiplied = Matrix()

        if mat2.row != mat1.col:
            raise ValueError('Invalid dimensions!')

        data = np.array([[sum(a * b for a, b in zip(row, col)) for col in zip(*mat2.data)] for row in mat1.data])
        multiplied.init_matrix_from_data(data)

        return multiplied

    def transpose(self):
        """
        Method for transposing the matrix.
        """
        self._data = np.array([[self._data[j][i] for j in range(self._row)] for i in range(self._col)])

    def is_square(self):
        """
        Method for checking if the matrix is square.
        :return: True if square, false otherwise
        """
        return self._row == self._col

    def get(self, row, col):
        """
        One matrix element getter.
        :param row: Index of the row
        :param col: Index of the column
        :return: The wanted element
        """
        if row < 0 or col < 0 or row > self._row or col > self._col:
            raise IndexError('Invalid dimensions!')

        return self._data[row][col]

    def set(self, row, col, element):
        """
        One matrix element setter.
        :param row: Index of the row
        :param col: Index of the column
        :param element: Element which will be set
        """
        if row < 0 or col < 0 or row > self._row or col > self._col:
            raise IndexError('Invalid dimensions!')

        self._data[row][col] = element

    def lup_decomposition(self, lup=False):
        """
        LU(P) decomposition method.
        :param lup: Is it LUP or LU decomposition
        """
        if not self.is_square():
            raise ValueError('Matrix is not square!')

        if self._is_lup:
            return

        P = Matrix()
        P.init_matrix_from_data(get_unit_data(self._row))

        for i in range(self._row-1):
            if lup:
                index = i
                j = i+1
                while j < self._row:
                    if abs(self.get(j, i)) > abs(self.get(index, i)):
                        index = j
                    j += 1
                P.swap_rows(i, index)
                self.swap_rows(i, index)

            if abs(self.get(i, i)) < EPSILON:
                raise ValueError('Pivot below threshold tolerance!')

            j = i+1

            while j < self._row:
                self.set(j, i, self.get(j, i)/self.get(i, i))
                k = i+1
                while k < self._row:
                    self.set(j, k, self.get(j, k) - (self.get(j, i)*self.get(i, k)))
                    k += 1
                j += 1

        self.divide_matrices(P)

    def divide_matrices(self, P):
        """
        Divide the matrix on L, U and P matrices.
        :param P: Permutation matrix
        """
        L = Matrix()
        U = Matrix()
        L.init_matrix(self._row, self._col)
        U.init_matrix(self._row, self._col)

        for i in range(self._row):
            for j in range(self._row):
                if i == j:
                    L.set(i, j, 1)
                    U.set(i, j, self.get(i, j))
                elif i < j:
                    L.set(i, j, 0)
                    U.set(i, j, self.get(i, j))
                else:
                    L.set(i, j, self.get(i, j))
                    U.set(i, j, 0)

        self._is_lup = True
        self._L = L
        self._U = U
        self._P = P

    def swap_rows(self, index1, index2):
        """
        Method for swapping the rows in the matrix.
        :param index1: Index of the first row
        :param index2: Index of the second row
        """
        tmp = copy.deepcopy(self._data[index1])
        self._data[index1] = self._data[index2]
        self._data[index2] = tmp

    def get_e(self):
        """
        Helper unit matrix used for inverse.
        :return: unit matrix
        """
        unit = Matrix()
        unit.init_matrix_from_data(get_unit_data(self._row))
        e = []
        for i in range(self._row):
            val = Matrix()
            val.init_matrix(self._row, 1)
            for j in range(self._row):
                val.set(j, 0, unit.get(j, i))
            e.append(val)

        return e

    def calculate_determinant(self):
        """
        Method for calculating the determinant of the matrix.
        :return: determinant
        """
        if not self.is_lup:
            self.lup_decomposition(True)
        permutations = count_permutations(self._P)
        det = 1.0

        for i in range(self._row):
            det = det * self._L.get(i, i) * self._U.get(i, i)

        return pow(-1, permutations + 1) * det

    def inverse_matrix(self):
        """
        Inverting the matrix if possible.
        :return: inverse of the matrix
        """
        if not self._is_lup:
            self.lup_decomposition(True)

        # self._L.print()
        # self._U.print()

        solution = []
        e = self.get_e()
        inverse = Matrix()

        for i in range(self._row):
            solution.append(find_solution(self, e[i]))

        inverse.init_matrix(solution[0].row, len(solution))
        for i in range(inverse._row):
            for j in range(inverse._col):
                inverse.set(j, i, solution[i].get(j, 0))

        return inverse

    def get_unit_matrix(self):
        """
        Method gets unit matrix based on the row dimension.
        :return: Unit matrix
        """
        data = get_unit_data(self._row)
        unit = Matrix()
        unit.init_matrix_from_data(data)
        return unit

    def print(self):
        """
        Print the matrix to the stdout.
        """
        print(self._data)

    def write_to_file(self):
        """
        Method for writing the matrices into the file.
        """
        np.savetxt("files/mat2.txt", self._data, delimiter=" ", fmt='%.1f',)

    @property
    def row(self):
        """
        Property getter.
        :return: First dimension
        """
        return self._row

    @property
    def col(self):
        """
        Property getter.
        :return: Second dimension
        """
        return self._col

    @property
    def data(self):
        """
        Property getter.
        :return: The matrix data
        """
        return self._data

    @property
    def is_lup(self):
        """
        Property getter.
        :return: Is lup flag
        """
        return self._is_lup

    @property
    def L(self):
        """
        Property getter.
        :return: L matrix
        """
        return self._L

    @property
    def U(self):
        """
        Property getter.
        :return: U matrix
        """
        return self._U

    @property
    def P(self):
        """
        Property getter.
        :return: P matrix
        """
        return self._P


