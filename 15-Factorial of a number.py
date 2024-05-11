#prg to find factorial of a number entered by the user
n=int(input("Enter a no:"))
f=1
for i in range(1,n+1):
    f*=i
print(n,"!=",f)