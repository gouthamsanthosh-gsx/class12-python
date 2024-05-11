#Count digits of a number using while loop
n=int(input("Enter a no:"))
c=0
while n>0:
    n=n//10
    c+=1
print("The no. of digits is",c)