print("Name: Aparna Jayakumar")
print("Reg no: SJC22MCA-2012")
print("course: Data Science Lab")
print("coursecode: 20MCA241")
print("Date: 26-09-23")
n=int(input("Enter a number:\n"))
sum=0
for i in range(1,n):
    if(n % i == 0):
        sum=sum+i
if( sum == n):
    print("The number is perfect number")
else:
    print("The entered number is not perfect")