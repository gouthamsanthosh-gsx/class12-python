#Find the sum of the digits of a number
n=int(input("Enter a no:"))
s=0
while n>0:
    r=n%10
    s+=r
    n=n//10
print("Sum of the digits is",s)