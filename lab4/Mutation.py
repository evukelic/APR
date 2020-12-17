from abc import ABC, abstractmethod
import random


class Mutation(ABC):
    """
    Abstract class Mutation represents one Mutation operation.
    """

    @abstractmethod
    def mutate(self, chromosome, probability, constraint):
        """
        Abstract method which represents mutation operation.
        :param chromosome: Chromosome which will be mutated
        :param probability: Probability which determines would there be mutation or not
        :param constraint: Explicit constraint
        """
        pass


class UniformBinaryMutation(Mutation):
    """
    Class which represents Uniform Binary Mutation.
    """

    def mutate(self, chromosome, probability, constraint):
        """
        Method which mutates the chromosome for certain probability.
        :param chromosome: Chromosome which will be mutated
        :param probability: Probability which determines would there be mutation or not
        :param constraint: Explicit constraint
        """
        for i in range(len(chromosome.data)):
            if random.random() <= probability:
                mutation_result = ''
                for j in range(len(chromosome.data[i])):
                    if random.random() <= probability:
                        if chromosome.data[i][j] == '0':
                            mutation_result += '1'
                        else:
                            mutation_result += '0'
                    else:
                        mutation_result += chromosome.data[i][j]

                chromosome.set_element(mutation_result, i)


class UniformFloatingPointMutation(Mutation):
    """
    Class which represents Uniform Floating Point Mutation.
    """

    def mutate(self, chromosome, probability, constraint):
        """
        Method which mutates the chromosome for certain probability.
        :param chromosome: Chromosome which will be mutated
        :param probability: Probability which determines would there be mutation or not
        :param constraint: Explicit constraint
        """
        for i in range(len(chromosome.data)):
            if random.random() <= probability:
                chromosome.set_element(random.uniform(constraint.lower, constraint.upper), i)
