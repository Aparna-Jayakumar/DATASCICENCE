import numpy as np
print("Name: Aparna Jayakumar")
print("Reg no: SJC22MCA-2012")
print("course: Data Science Lab")
print("coursecode: 20MCA241")
print("Date: 10-10-23")
matrix1 = np.array([[51, 82, 37], [14, 20, 62], [7, 10, 77]])
matrix2 = np.array([[5, 43, 22], [9, 12, 80], [32, 52, 71]])
print("Matrix 1:")
print(matrix1)

print("Matrix 2:")
print(matrix2)

matrix_sum = matrix1 + matrix2
print("Sum of the two matrices:")
print(matrix_sum)
matrix_diff = matrix1 - matrix2
print("\nDifference of the two matrices:")
print(matrix_diff)
matrix_product = matrix1 * matrix2
print("\nElement-wise product of the two matrices:")
print(matrix_product)
with np.errstate(divide='ignore', invalid='ignore'):
    matrix_division = np.true_divide(matrix1, matrix2)
    matrix_division[~np.isfinite(matrix_division)] = np.nan
print("\nElement-wise division of the two matrices:")
print(matrix_division)
matrix_mult = np.dot(matrix1, matrix2)
print("\nMatrix multiplication of the two matrices:")
print(matrix_mult)
matrix1_transpose = np.transpose(matrix1)
print("\nTranspose of matrix1:")
print(matrix1_transpose)
diagonal_sum = np.trace(matrix1)
print("\nSum of diagonal elements of matrix1:")
print(diagonal_sum)