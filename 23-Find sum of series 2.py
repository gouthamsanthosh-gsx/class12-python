#prg to find the sum of the series:x^1/1!+x^2/2!+x^3/3!...x^n/n!
x=int(input("Enter the value of x:"))
n=int(input("Enter the value of n:"))
a=f,b=1,0
for i in range(1,n+1):
    f*=i
    a=(x**i)/f
    b+=a
print(b)