import numpy as np
print("Name: Aparna Jayakumar")
print("Reg no: SJC22MCA-2012")
print("course: Data Science Lab")
print("coursecode: 20MCA241")
print("Date: 13-10-23")
n = int(input("Enter the size of the square matrix: "))
square_matrix = np.zeros((n, n))

print("Enter elements for the square matrix:")
for i in range(n):
    row = input().split()
    for j in range(n):
        square_matrix[i][j] = int(row[j])
diagonal_elements_square = np.diag(square_matrix)
print("\nDiagonal Elements of Square Matrix:")
print(diagonal_elements_square)
print()
m = int(input("Enter the number of rows for the rectangular matrix: "))
n = int(input("Enter the number of columns for the rectangular matrix: "))
rectangular_matrix = np.zeros((m, n))

print("\nEnter elements for the rectangular matrix:")
for i in range(m):
    row = input().split()
    for j in range(n):
        rectangular_matrix[i][j] = int(row[j])
main_diagonal_elements_rectangular = np.diag(rectangular_matrix)
print("\nMain Diagonal Elements of Rectangular Matrix:")
print(main_diagonal_elements_rectangular)