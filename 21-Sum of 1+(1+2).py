#prg to find the sum of : 1+(1+2)+(1+2+3)+(1+2+3+4).....(1+2+3+4+...n)
n=int(input("Enter a no:"))
x=y=0
for i in range(1,n+1):
    x+=i
    y+=x
print(y)