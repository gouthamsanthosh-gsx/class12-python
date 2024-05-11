#prg to find the sum of the series:x^1/1!-x^2/2!+x^3/3!-x^4/4!...x^n/n!
x=int(input("Enter the value of x:"))
n=int(input("Enter the value of n:"))
a=0
c=1
f=1
for i in range(1,n+1):
    f*=i
    a+=c*(x**i/f)
    c*=-1
print(a)