from Matrix import Matrix
import Helper

"""
Main file for testing out the behavior of the Matrix.
"""

# task one
print('Task one:')
print()
mat1 = Matrix()
mat1_copy = Matrix()

mat1.init_matrix_from_file("files/mat1.txt")
mat1_copy.init_matrix_from_data(mat1.data)
print(mat1 == mat1_copy)

mat1.multiply_by_scalar(3.3)
mat1.divide_by_scalar(3.3)
print(mat1 == mat1_copy)
print()

# task two
print('Task two:')
print()
mat2 = Matrix()
mat2.init_matrix_from_file("files/mat2.txt")
b2 = Matrix()
b2.init_matrix_from_file("files/b2.txt")
# s = Helper.find_solution(mat2, b2, False)
# s.print()

mat2.init_matrix_from_file("files/mat2.txt")
s = Helper.find_solution(mat2, b2, True)
s.print()
print()

# task three
print('Task three:')
print()
mat3 = Matrix()
mat3.init_matrix_from_file("files/mat3.txt")
mat3_copy = Matrix()
mat3_copy.init_matrix_from_file("files/mat3.txt")

mat3.lup_decomposition(False)
mat3.L.print()
mat3.U.print()

mat3_copy.lup_decomposition(True)
mat3_copy.L.print()
mat3_copy.U.print()
mat3_copy.P.print()

b3 = Matrix()
b3.init_matrix_from_file("files/b3.txt")
s = Helper.find_solution(mat3_copy, b3, True)
s.print()
print()

# task four
print('Task four:')
print()
mat4 = Matrix()
mat4_copy = Matrix()
mat4.init_matrix_from_file("files/mat4.txt")
mat4_copy.init_matrix_from_file("files/mat4.txt")
b4 = Matrix()
b4.init_matrix_from_file("files/b4.txt")

s = Helper.find_solution(mat4, b4, False)
s.print()

s = Helper.find_solution(mat4_copy, b4, True)
s.print()
print()

# task five
print('Task five:')
print()
mat5 = Matrix()
mat5.init_matrix_from_file("files/mat5.txt")
b5 = Matrix()
b5.init_matrix_from_file("files/b5.txt")
s = Helper.find_solution(mat5, b5, True)
s.print()
print()

# task six
print('Task six:')
print()
mat6 = Matrix()
mat6.init_matrix_from_file("files/mat6.txt")
b6 = Matrix()
b6.init_matrix_from_file("files/b6.txt")
s = Helper.find_solution(mat6, b6, True)
s.print()
print()

# task seven
print('Task seven:')
print()
mat7 = Matrix()
mat7.init_matrix_from_file("files/mat7.txt")
inverse = mat7.inverse_matrix()
inverse.print()
print()

# task eight
print('Task eight:')
print()
mat8 = Matrix()
mat8.init_matrix_from_file("files/mat8.txt")
inverse = mat8.inverse_matrix()
inverse.print()
print()

# task nine
print('Task nine:')
print()
mat9 = Matrix()
mat9.init_matrix_from_file("files/mat9.txt")
determinant = mat9.calculate_determinant()
print(determinant)
print()

# task ten
print('Task ten:')
print()
mat10 = Matrix()
mat10.init_matrix_from_file("files/mat10.txt")
determinant = mat10.calculate_determinant()
print(determinant)
print()
