#prg to find the sum of squares of numbers till 'n'(1^2+2^2+3^2...n^2)
x=0
n=int(input("Enter a no:"))
for i in range(1,n):
    x+=i**2
print("The sum of squares of numbers till",n,"is",x)