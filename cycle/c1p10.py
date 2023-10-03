print("Name: Aparna Jayakumar")
print("Reg no: SJC22MCA-2012")
print("course: Data Science Lab")
print("coursecode: 20MCA241")
print("Date: 3-10-23")
r=int(input("Enter the Number Rows: "));
c=int(input("Enter the Number Coloums: "));
a = [[0 for j in range(0,c)] for i in range(0,r)]
b = [[0 for j in range(0,c)] for i in range(0,r)]
sum = [[0 for j in range(0,c)] for i in range(0,r)]
print("Enter the Elements of Matrix a:")
for i in range(0,r):
    for j in range(0,c):
        print("Enter an Element (",i+1,",",j+1,"): ")
        a[i][j]= int(input())
print("Enter the Elements of Matrix b:")
for i in range(0,r):
    for j in range(0,c):
        print("Enter an Element (",i+1,",",j+1,"): ")
        b[i][j]=int(input())
for i in range(0,r):
    for j in range(0,c):
        sum[i][j]=a[i][j]+b[i][j]

print("Sum of Matrices is")
for i in sum:
    print(i)
