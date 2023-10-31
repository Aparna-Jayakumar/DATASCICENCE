import numpy as np
print("Name: Aparna Jayakumar")
print("Reg no: SJC22MCA-2012")
print("course: Data Science Lab")
print("coursecode: 20MCA241")
print("Date: 10-10-23")

even_numbers = np.arange(2, 32, 2)
print("1D Array with the first 15 even numbers:")
print(even_numbers)

subset_a = even_numbers[2:9:2]
print("\nElements from index 2 to 8 with step 2 (using slice):")
print(subset_a)

subset_b = even_numbers[-3:]
print("\nLast 3 elements of the array using negative index:")
print(subset_b)

subset_c = even_numbers[::2]
print("\nAlternate elements of the array:")
print(subset_c)

subset_d = even_numbers[-3::2]
print("\nLast 3 alternate elements:")
print(subset_d)
