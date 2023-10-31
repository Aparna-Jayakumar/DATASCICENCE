import numpy as np
print("Name: Aparna Jayakumar")
print("Reg no: SJC22MCA-2012")
print("course: Data Science Lab")
print("coursecode: 20MCA241")
print("Date: 10-10-23")
arr= np.array([[1.0+2.0j,2.0+3.0j,8.0+4.0j],[1.0+2.0j,8.0+6.0j,5.0+3.0j]])
print(arr)
print("number of coloumns and rows")
print(arr.shape)
print("type___")
print(arr.dtype)
print("reshaped matrix")
new=arr.reshape(3,2)
print(new)


