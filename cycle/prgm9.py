print("Name: Aparna Jayakumar")
print("Reg no: SJC22MCA-2012")
print("course: Data Science Lab")
print("coursecode: 20MCA241")
print("Date: 3-10-23")
l=[]
m=[]
n=[]
a=int(input("Enter total number of elements in alist "))
print("First list:")
for i in range(1,a+1):
    b=int(input("Enter the value of %d index is:" %i))
    l.append(b)
print("Second list")
for i in range(1,a+1):
    c=int(input("Enter the value of %d index is:" %i))
    m.append(c)
for j in range(a):
    n.append(l[j]+m[j])
print("Result",n)

