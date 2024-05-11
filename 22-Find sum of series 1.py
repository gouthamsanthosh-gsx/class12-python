#prg to find the sum of: x/1+x/2+x/3...x/n
x=int(input("Enter the value of x:"))
n=int(input("Enter the value of n:"))
a,b=1,0
for i in range(1,n+1):
    a=x/i
    b+=a
print(b)