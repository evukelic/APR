from Helper import *


class Chromosome:
    """
    Abstract class which represents a chromosome.
    """

    def __init__(self, data, fitness):
        """
        Initialization method.
        :param data: chromosome data
        :param fitness: fitness function
        """
        self._data = data
        self._fitness = fitness
        self._length = None

    def set_element(self, value, index):
        """
        Sets the element at the given index.
        :param value: value for the insertion
        :param index: index of the insertion
        """
        self._data[index] = value

    def get_data(self):
        """
        Gets the chromosome data.
        :return: chromosome data
        """
        return self._data

    @property
    def data(self):
        """
        Property getter.
        :return: chromosome data
        """
        return self._data

    @property
    def length(self):
        """
        Property getter.
        :return: chromosome length
        """
        return self._length

    @property
    def fitness(self):
        """
        Property getter.
        :return: the fitness function
        """
        return self._fitness

    @fitness.setter
    def fitness(self, fitness):
        """
        Property setter.
        :param fitness: fitness function
        """
        self._fitness = fitness


class BinaryChromosome(Chromosome):
    """
    Class BinaryChromosome represents a binary chromosome.
    """

    def __init__(self, constraint, n, data, fitness, real_data, precision):
        """
        Initialization method.
        """
        # how many times has the function been called
        # dictionary for the calculated values
        super().__init__(data, fitness)
        self._upper = constraint.upper
        self._constraint = constraint
        self._lower = constraint.lower
        self._length = n
        # data as binary string
        self._data = data
        # data as real numbers
        self._real_data = real_data
        self._precision = precision

    def get_data(self):
        """
        Gets the chromosome data.
        :return: chromosome data
        """
        return self._real_data

    @property
    def length(self):
        """
        Property getter.
        :return: length of the chromosome
        """
        return self._length

    @property
    def real_data(self):
        """
        Property getter.
        :return: chromosome real data
        """
        return self._real_data

    @property
    def constraint(self):
        """
        Property getter.
        :return: explicit constraint
        """
        return self._constraint

    @property
    def precision(self):
        """
        Property getter.
        :return: the precision
        """
        return self._precision

    @property
    def fitness(self):
        """
        Property getter.
        :return: the fitness function
        """
        return self._fitness

    @fitness.setter
    def fitness(self, fitness):
        """
        Property setter.
        :param fitness: the fitness function
        """
        self._fitness = fitness

