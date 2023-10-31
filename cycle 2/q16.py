import numpy as np
print("Name: Aparna Jayakumar")
print("Reg no: SJC22MCA-2012")
print("course: Data Science Lab")
print("coursecode: 20MCA241")
print("Date: 16-10-23")
A = np.array([[5, 27, 32], [14, 53, 62], [67, 88, 19]])
U, S, Vt = np.linalg.svd(A)
A_hat = U @ np.diag(S) @ Vt

print("Original Matrix A:")
print(A)
print("\nSingular Values:")
print(S)
print("\nReconstructed Matrix A_hat:")
print(A_hat)