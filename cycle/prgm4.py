print("Name: Aparna Jayakumar")
print("Reg no: SJC22MCA-2012")
print("course: Data Science Lab")
print("coursecode: 20MCA241")
print("Date: 25-10-23")
def are_coprime(a,b):
    
    hcf = 1
    for i in range(1, a+1):
        if a%i==0 and b%i==0:
            hcf = i

    return hcf == 1
first = int(input('Enter first number: '))
second = int(input('Enter second number: '))

if are_coprime(first, second):
    print('%d and %d are CO-PRIME' %(first, second))
else:
    print('%d and %d are NOT CO-PRIME' %(first, second))
