#prg to check whether a no is perfect number or not
#eg:6=1+2+3
n=int(input("Enter a no:"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print(n,"is a perfect number")
else:
    print(n,"is not a perfect number")