from NumericIntegrations import *
from Matrix import *
from Function import *


### TASK 1 ###
file1 = open("results/task1.txt", "w")

A = Matrix()
A.init_matrix(2, 2)
A.set(0, 0, 0)
A.set(0, 1, 1)
A.set(1, 0, -1)
A.set(1, 1, 0)

X0 = Matrix()
X0.init_matrix(2, 1)
X0.set(0, 0, 1)
X0.set(1, 0, 1)

euler = Euler(A, None, X0, None, 0.01, 10, 100)
file1.write('### EULER ###\n')
euler.print_solution(file1, True)

reversed_euler = ReversedEuler(A, None, X0, None, 0.01, 10, 100)
file1.write('\n\n### REVERSED EULER ###\n')
reversed_euler.print_solution(file1, True)

trapezoid = Trapezoid(A, None, X0, None, 0.01, 10, 100)
file1.write('\n\n### TRAPEZOID ###\n')
trapezoid.print_solution(file1, True)

runge_kutta = RungeKutta(A, None, X0, None, 0.01, 10, 100)
file1.write('\n\n### RUNGE-KUTTA ###\n')
runge_kutta.print_solution(file1, True)

A = Matrix()
A.init_matrix(2, 2)
A.set(0, 0, 0)
A.set(0, 1, 1)
A.set(1, 0, -1)
A.set(1, 1, 0)

X0 = Matrix()
X0.init_matrix(2, 1)
X0.set(0, 0, 1)
X0.set(1, 0, 1)

pece2 = PECE2(A, None, X0, None, 0.01, 10, 100, 2)
file1.write('\n\n### PECE2 ###\n')
pece2.print_solution(file1, True)

pece = PECE(A, None, X0, None, 0.01, 10, 100, 1)
file1.write('\n\n### PECE ###\n')
pece.print_solution(file1, True)


## TASK 2 ###
file2 = open("results/task2.txt", "w")

A = Matrix()
A.init_matrix(2, 2)
A.set(0, 0, 0)
A.set(0, 1, 1)
A.set(1, 0, -200)
A.set(1, 1, -102)

X0 = Matrix()
X0.init_matrix(2, 1)
X0.set(0, 0, 1)
X0.set(1, 0, -2)

euler = Euler(A, None, X0, None, 0.1, 1, 1)
file2.write('### EULER ###\n')
euler.print_solution(file2)

reversed_euler = ReversedEuler(A, None, X0, None, 0.1, 1, 1)
file2.write('\n\n### REVERSED EULER ###\n')
reversed_euler.print_solution(file2)

trapezoid = Trapezoid(A, None, X0, None, 0.1, 1, 1)
file2.write('\n\n### TRAPEZOID ###\n')
trapezoid.print_solution(file2)

runge_kutta = RungeKutta(A, None, X0, None, 0.1, 1, 1)
file2.write('\n\n### RUNGE-KUTTA ###\n')
runge_kutta.print_solution(file2)

A = Matrix()
A.init_matrix(2, 2)
A.set(0, 0, 0)
A.set(0, 1, 1)
A.set(1, 0, -200)
A.set(1, 1, -102)

X0 = Matrix()
X0.init_matrix(2, 1)
X0.set(0, 0, 1)
X0.set(1, 0, -2)

pece2 = PECE2(A, None, X0, None, 0.1, 1, 1, 2)
file2.write('\n\n### PECE2 ###\n')
pece2.print_solution(file2)

pece = PECE(A, None, X0, None, 0.1, 1, 1, 1)
file2.write('\n\n### PECE ###\n')
pece.print_solution(file2)

file2b = open("results/task2-b.txt", "w")

A = Matrix()
A.init_matrix(2, 2)
A.set(0, 0, 0)
A.set(0, 1, 1)
A.set(1, 0, -200)
A.set(1, 1, -102)

X0 = Matrix()
X0.init_matrix(2, 1)
X0.set(0, 0, 1)
X0.set(1, 0, -2)

euler = Euler(A, None, X0, None, 0.02, 1, 1)
file2b.write('### EULER ###\n')
euler.print_solution(file2b)

reversed_euler = ReversedEuler(A, None, X0, None, 0.02, 1, 1)
file2b.write('\n\n### REVERSED EULER ###\n')
reversed_euler.print_solution(file2b)

trapezoid = Trapezoid(A, None, X0, None, 0.02, 1, 1)
file2b.write('\n\n### TRAPEZOID ###\n')
trapezoid.print_solution(file2b)

runge_kutta = RungeKutta(A, None, X0, None, 0.02, 1, 1)
file2b.write('\n\n### RUNGE-KUTTA ###\n')
runge_kutta.print_solution(file2b)

A = Matrix()
A.init_matrix(2, 2)
A.set(0, 0, 0)
A.set(0, 1, 1)
A.set(1, 0, -200)
A.set(1, 1, -102)

X0 = Matrix()
X0.init_matrix(2, 1)
X0.set(0, 0, 1)
X0.set(1, 0, -2)

pece2 = PECE2(A, None, X0, None, 0.02, 1, 1, 2)
file2b.write('\n\n### PECE2 ###\n')
pece2.print_solution(file2b)

pece = PECE(A, None, X0, None, 0.02, 1, 1, 1)
file2b.write('\n\n### PECE ###\n')
pece.print_solution(file2b)


## TASK 3 ###
file3 = open("results/task3.txt", "w")

A = Matrix()
A.init_matrix(2, 2)
A.set(0, 0, 0)
A.set(0, 1, -2)
A.set(1, 0, 1)
A.set(1, 1, -3)

B = Matrix()
B.init_matrix(2, 2)
B.set(0, 0, 2)
B.set(0, 1, 0)
B.set(1, 0, 0)
B.set(1, 1, 3)

X0 = Matrix()
X0.init_matrix(2, 1)
X0.set(0, 0, 1)
X0.set(1, 0, 3)

euler = Euler(A, B, X0, [Function1(), Function1()], 0.01, 10, 100)
file3.write('### EULER ###\n')
euler.print_solution(file3)

reversed_euler = ReversedEuler(A, B, X0, [Function1(), Function1()], 0.01, 10, 100)
file3.write('\n\n### REVERSED EULER ###\n')
reversed_euler.print_solution(file3)

trapezoid = Trapezoid(A, B, X0, [Function1(), Function1()], 0.01, 10, 100)
file3.write('\n\n### TRAPEZOID ###\n')
trapezoid.print_solution(file3)

runge_kutta = RungeKutta(A, B, X0, [Function1(), Function1()], 0.01, 10, 100)
file3.write('\n\n### RUNGE-KUTTA ###\n')
runge_kutta.print_solution(file3)

A = Matrix()
A.init_matrix(2, 2)
A.set(0, 0, 0)
A.set(0, 1, -2)
A.set(1, 0, 1)
A.set(1, 1, -3)

B = Matrix()
B.init_matrix(2, 2)
B.set(0, 0, 2)
B.set(0, 1, 0)
B.set(1, 0, 0)
B.set(1, 1, 3)

X0 = Matrix()
X0.init_matrix(2, 1)
X0.set(0, 0, 1)
X0.set(1, 0, 3)

pece2 = PECE2(A, B, X0, [Function1(), Function1()], 0.01, 10, 100, 2)
file3.write('\n\n### PECE2 ###\n')
pece2.print_solution(file3)

pece = PECE(A, B, X0, [Function1(), Function1()], 0.01, 10, 100, 1)
file3.write('\n\n### PECE ###\n')
pece.print_solution(file3)


## TASK 4 ###
file4 = open("results/task4.txt", "w")

A = Matrix()
A.init_matrix(2, 2)
A.set(0, 0, 1)
A.set(0, 1, -5)
A.set(1, 0, 1)
A.set(1, 1, -7)

B = Matrix()
B.init_matrix(2, 2)
B.set(0, 0, 5)
B.set(0, 1, 0)
B.set(1, 0, 0)
B.set(1, 1, 3)

X0 = Matrix()
X0.init_matrix(2, 1)
X0.set(0, 0, -1)
X0.set(1, 0, 3)

euler = Euler(A, B, X0, [Function2(), Function2()], 0.01, 1, 10)
file4.write('### EULER ###\n')
euler.print_solution(file4)

reversed_euler = ReversedEuler(A, B, X0, [Function2(), Function2()], 0.01, 1, 10)
file4.write('\n\n### REVERSED EULER ###\n')
reversed_euler.print_solution(file4)

trapezoid = Trapezoid(A, B, X0, [Function2(), Function2()], 0.01, 1, 10)
file4.write('\n\n### TRAPEZOID ###\n')
trapezoid.print_solution(file4)

runge_kutta = RungeKutta(A, B, X0, [Function2(), Function2()], 0.01, 1, 10)
file4.write('\n\n### RUNGE-KUTTA ###\n')
runge_kutta.print_solution(file4)

A = Matrix()
A.init_matrix(2, 2)
A.set(0, 0, 1)
A.set(0, 1, -5)
A.set(1, 0, 1)
A.set(1, 1, -7)

B = Matrix()
B.init_matrix(2, 2)
B.set(0, 0, 5)
B.set(0, 1, 0)
B.set(1, 0, 0)
B.set(1, 1, 3)

X0 = Matrix()
X0.init_matrix(2, 1)
X0.set(0, 0, -1)
X0.set(1, 0, 3)

pece2 = PECE2(A, B, X0, [Function2(), Function2()], 0.01, 1, 10, 2)
file4.write('\n\n### PECE2 ###\n')
pece2.print_solution(file4)

pece = PECE(A, B, X0, [Function2(), Function2()], 0.01, 1, 10, 1)
file4.write('\n\n### PECE ###\n')
pece.print_solution(file4)
