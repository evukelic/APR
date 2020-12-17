from EvolutionaryAlgorithm import *
from Mutation import *
from Crossover import *
from ExplicitConstraint import *
from Function import *
from Constants import *
import statistics

### TASK 1 ###

# Function 1 - Floating point
# file1_1f = open("results/Task1/FloatingPoint/task1_1f.txt", "w")
# file1_1f.write('Crossover: Heuristic Crossover\nMutation: Uniform Mutation\n\n')
# evolutionary_algorithm(100, 3, 0.5, UniformFloatingPointMutation(), HeuristicFloatingPointCrossover(), ExplicitConstraint(-50, 150), 1000000, Function1(2), file1_1f)
# file1_1f.write('\n\nCrossover: Arithmetic Crossover\nMutation: Uniform Mutation\n\n')
# evolutionary_algorithm(100, 3, 0.5, UniformFloatingPointMutation(), ArithmeticFloatingPointCrossover(), ExplicitConstraint(-50, 150), 1000000, Function1(2), file1_1f)

# Function 1 - Binary
# file1_1b = open("results/Task1/Binary/task1_1b.txt", "w")
# file1_1b.write('Crossover: One Point Crossover\nMutation: Uniform Mutation\n\n')
# evolutionary_algorithm(100, 3, 0.5, UniformBinaryMutation(), OnePointBinaryCrossover(), ExplicitConstraint(-50, 150), 1000000, Function1(2), file1_1b, True, 3)
# file1_1b.write('\n\nCrossover: Uniform Crossover\nMutation: Uniform Mutation\n\n')
# evolutionary_algorithm(100, 3, 0.5, UniformBinaryMutation(), UniformBinaryCrossover(), ExplicitConstraint(-50, 150), 1000000, Function1(2), file1_1b, True, 3)

# Function 3 - Floating point
# file1_3f = open("results/Task1/FloatingPoint/task1_3f.txt", "w")
# file1_3f.write('Crossover: Heuristic Crossover\nMutation: Uniform Mutation\n\n')
# evolutionary_algorithm(100, 3, 0.5, UniformFloatingPointMutation(), HeuristicFloatingPointCrossover(), ExplicitConstraint(-50, 150), 10000000, Function3(5), file1_3f)
# file1_3f.write('\n\nCrossover: Arithmetic Crossover\nMutation: Uniform Mutation\n\n')
# evolutionary_algorithm(100, 3, 0.5, UniformFloatingPointMutation(), ArithmeticFloatingPointCrossover(), ExplicitConstraint(-50, 150), 10000000, Function3(5), file1_3f)

# Function 3 - Binary
# file1_3b = open("results/Task1/Binary/task1_3b.txt", "w")
# file1_3b.write('Crossover: One Point Crossover\nMutation: Uniform Mutation\n\n')
# evolutionary_algorithm(100, 3, 0.5, UniformBinaryMutation(), OnePointBinaryCrossover(), ExplicitConstraint(-50, 150), 1000000, Function3(5), file1_3b, True, 3)
# file1_3b.write('\n\nCrossover: Uniform Crossover\nMutation: Uniform Mutation\n\n')
# evolutionary_algorithm(100, 3, 0.5, UniformBinaryMutation(), UniformBinaryCrossover(), ExplicitConstraint(-50, 150), 1000000, Function3(5), file1_3b, True, 3)

# Function 6 - Floating point
# file1_6f = open("results/Task1/FloatingPoint/task1_6f.txt", "w")
# file1_6f.write('Crossover: Heuristic Crossover\nMutation: Uniform Mutation\n\n')
# evolutionary_algorithm(100, 3, 0.5, UniformFloatingPointMutation(), HeuristicFloatingPointCrossover(), ExplicitConstraint(-50, 150), 1000000, Function6(2), file1_6f)
# file1_6f.write('\n\nCrossover: Arithmetic Crossover\nMutation: Uniform Mutation\n\n')
# evolutionary_algorithm(100, 3, 0.5, UniformFloatingPointMutation(), ArithmeticFloatingPointCrossover(), ExplicitConstraint(-50, 150), 1000000, Function6(2), file1_6f)

# Function 6 - Binary
# file1_6b = open("results/Task1/Binary/task1_6b.txt", "w")
# file1_6b.write('Crossover: One Point Crossover\nMutation: Uniform Mutation\n\n')
# evolutionary_algorithm(100, 3, 0.5, UniformBinaryMutation(), OnePointBinaryCrossover(), ExplicitConstraint(-50, 150), 1000000, Function6(2), file1_6b, True, 3)
# file1_6b.write('\n\nCrossover: Uniform Crossover\nMutation: Uniform Mutation\n\n')
# evolutionary_algorithm(100, 3, 0.5, UniformBinaryMutation(), UniformBinaryCrossover(), ExplicitConstraint(-50, 150), 1000000, Function6(2), file1_6b, True, 3)

# Function 7 - Floating point
# file1_7f = open("results/Task1/FloatingPoint/task1_7f.txt", "w")
# file1_7f.write('Crossover: Heuristic Crossover\nMutation: Uniform Mutation\n\n')
# evolutionary_algorithm(100, 3, 0.5, UniformFloatingPointMutation(), HeuristicFloatingPointCrossover(), ExplicitConstraint(-50, 150), 1000000, Function7(2), file1_7f)
# file1_7f.write('\n\nCrossover: Arithmetic Crossover\nMutation: Uniform Mutation\n\n')
# evolutionary_algorithm(100, 3, 0.5, UniformFloatingPointMutation(), ArithmeticFloatingPointCrossover(), ExplicitConstraint(-50, 150), 1000000, Function7(2), file1_7f)

# Function 7 - Binary
# file1_7b = open("results/Task1/Binary/task1_7b.txt", "w")
# file1_7b.write('Crossover: One Point Crossover\nMutation: Uniform Mutation\n\n')
# evolutionary_algorithm(100, 3, 0.5, UniformBinaryMutation(), OnePointBinaryCrossover(), ExplicitConstraint(-50, 150), 1000000, Function7(2), file1_7b, True, 3)
# file1_7b.write('\n\nCrossover: Uniform Crossover\nMutation: Uniform Mutation\n\n')
# evolutionary_algorithm(100, 3, 0.5, UniformBinaryMutation(), UniformBinaryCrossover(), ExplicitConstraint(-50, 150), 1000000, Function7(2), file1_7b, True, 3)


### TASK 2 ###


# file2_6 = open("results/Task2/task2_6.txt", "w")
# file2_6.write('\n\nCrossover: Arithmetic Crossover\nMutation: Uniform Mutation\n\nDimension: 1\n\n')
# evolutionary_algorithm(100, 3, 0.4, UniformFloatingPointMutation(), ArithmeticFloatingPointCrossover(), ExplicitConstraint(-50, 150), 1000000, Function6(1), file2_6)
# file2_6.write('\n\nCrossover: Arithmetic Crossover\nMutation: Uniform Mutation\n\nDimension: 3\n\n')
# evolutionary_algorithm(100, 3, 0.4, UniformFloatingPointMutation(), ArithmeticFloatingPointCrossover(), ExplicitConstraint(-50, 150), 1000000, Function6(3), file2_6)
# file2_6.write('\n\nCrossover: Arithmetic Crossover\nMutation: Uniform Mutation\n\nDimension: 6\n\n')
# evolutionary_algorithm(100, 3, 0.4, UniformFloatingPointMutation(), ArithmeticFloatingPointCrossover(), ExplicitConstraint(-50, 150), 1000000, Function6(6), file2_6)
# file2_6.write('\n\nCrossover: Arithmetic Crossover\nMutation: Uniform Mutation\n\nDimension: 10\n\n')
# evolutionary_algorithm(100, 3, 0.4, UniformFloatingPointMutation(), ArithmeticFloatingPointCrossover(), ExplicitConstraint(-50, 150), 1000000, Function6(10), file2_6)

# file2_7 = open("results/Task2/task2_7.txt", "w")
# file2_7.write('\n\nCrossover: Arithmetic Crossover\nMutation: Uniform Mutation\n\nDimension: 1\n\n')
# evolutionary_algorithm(1000, 3, 0.4, UniformFloatingPointMutation(), ArithmeticFloatingPointCrossover(), ExplicitConstraint(-50, 150), 1000000, Function7(1), file2_7)
# file2_7.write('\n\nCrossover: Arithmetic Crossover\nMutation: Uniform Mutation\n\nDimension: 3\n\n')
# evolutionary_algorithm(30, 3, 0.05, UniformFloatingPointMutation(), ArithmeticFloatingPointCrossover(), ExplicitConstraint(-50, 150), 1000000, Function7(3), file2_7)
# file2_7.write('\n\nCrossover: Arithmetic Crossover\nMutation: Uniform Mutation\n\nDimension: 6\n\n')
# evolutionary_algorithm(30, 3, 0.05, UniformFloatingPointMutation(), ArithmeticFloatingPointCrossover(), ExplicitConstraint(-50, 150), 1000000, Function7(6), file2_7)
# file2_7.write('\n\nCrossover: Arithmetic Crossover\nMutation: Uniform Mutation\n\nDimension: 10\n\n')
# evolutionary_algorithm(30, 3, 0.05, UniformFloatingPointMutation(), ArithmeticFloatingPointCrossover(), ExplicitConstraint(-50, 150), 1000000, Function7(10), file2_7)


### TASK 3 ###


# file3 = open("results/Task3/task3_analytics.txt", "w")
# file3_6b = open("results/Task3/task3_6.txt", "w")
# file3_7b = open("results/Task3/task3_7.txt", "w")

#file3_6f = open("results/Task3/task3_6f.txt", "w")
#file3_7f = open("results/Task3/task3_7f.txt", "w")

# f6b_dim3_optimums_found = 0
# f6b_dim6_optimums_found = 0
# f7b_dim3_optimums_found = 0
# f7b_dim6_optimums_found = 0
#
# f6f_dim3_optimums_found = 0
# f6f_dim6_optimums_found = 0
# f7f_dim3_optimums_found = 0
# f7f_dim6_optimums_found = 0
#
# median_6b_dim3 = []
# median_6b_dim6 = []
# median_6f_dim3 = []
# median_6f_dim6 = []
#
# median_7b_dim3 = []
# median_7b_dim6 = []
# median_7f_dim3 = []
# median_7f_dim6 = []

# for iteration in range(ITERATIONS):
#     file3_6b.write('\n\nCrossover: Uniform Crossover\nMutation: Uniform Mutation\n\nDimension: 3\n\n')
#     res6_3b, evaluation6_3b = evolutionary_algorithm(100, 3, 0.4, UniformBinaryMutation(), UniformBinaryCrossover(), ExplicitConstraint(-50, 150), 100000, Function6(3), file3_6b, True, 4)
#     if res6_3b == 0:
#         f6b_dim3_optimums_found += 1
#     median_6b_dim3.append(evaluation6_3b)
#     file3_6b.write('\n\nCrossover: Uniform Crossover\nMutation: Uniform Mutation\n\nDimension: 6\n\n')
#     res6_6b, evaluation6_6b = evolutionary_algorithm(100, 3, 0.4, UniformBinaryMutation(), UniformBinaryCrossover(), ExplicitConstraint(-50, 150), 100000, Function6(6), file3_6b, True, 4)
#     if res6_6b == 0:
#         f6b_dim6_optimums_found += 1
#     median_6b_dim6.append(evaluation6_6b)

    # file3_6f.write('\n\nCrossover: Arithmetic Crossover\nMutation: Uniform Mutation\n\nDimension: 3\n\n')
    # res6_3f, evaluation6_3f = evolutionary_algorithm(100, 3, 0.4, UniformFloatingPointMutation(), ArithmeticFloatingPointCrossover(), ExplicitConstraint(-50, 150), 100000, Function6(3), file3_6f)
    # if res6_3f == 0:
    #     f6f_dim3_optimums_found += 1
    # median_6f_dim3.append(evaluation6_3f)
    # file3_6f.write('\n\nCrossover: Arithmetic Crossover\nMutation: Uniform Mutation\n\nDimension: 6\n\n')
    # res6_6f, evaluation6_6f = evolutionary_algorithm(100, 3, 0.4, UniformFloatingPointMutation(), ArithmeticFloatingPointCrossover(), ExplicitConstraint(-50, 150), 100000, Function6(6), file3_6f)
    # if res6_6f == 0:
    #     f6f_dim6_optimums_found += 1
    # median_6f_dim6.append(evaluation6_6f)

    # file3_7b.write('\n\nCrossover: Uniform Crossover\nMutation: Uniform Mutation\n\nDimension: 3\n\n')
    # res7_3b, evaluation7_3b = evolutionary_algorithm(100, 3, 0.4, UniformBinaryMutation(), UniformBinaryCrossover(), ExplicitConstraint(-50, 150), 100000, Function7(3), file3_7b, True, 4)
    # if res7_3b == 0:
    #     f7b_dim3_optimums_found += 1
    # median_7b_dim3.append(evaluation7_3b)
    # file3_7b.write('\n\nCrossover: Uniform Crossover\nMutation: Uniform Mutation\n\nDimension: 6\n\n')
    # res7_6b, evaluation7_6b = evolutionary_algorithm(100, 3, 0.4, UniformBinaryMutation(), UniformBinaryCrossover(), ExplicitConstraint(-50, 150), 100000, Function7(6), file3_7b, True, 4)
    # if res7_6b == 0:
    #     f7b_dim6_optimums_found += 1
    # median_7b_dim6.append(evaluation7_6b)

    # file3_7f.write('\n\nCrossover: Uniform Crossover\nMutation: Uniform Mutation\n\nDimension: 3\n\n')
    # res7_3f, evaluation7_3f = evolutionary_algorithm(100, 3, 0.4, UniformFloatingPointMutation(), ArithmeticFloatingPointCrossover(), ExplicitConstraint(-50, 150), 100000, Function7(3), file3_7f)
    # if res7_3f == 0:
    #     f7f_dim3_optimums_found += 1
    # median_7f_dim3.append(evaluation7_3f)
    # file3_7f.write('\n\nCrossover: Uniform Crossover\nMutation: Uniform Mutation\n\nDimension: 6\n\n')
    # res7_6f, evaluation7_6f = evolutionary_algorithm(100, 3, 0.4, UniformFloatingPointMutation(), ArithmeticFloatingPointCrossover(), ExplicitConstraint(-50, 150), 100000, Function7(6), file3_7f)
    # if res7_6f == 0:
    #     f7f_dim6_optimums_found += 1
    # median_7f_dim6.append(evaluation7_6f)


# file3.write('### Task 3 Analytics ###')
# file3.write('\n\n### Function 6 - FLOATING POINT ###')
# file3.write('\n### DIMENSION: 3 ###')
# file3.write('\nNumber of found optimums: ' + str(f6f_dim3_optimums_found))
# file3.write('\nMedian: ' + str(statistics.median(median_6f_dim3)))
#
# file3.write('\n\n### DIMENSION: 6 ###')
# file3.write('\nNumber of found optimums: ' + str(f6f_dim6_optimums_found))
# file3.write('\nMedian: ' + str(statistics.median(median_6f_dim6)))

# file3.write('\n\n### Function 6 - BINARY ###')
# file3.write('\n### DIMENSION: 3 ###')
# file3.write('\nNumber of found optimums: ' + str(f6b_dim3_optimums_found))
# file3.write('\nMedian: ' + str(statistics.median(median_6b_dim3)))
#
# file3.write('\n\n### DIMENSION: 6 ###')
# file3.write('\nNumber of found optimums: ' + str(f6b_dim6_optimums_found))
# file3.write('\nMedian: ' + str(statistics.median(median_6b_dim6)))

# file3.write('\n\n\n### Function 7 - FLOATING POINT ###')
# file3.write('\n### DIMENSION: 3 ###')
# file3.write('\nNumber of found optimums: ' + str(f7f_dim3_optimums_found))
# file3.write('\nMedian: ' + str(statistics.median(median_7f_dim3)))
#
# file3.write('\n\n### DIMENSION: 6 ###')
# file3.write('\nNumber of found optimums: ' + str(f7f_dim6_optimums_found))
# file3.write('\nMedian: ' + str(statistics.median(median_7f_dim6)))

# file3.write('\n\n### Function 7 - BINARY ###')
# file3.write('\n### DIMENSION: 3 ###')
# file3.write('\nNumber of found optimums: ' + str(f7b_dim3_optimums_found))
# file3.write('\nMedian: ' + str(statistics.median(median_7b_dim3)))
#
# file3.write('\n\n### DIMENSION: 6 ###')
# file3.write('\nNumber of found optimums: ' + str(f7b_dim6_optimums_found))
# file3.write('\nMedian: ' + str(statistics.median(median_7b_dim6)))


### TASK 4 ###

# file4 = open("results/Task4/task4.txt", "w")
# file4_6f = open("results/Task4/task4_6f.txt", "w")
# file4.write('### Function 6 parameters optimisation ###')
# file4.write('\nCrossover: Arithmetic crossover')
# file4.write('\nMutation: Uniform mutation')
# file4.write('\nAlgorithm run: 10 times')
#
# mutation_probability_list = [0.1, 0.3, 0.6, 0.9]
# population_size_list = [30, 50, 100, 200]
#
# median_a = []
# median_b = []
# median_c = []
# median_d = []
# for i in range(ITERATIONS):
#     res6_3fa, evaluation6_3fa = evolutionary_algorithm(100, 3, 0.1, UniformFloatingPointMutation(),
#                                                      HeuristicFloatingPointCrossover(), ExplicitConstraint(-50, 150),
#                                                      100000, Function6(2), file4_6f)
#     median_a.append(evaluation6_3fa)
#     file4_6f.write('\n\n')
#     res6_3fb, evaluation6_3fb = evolutionary_algorithm(100, 3, 0.3, UniformFloatingPointMutation(),
#                                                      HeuristicFloatingPointCrossover(), ExplicitConstraint(-50, 150),
#                                                      100000, Function6(2), file4_6f)
#     median_b.append(evaluation6_3fb)
#     file4_6f.write('\n\n')
#     res6_3fc, evaluation6_3fc = evolutionary_algorithm(100, 3, 0.6, UniformFloatingPointMutation(),
#                                                      HeuristicFloatingPointCrossover(), ExplicitConstraint(-50, 150),
#                                                      100000, Function6(2), file4_6f)
#     median_c.append(evaluation6_3fc)
#     file4_6f.write('\n\n')
#     res6_3fd, evaluation6_3fd = evolutionary_algorithm(100, 3, 0.9, UniformFloatingPointMutation(),
#                                                      HeuristicFloatingPointCrossover(), ExplicitConstraint(-50, 150),
#                                                      100000, Function6(2), file4_6f)
#     median_d.append(evaluation6_3fd)
#     file4_6f.write('\n\n')
#
# file4.write('\n\n### Mutation probability optimisation ###')
# file4.write('\nProbability: 0.1')
# calc_median_a = statistics.median(median_a)
# file4.write('\nMedian: ' + str(calc_median_a))
#
# file4.write('\n\nProbability: 0.3')
# calc_median_b = statistics.median(median_b)
# file4.write('\nMedian: ' + str(calc_median_b))
#
# file4.write('\n\nProbability: 0.6')
# calc_median_c = statistics.median(median_c)
# file4.write('\nMedian: ' + str(calc_median_c))
#
# file4.write('\n\nProbability: 0.9')
# calc_median_d = statistics.median(median_d)
# file4.write('\nMedian: ' + str(calc_median_d))
#
# median_list = [calc_median_a, calc_median_b, calc_median_c, calc_median_d]
# file4.write('\n\nBest Mutation Probability Median is: ' + str(min(median_list)))
#
# median_a = []
# median_b = []
# median_c = []
# median_d = []
# median_list = []
# for i in range(ITERATIONS):
#     res6_3fa, evaluation6_3fa = evolutionary_algorithm(30, 3, 0.1, UniformFloatingPointMutation(),
#                                                      HeuristicFloatingPointCrossover(), ExplicitConstraint(-50, 150),
#                                                      100000, Function6(2), file4_6f)
#     median_a.append(evaluation6_3fa)
#     file4_6f.write('\n\n')
#     res6_3fb, evaluation6_3fb = evolutionary_algorithm(50, 3, 0.1, UniformFloatingPointMutation(),
#                                                      HeuristicFloatingPointCrossover(), ExplicitConstraint(-50, 150),
#                                                      100000, Function6(2), file4_6f)
#     median_b.append(evaluation6_3fb)
#     file4_6f.write('\n\n')
#     res6_3fc, evaluation6_3fc = evolutionary_algorithm(100, 3, 0.1, UniformFloatingPointMutation(),
#                                                      HeuristicFloatingPointCrossover(), ExplicitConstraint(-50, 150),
#                                                      100000, Function6(2), file4_6f)
#     median_c.append(evaluation6_3fc)
#     file4_6f.write('\n\n')
#     res6_3fd, evaluation6_3fd = evolutionary_algorithm(200, 3, 0.1, UniformFloatingPointMutation(),
#                                                      HeuristicFloatingPointCrossover(), ExplicitConstraint(-50, 150),
#                                                      100000, Function6(2), file4_6f)
#     median_d.append(evaluation6_3fd)
#     file4_6f.write('\n\n')
#
# file4.write('\n\n### Population size optimisation ###')
# file4.write('\nPopulation: 30')
# calc_median_a = statistics.median(median_a)
# file4.write('\nMedian: ' + str(calc_median_a))
#
# file4.write('\n\nPopulation: 50')
# calc_median_b = statistics.median(median_b)
# file4.write('\nMedian: ' + str(calc_median_b))
#
# file4.write('\n\nPopulation: 100')
# calc_median_c = statistics.median(median_c)
# file4.write('\nMedian: ' + str(calc_median_c))
#
# file4.write('\n\nPopulation: 200')
# calc_median_d = statistics.median(median_d)
# file4.write('\nMedian: ' + str(calc_median_d))
#
# median_list = [calc_median_a, calc_median_b, calc_median_c, calc_median_d]
# file4.write('\n\nBest Population Size Median is: ' + str(min(median_list)))

### TASK 5 ###
# file5 = open("results/Task5/task5_6f.txt", "w")
# file5_analytics = open("results/Task5/task5.txt", "w")
# file5.write('\n\nCrossover: Arithmetic Crossover\nMutation: Uniform Mutation\n')
#
# res1 = []
# res2 = []
# res3 = []
# for i in range(ITERATIONS):
#     r1, e1 = evolutionary_algorithm(100, 3, 0.4, UniformFloatingPointMutation(), ArithmeticFloatingPointCrossover(), ExplicitConstraint(-50, 150), 1000000, Function6(2), file5)
#     res1.append(e1)
#     file5.write('\n')
#
#     r2, e2 = evolutionary_algorithm(100, 4, 0.4, UniformFloatingPointMutation(), ArithmeticFloatingPointCrossover(), ExplicitConstraint(-50, 150), 1000000, Function6(2), file5)
#     res2.append(e2)
#     file5.write('\n')
#
#     r3, e3 = evolutionary_algorithm(100, 5, 0.4, UniformFloatingPointMutation(), ArithmeticFloatingPointCrossover(), ExplicitConstraint(-50, 150), 1000000, Function6(2), file5)
#     res3.append(e3)
#
# file5_analytics.write('\n### Tournament size: 3 \n')
# file5_analytics.write('Optimum median: ' + str(statistics.median(res1)))
# file5_analytics.write('\n\n### Tournament size: 4 \n')
# file5_analytics.write('Optimum median: ' + str(statistics.median(res2)))
# file5_analytics.write('\n\n### Tournament size: 5 \n')
# file5_analytics.write('Optimum median: ' + str(statistics.median(res3)))

