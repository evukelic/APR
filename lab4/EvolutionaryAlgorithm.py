from Constants import *
from Function import FitnessFunction
from Population import *


def evolutionary_algorithm(population_size, tournament_size, probability, mutation, crossover, constraint, iterations,
                        function, file, binary=False, precision=None):
    """
    Evolutionary algorithm.
    :param population_size: population size
    :param tournament_size: tournament size
    :param probability: mutation probability
    :param mutation: type of the mutation
    :param crossover: type of the crossover
    :param constraint: explicit constraint
    :param iterations: number of iterations
    :param function: function which needs to be minimized
    :param file: file in which the results will be written
    :param binary: is the display type binary or real
    :param precision: the precision
    """
    # generate fitness function for the given function
    fitness_function = FitnessFunction(function)
    # determine which population needs to be generated
    if binary:
        population = BinaryPopulation(population_size, function.dimension, constraint, fitness_function, precision)
    else:
        population = FloatingPointPopulation(population_size, function.dimension, constraint, fitness_function)

    evaluation = None
    eval_before = None

    for i in range(iterations):
        tournament = get_tournament_members(0, population_size-1, tournament_size)
        worst = population.get_worst_index(tournament)

        chromosomes = []
        for t in tournament:
            if t == worst:
                continue
            chromosomes.append(population.get_chromosome(t))

        crossover_chromosome = crossover.do_crossover(chromosomes[0], chromosomes[1])
        mutation.mutate(crossover_chromosome, probability, constraint)
        population.set_chromosome_data(crossover_chromosome, worst)
        best_chromosome = population.get_best_chromosome()
        evaluation = function.calculate(best_chromosome.get_data())

        if eval_before is None or (evaluation < eval_before and math.fabs(evaluation - eval_before) > EPSILON):
            file.write('Iteration: ' + str(i+1))
            file.write('     Current best unit: ' + str(best_chromosome.data))
            file.write('     Function evaluation: ' + str(evaluation))
            file.write('\n')
            eval_before = evaluation

        if math.fabs(evaluation) < EPSILON:
            file.write('\nOPTIMUM HAS BEEN FOUND!\n\n')
            return 0, evaluation

    return -1, evaluation
