#prg to find the sum of factorial of 'n' numbers
n=int(input("Enter a no:"))
f=1
sum=0
for i in range(1,n+1):
    f*=i
    sum+=f
print(sum)