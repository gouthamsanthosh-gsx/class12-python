#prg to find the sum of : x^1+x^2+x^3...x^n
x=int(input("Enter x:"))
n=int(input("Enter n:"))
a=0
for i in range(1,n+1):
    a+=x**i
print(a)