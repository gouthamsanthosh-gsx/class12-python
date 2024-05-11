#Check whether a number is amstrong number or not
#eg:371 3^3 + 7^3 + 1^3 = 371
n=n2=int(input("Enter a no:"))
s=0
while n>0:
    x=n%10
    s+=x**3
    n=n//10
if s==n2:
    print(n2,"is an Amstrong number.")
else:
    print(n2,"is not an Amstrong number.")