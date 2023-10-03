print("Name: Aparna Jayakumar")
print("Reg no: SJC22MCA-2012")
print("course: Data Science Lab")
print("coursecode: 20MCA241")
print("Date: 26-10-23")
print("Arm strong numbers upto 1000 are:")
for i in range(1,1000):
    n=i
    sum=0
    while(i>0):
        rem= i % 10
        sum= sum  + (rem * rem * rem)
        i= i//10
    if (sum == n):
        print(n)

