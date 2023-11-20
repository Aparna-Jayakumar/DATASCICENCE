import numpy as np
print("Name: Aparna Jayakumar")
print("Reg no: SJC22MCA-2012")
print("course: Data Science Lab")
print("coursecode: 20MCA241")
print("Date: 10-10-23")
two_dim_array = np.arange(16).reshape(4, 4)
print("\n2D Array:")
print(two_dim_array)
print("\nAll elements excluding the first row:")
print(two_dim_array[1:])
print("\nAll elements excluding the last column:")
print(two_dim_array[:, :-1])
print("\nElements of the 1st and 2nd column in the 2nd and 3rd row:")
print(two_dim_array[1:3, 0:2])
print("\nElements of the 2nd and 3rd column:")
print(two_dim_array[:, 1:3])
print("\n2nd and 3rd element of the 1st row:")
print(two_dim_array[0, 1:3])
print("\nElements from indices 4 to 10 in descending order:")
print(two_dim_array[3:0:-1, 2:0:-1])