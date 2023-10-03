print("Name: Aparna Jayakumar")
print("Reg no: SJC22MCA-2012")
print("course: Data Science Lab")
print("coursecode: 20MCA241")
print("Date: 25-09-23")
x=int(input())
y=int(input())
print("lower=",x)
print("upper",y)
print("The prime numbers in between the range ",x,y)
for n in range(x, y+1):
    if(n > 1):
        for i in range(2,n):
            if(n % i) == 0:
                print(n)
                break
