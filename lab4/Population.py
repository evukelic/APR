from abc import ABC, abstractmethod
from Chromosome import *


class Population(ABC):
    """
    Abstract class Population represents one chromosome units population.
    """

    def __init__(self, size, dim, constraint, fitness, precision=None):
        """
        Initialization method.
        :param size: size of the population
        :param dim: dimension of the data
        :param constraint: explicit constraint
        :param fitness: fitness function
        :param precision: data precision
        """
        self._size = size
        self._dimension = dim
        self._constraint = constraint
        # upper boundary
        self._upper = constraint.upper
        # lower boundary
        self._lower = constraint.lower
        self._function = fitness
        self._precision = precision
        # generate population data
        self._chromosome_data = self.generate_data(precision)

    def set_chromosome_data(self, element, index):
        """
        Sets the chromosome data at the given index.
        :param element: Element which will be set
        :param index: index on which the element will be set
        """
        # calculate the fitness for the element
        try:
            fitness = self._function.calculate(element.data)
        except TypeError:
            fitness = self._function.calculate(element.real_data)
        element.fitness = fitness
        self._chromosome_data[index] = element

    def get_chromosome(self, index):
        """
        Gets the chromosome data at the given index.
        :param index: Index of the wanted element
        :return: the wanted element
        """
        return self._chromosome_data[index]

    def get_best_chromosome(self, index=False):
        """
        Gets either the best chromosome in the population or the index of the best chromosome.
        :param index: False if the unit itself is wanted, True otherwise
        :return: best unit or index of the best unit
        """
        best_index = 0
        cnt = 0
        best_fitness = self._chromosome_data[0].fitness

        for chromosome in self._chromosome_data:
            fitness = chromosome.fitness
            if fitness < best_fitness:
                best_fitness = fitness
                best_index = cnt
            cnt += 1

        if index:
            return best_index

        return self._chromosome_data[best_index]

    def get_worst_index(self, tournament):
        """
        Gets the index of the worst chromosome in the tournament selection.
        :param tournament: the tournament
        :return: index of the worst unit
        """
        worst = 0
        worst_fitness = 0
        first_iteration = True
        for i in tournament:
            current = self._chromosome_data[i].fitness
            if first_iteration or current > worst_fitness:
                worst_fitness = current
                worst = i
                first_iteration = False
        return worst

    @abstractmethod
    def generate_data(self, precision):
        """
        Abstract method which generates population data.
        :param precision: precision of the data
        :return: the chromosome population
        """
        pass

    @property
    def size(self):
        """
        Property getter.
        :return: the population size
        """
        return self._size

    @property
    def dimension(self):
        """
        Property getter.
        :return: the data dimension
        """
        return self._dimension

    @property
    def constraint(self):
        """
        Property getter.
        :return: explicit constraint
        """
        return self._constraint

    @property
    def upper(self):
        """
        Property getter.
        :return: upper boundary of the constraint
        """
        return self._upper

    @property
    def lower(self):
        """
        Property getter.
        :return: lower boundary of the constraint
        """
        return self._lower

    @property
    def fitness_function(self):
        """
        Property getter.
        :return: the fitness function
        """
        return self._function

    @property
    def chromosome_data(self):
        """
        Property getter.
        :return: the population data
        """
        return self._chromosome_data


class FloatingPointPopulation(Population):
    """
    Class FloatingPointPopulation represents population of the floating point display type.
    """

    def generate_data(self, precision):
        """
        Generates floating point population data.
        :param precision: precision of the data
        :return: the chromosome population
        """
        data = []
        for i in range(self.size):
            element_data = []

            for j in range(self.dimension):
                element_data.append(random.uniform(self.lower, self.upper))

            fitness = self.fitness_function.calculate(element_data)
            chromosome = Chromosome(element_data, fitness)
            data.append(chromosome)

        return data


class BinaryPopulation(Population):
    """
    Class BinaryPopulation represents population of the binary display type.
    """

    def __init__(self, size, dim, constraint, fitness, precision):
        """
        Initialization method.
        :param size: size of the population
        :param dim: dimension of the data
        :param constraint: explicit constraint
        :param fitness: fitness function
        :param precision: data precision
        """
        super(BinaryPopulation, self).__init__(size, dim, constraint, fitness, precision)

    def calculate_length(self, precision):
        """
        Calculates the length of the binary based on the precision.
        :param precision: predefined precision
        :return: length
        """
        return math.ceil(math.log(math.floor(1+(self.upper - self.lower) * math.pow(10, self._precision)))
                         / math.log(2))

    def generate_data(self, precision):
        """
        Generates binary population data.
        :param precision: precision of the data
        :return: the chromosome population
        """
        length = self.calculate_length(precision)
        factor = math.pow(2, length)
        data = []

        for i in range(self.size):
            element_data = []

            for j in range(self.dimension):
                rebounded_data = int(random.random() * factor - 1)
                element_data.append(rebounded_data)

            real_data = [convert_binary(data, self.upper, self.lower, length, False) for data in element_data]
            fitness = self.fitness_function.calculate(real_data)

            element_data = [str(bin(data))[2:].zfill(length) for data in element_data]
            chromosome = BinaryChromosome(self.constraint, length, element_data, None, real_data, length)
            chromosome.fitness = fitness

            data.append(chromosome)

        return data
