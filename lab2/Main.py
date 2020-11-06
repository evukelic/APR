from OptimisationMethods import *
from Function import *
from random import uniform

"""
Tasks which will test out the behaviour of the optimisation methods.
"""

file1_a = open("results/task1_a.txt", "w")
file1_b = open("results/task1_b.txt", "w")
file1_c = open("results/task1_c.txt", "w")

points = [10, 100, 1000]
files = [file1_a, file1_b, file1_c]

# task1
print("### Task 1: ###")

for point, file in list(zip(points, files)):
    print('\nPoint: ' + str(point))
    file.write("### GOLDEN RATIO ###\n")
    func1 = Function3()
    print("### GOLDEN RATIO ###")
    res = golden_ratio(func1, False, 1, point, file)
    print("Minimum: " + "{:.2f}".format(res))
    print("Number of evaluations: " + str(func1.called))
    print("\n")

    func1 = Function3()
    print("### COORDINATE SEARCH ###")
    res = coordinate_search(point, func1)
    print("Minimum: " + "{:.2f}".format(res[0]))
    print("Number of evaluations: " + str(func1.called))
    print("\n")

    file.write("\n\n### NELDER-MEAD ###\n")
    func1 = Function3()
    print("### NELDER-MEAD ###")
    res = nelder_mead(point, 1, func1, file)
    print("Minimum: " + "{:.2f}".format(res[0]))
    print("Number of evaluations: " + str(func1.called))
    print("\n")

    file.write("\n\n### HOOKE-JEEVES ###\n")
    func1 = Function3()
    print("### HOOKE-JEEVES ###")
    res = hooke_jeeves(point, func1, file)
    print("Minimum: " + "{:.2f}".format(res[0]))
    print("Number of evaluations: " + str(func1.called))


# task2
file2 = open("results/task2.txt", "w")

print("\n\nTask 2:\n")
print('Nelder-Mead                       Hooke-Jeeves                       Coordinate Search')
print('-------------------------------------------------------------------------------------------------------')
point1 = (-1.9, 2)
func1 = Function1()
res1_a = nelder_mead(point1, 1, func1, file2)
tup1 = ' '.join(format(f, '.2f') for f in res1_a)
call1 = func1.called
func1 = Function1()
res1_b = hooke_jeeves(point1, func1, file2)
tup2 = ' '.join(format(f, '.2f') for f in res1_b)
call2 = func1.called
func1 = Function1()
res1_c = coordinate_search(point1, func1)
tup3 = ' '.join(format(f, '.2f') for f in res1_c)
call3 = func1.called
print(tup1 + ', ' + str(call1) + '                    ' + tup2 + ', ' + str(call2) + '                     ' + tup3 + ', ' + str(call3))
print('-------------------------------------------------------------------------------------------------------')
point2 = (0.1, 0.3)
func2 = Function2()
res2_a = nelder_mead(point2, 1, func2, file2)
tup1 = ' '.join(format(f, '.2f') for f in res2_a)
call1 = func2.called
func2 = Function2()
res2_b = hooke_jeeves(point2, func2, file2)
tup2 = ' '.join(format(f, '.2f') for f in res2_b)
call2 = func2.called
func2 = Function2()
res2_c = coordinate_search(point2, func2)
tup3 = ' '.join(format(f, '.2f') for f in res2_c)
call3 = func2.called
print(tup1 + ', ' + str(call1) + '                     ' + tup2 + ', ' + str(call2) + '                     ' + tup3 + ', ' + str(call3))
print('-------------------------------------------------------------------------------------------------------')
point3 = (0,0,0,0,0)
func3 = Function3()
res3_a = nelder_mead(point3, 1, func3, file2)
tup1 = ' '.join(format(f, '.2f') for f in res3_a)
call1 = func3.called
func3 = Function3()
res3_b = hooke_jeeves(point3, func3, file2)
tup2 = ' '.join(format(f, '.2f') for f in res3_b)
call2 = func3.called
func3 = Function3()
res3_c = coordinate_search(point3, func3)
tup3 = ' '.join(format(f, '.2f') for f in res3_c)
call3 = func3.called
print(tup1 + ', ' + str(call1) + '     ' + tup2 + ', ' + str(call2) + '      ' + tup3 + ', ' + str(call3))
print('-------------------------------------------------------------------------------------------------------')
point4 = (5.1, 1.1)
func4 = Function4()
res3_a = nelder_mead(point4, 1, func4, file2)
tup1 = ' '.join(format(f, '.2f') for f in res3_a)
call1 = func4.called
func4 = Function4()
res3_b = hooke_jeeves(point4, func4, file2)
tup2 = ' '.join(format(f, '.2f') for f in res3_b)
call2 = func4.called
func4 = Function4()
res3_c = coordinate_search(point4, func4)
tup3 = ' '.join(format(f, '.2f') for f in res3_c)
call3 = func4.called
print(tup1 + ', ' + str(call1) + '                   ' + tup2 + ', ' + str(call2) + '                     ' + tup3 + ', ' + str(call3))
print('-------------------------------------------------------------------------------------------------------')

# task3
file3 = open("results/task3.txt", "w")

print("\n\nTask 3:\n")
print('Nelder-Mead                       Hooke-Jeeves')
print('-----------------------------------------------------------------')
point = (5, 5)
func = Function4()
res3_a = nelder_mead(point, 1, func, file3)
tup1 = ' '.join(format(f, '.2f') for f in res3_a)
call1 = func.called
func = Function4()
res3_b = hooke_jeeves(point, func, file3)
tup2 = ' '.join(format(f, '.2f') for f in res3_b)
call2 = func.called
print(tup1 + ', ' + str(call1) + '                    ' + tup2 + ', ' + str(call2))
print('------------------------------------------------------------------')

# task4
file4 = open("results/task4.txt", "w")

print("\n\nTask 4:\n")
print('Nelder-Mead, (0.5, 0.5)')
print('---------------------------------')
point_1 = (0.5, 0.5)
for i in range(20):
    func = Function1()
    res4_a = nelder_mead(point_1, i+1, func, file4)
    tup1 = ' '.join(format(f, '.2f') for f in res4_a)
    call1 = func.called
    print(tup1 + ', ' + str(call1))
print('---------------------------------\n')

print('Nelder-Mead, (20, 20)')
print('---------------------------------')
point_1 = (20, 20)
for i in range(20):
    func = Function1()
    res4_a = nelder_mead(point_1, i+1, func, file4)
    tup1 = ' '.join(format(f, '.2f') for f in res4_a)
    call1 = func.called
    print(tup1 + ', ' + str(call1))
print('---------------------------------')

# task5
file5 = open("results/task5.txt", "w")

print("\n\nTask 5:\n")
optimums = 0
for i in range(1000):
    lower = uniform(-50, 50)
    upper = uniform(-50, 50)
    if lower < upper:
        point = (lower, upper)
    else:
        point = (upper, lower)

    func6 = Function6()
    res = hooke_jeeves(point, func6, file5)
    print('Point: ' + str(point) + ', Minimum: ' + ' '.join(format(f, '.2f') for f in res))
    if math.fabs(func6.calculate(res)) < 0.0001:
        optimums += 1
print('\nOptimums found: ' + str(optimums))
