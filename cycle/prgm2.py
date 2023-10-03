print("Name: Aparna Jayakumar")
print("Reg no: SJC22MCA-2012")
print("course: Data Science Lab")
print("coursecode: 20MCA241")
print("Date: 25-09-23")
n= int(input("Limit of series:\n"))
a=0
b=1
count=0
if(n <= 0):
    print("Invalid input..")
else:
    print("Fibonacci Series.....")
    while(count < n):
        print(a)
        next=a+b
        a=b
        b=next
        count=count+1