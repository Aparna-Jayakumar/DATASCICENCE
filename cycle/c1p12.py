print("Name: Aparna Jayakumar")
print("Reg no: SJC22MCA-2012")
print("course: Data Science Lab")
print("coursecode: 20MCA241")
print("Date: 3-10-23")
vowels='aeiou'
a=input("Enter the string:")
a=a.casefold()
count={}.fromkeys(vowels,0)
for char in a:
    if char in count:
        count[char] +=1
print(count)
