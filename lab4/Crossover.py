from abc import ABC, abstractmethod
from Chromosome import *
from Helper import *


class Crossover(ABC):
    """
    Abstract class Crossover represents one chromosome crossover operation.
    """
    def __init__(self):
        """
        Initialization method.
        """
        # The first parent
        self._first_chromosome = None
        # The second parent
        self._second_chromosome = None

    @abstractmethod
    def do_crossover(self, first, second):
        """
        Abstract method which represents crossover operation.
        :param first: the first parent
        :param second: the second parent
        :return: result of the crossover
        """
        pass

    @property
    def first_chromosome(self):
        """
        Property getter.
        :return: first parent chromosome
        """
        return self._first_chromosome

    @property
    def second_chromosome(self):
        """
        Property getter.
        :return: second parent chromosome
        """
        return self._second_chromosome


class ArithmeticFloatingPointCrossover(Crossover):
    """
    Class which represents Arithmetic Floating Point Crossover.
    """
    def do_crossover(self, first, second):
        """
        Crossover operation function.
        :param first: the first parent chromosome
        :param second: the second parent chromosome
        :return: crossover result chromosome
        """
        elements = []
        for i in range(len(first.data)):
            a = random.random()
            crossover_result = a*first.data[i] + (1 - a)*second.data[i]
            elements.append(crossover_result)

        return Chromosome(elements, first.fitness)


class HeuristicFloatingPointCrossover(Crossover):
    """
    Class which represents Heuristic Floating Point Crossover.
    """
    def do_crossover(self, first, second):
        """
        Crossover operation function.
        :param first: the first parent chromosome
        :param second: the second parent chromosome
        :return: crossover result chromosome
        """
        elements = []

        if first.fitness < second.fitness:
            x1 = first
            x2 = second
        else:
            x1 = second
            x2 = first

        for i in range(len(first.data)):
            a = random.random()
            crossover_result = a*(x2.data[i] - x1.data[i]) + x2.data[i]
            elements.append(crossover_result)

        return Chromosome(elements, first.fitness)


class OnePointBinaryCrossover(Crossover):
    """
    Class which represents One-Point Binary Crossover.
    """
    def do_crossover(self, first, second):
        """
        Crossover operation function.
        :param first: the first parent chromosome
        :param second: the second parent chromosome
        :return: crossover result chromosome
        """
        elements = []
        for i in range(len(first.data)):
            breakpoint_index = random.randint(0, first.length)
            crossover_result = ""
            # if index is 0, the result is the second parent
            if breakpoint_index == 0:
                elements.append(second.data[i])
            # if index is length, the result is the first parent
            elif breakpoint_index == first.length:
                elements.append(first.data[i])
            # else, divide by breakpoint
            else:
                for j in range(first.length):
                    if j < breakpoint_index:
                        crossover_result += first.data[i][j]
                    else:
                        crossover_result += second.data[i][j]
                elements.append(crossover_result)

        real_data = [convert_binary(int(data, 2), first.constraint.upper, first.constraint.lower, first.precision, False) for data in elements]

        return BinaryChromosome(first.constraint, first.length, elements, first.fitness, real_data, first.precision)


class UniformBinaryCrossover(Crossover):
    """
    Class which represents Uniform Binary Crossover.
    """
    def do_crossover(self, first, second):
        """
        Crossover operation function.
        :param first: the first parent chromosome
        :param second: the second parent chromosome
        :return: crossover result chromosome
        """

        elements = []
        for i in range(len(first.data)):
            rand_unit = random_unit_generator(first.length)
            xor_result = xor(first.data[i], second.data[i])
            crossover_result = (int(first.data[i], 2) & int(second.data[i], 2)) | (int(rand_unit, 2) & int(xor_result, 2))
            converted_result = bin(crossover_result)[2:].zfill(first.length)
            elements.append(converted_result)

        real_data = [
            convert_binary(int(data, 2), first.constraint.upper, first.constraint.lower, first.precision, False) for
            data in elements]

        return BinaryChromosome(first.constraint, first.length, elements, first.fitness, real_data, first.precision)