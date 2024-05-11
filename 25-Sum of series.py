#prg to find the sum of the series:x^1/1!+x^3/3!+x^5/5!...x^2n-1/2n-1!
x=int(input("Enter the value of x:"))
n=int(input("Enter the value of n:"))
f=1
s=0
for i in range(1,(2*n),2):
    f*=i
    s+=(x**i)/f
    f*=(i+1)
print(s)