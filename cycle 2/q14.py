import numpy as np
print("Name: Aparna Jayakumar")
print("Reg no: SJC22MCA-2012")
print("course: Data Science Lab")
print("coursecode: 20MCA241")
print("Date: 16-10-23")
def is_symmetric(matrix):
    return np.array_equal(matrix, matrix.T)
def is_skew_symmetric(matrix):
    return np.array_equal(matrix, -matrix.T)

# Input matrix dimensions
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix = np.zeros((rows, cols))

print("Enter matrix elements row by row:")
for i in range(rows):
    row = input().split()
    for j in range(cols):
        matrix[i][j] = float(row[j])
if is_symmetric(matrix):
    print("The matrix is symmetric.")
elif is_skew_symmetric(matrix):
    print("The matrix is skew-symmetric.")
else:
    print("The matrix is neither symmetric nor skew-symmetric.")