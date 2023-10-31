import numpy as np
print("Name: Aparna Jayakumar")
print("Reg no: SJC22MCA-2012")
print("course: Data Science Lab")
print("coursecode: 20MCA241")
print("Date: 13-10-23")
A = np.array([[2, 3, -1],
              [1, 2, 1],
              [3, 1, -2]])

b = np.array([7, 3, 8])

try:

    X = np.linalg.solve(A, b)
    print("Solution X:")
    print(X)
except np.linalg.LinAlgError:
    print("Matrix A is singular. The system of equations may not have a unique solution.")