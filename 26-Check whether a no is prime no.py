#prg to check whether a number is prime or not
n=int(input("Enter a no:"))
num=0
for i in range(1,n+1):
    if n%i==0:
        num+=1
if num==2:
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")