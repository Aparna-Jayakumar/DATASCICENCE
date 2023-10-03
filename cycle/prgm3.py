print("Name: Aparna Jayakumar")
print("Reg no: SJC22MCA-2012")
print("course: Data Science Lab")
print("coursecode: 20MCA241")
print("Date: 25-09-23")
print("Input length of Triangle Sides:")
x=int(input("x:"))
y=int(input("y:"))
z=int(input("z:"))
if( x == y == z):
    print("Equilateral triangle")
elif(x == y or y==z or z==x):
    print("Isosceles triangle")
else:
    print("Triangle is Scalene")