import math
print("Name: Aparna Jayakumar")
print("Reg no: SJC22MCA-2012")
print("course: Data Science Lab")
print("coursecode: 20MCA241")
print("Date: 25-10-23")
print("Coeffient  of equation ax^2 + bx +c")
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
d= b*b -4*a*c
if(d<0):
    print("Roots are imaginary")
else:
    r1= (-b + d)/2*a
    r2= (-b + d)/2*a
    print("Root 1",round(r1,2))
    print("Root 2",round(r2,2))