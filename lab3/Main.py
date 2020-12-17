from OptimisationMethods import *
from ExplicitConstraint import *
from ImplicitConstraint import *

"""
Main file which tests out the behaviour of the Optimisation algorithms.
"""

# task 1
print("### TASK 1 - GRADIENT DESCENT + GOLDEN SECTION / FUNCTION 3 ###")
func = Function3()
minimum = gradient_descent((0, 0), func, True)
print()
print("Minimum: " + str(minimum))
print("Minimum evaluation: " + str(func.calculate(minimum)))
print("Number of function evaluations: " + str(func.called-1))
print("Number of derivative evaluations: " + str(func.called_derivative))
print("\n")

print("### TASK 1 - GRADIENT DESCENT / FUNCTION 3 ###")
func = Function3()
print()
minimum = gradient_descent((0, 0), func, False)
print("\n")


# task 2
print("### TASK 2 - GRADIENT DESCENT + GOLDEN SECTION / FUNCTION 1 ###")
func = Function1()
minimum = gradient_descent((-1.9, 2.0), func, True)
print()
print("Minimum: " + str(minimum))
print("Minimum evaluation: " + str(func.calculate(minimum)))
print("Number of function evaluations: " + str(func.called-1))
print("Number of derivative evaluations: " + str(func.called_derivative))
print("\n")

print("### TASK 2 - GRADIENT DESCENT + GOLDEN SECTION / FUNCTION 2 ###")
func = Function2()
minimum = gradient_descent((0.1, 0.3), func, True)
print()
print("Minimum: " + str(minimum))
print("Minimum evaluation: " + str(func.calculate(minimum)))
print("Number of function evaluations: " + str(func.called-1))
print("Number of derivative evaluations: " + str(func.called_derivative))
print("\n")

print("### TASK 2 - NEWTON-RAPHSON + GOLDEN SECTION / FUNCTION 1 ###")
func = Function1()
minimum = newton_raphson((-1.9, 2.0), func, True)
print()
print("Minimum: " + str(minimum))
print("Minimum evaluation: " + str(func.calculate(minimum)))
print("Number of function evaluations: " + str(func.called-1))
print("Number of derivative evaluations: " + str(func.called_derivative))
print("Number of Hessian matrix evaluations: " + str(func.called_hessian))
print("\n")

print("### TASK 2 - NEWTON-RAPHSON + GOLDEN SECTION / FUNCTION 2 ###")
func = Function2()
minimum = newton_raphson((0.1, 0.3), func, True)
print()
print("Minimum: " + str(minimum))
print("Minimum evaluation: " + str(func.calculate(minimum)))
print("Number of function evaluations: " + str(func.called-1))
print("Number of derivative evaluations: " + str(func.called_derivative))
print("Number of Hessian matrix evaluations: " + str(func.called_hessian))
print("\n")

# task 3
explicit = ExplicitConstraint(-100, 100)
implicit1 = ImplicitConstraint1(False)
implicit2 = ImplicitConstraint2(False)

print("### TASK 3 - BOX / FUNCTION 1 ###")
func = Function1()
minimum = box_algorithm((-1.9, 2.0), func, [explicit], [implicit1, implicit2])
print()
print("Minimum: " + str(minimum))
print("Minimum evaluation: " + str(func.calculate(minimum)))
print("Number of function evaluations: " + str(func.called-1))
print("\n")

print("### TASK 3 - BOX / FUNCTION 2 ###")
func = Function2()
minimum = box_algorithm((0.1, 0.3), func, [explicit], [implicit1, implicit2])
print()
print("Minimum: " + str(minimum))
print("Minimum evaluation: " + str(func.calculate(minimum)))
print("Number of function evaluations: " + str(func.called-1))
print("\n")

# task 4
print("### TASK 4 - TRANSFORMATION + HOOKE-JEEVES / FUNCTION 1 ###")
func = Function1()
minimum = no_constraints_transformation((-1.9, 2.0), func, [implicit1, implicit2])
print()
print("Minimum: " + str(minimum))
print("Minimum evaluation: " + str(func.calculate(minimum)))
print("Number of function evaluations: " + str(func.called-1))
print("\n")

print("### TASK 4 - TRANSFORMATION + HOOKE-JEEVES / FUNCTION 2 ###")
func = Function2()
minimum = no_constraints_transformation((0.1, 0.3), func, [implicit1, implicit2])
print()
print("Minimum: " + str(minimum))
print("Minimum evaluation: " + str(func.calculate(minimum)))
print("Number of function evaluations: " + str(func.called-1))
print("\n")

# task 5
implicit3 = ImplicitConstraint3(True)
implicit4 = ImplicitConstraint4(True)
implicit5 = ImplicitConstraint5(True)

print("### TASK 5 - TRANSFORMATION + HOOKE-JEEVES / FUNCTION 4 ###")
func = Function4()
minimum = no_constraints_transformation((5.0, 5.0), func, [implicit3, implicit4, implicit5])
print()
print("Minimum: " + str(minimum))
print("Minimum evaluation: " + str(func.calculate(minimum)))
print("Number of function evaluations: " + str(func.called-1))
