#prg to display multiplication table of any number
n=int(input("Enter a no:"))
print("Multiplication Table of",n)
for i in range(1,11):
    print(n,"x",i,"=",n*i)