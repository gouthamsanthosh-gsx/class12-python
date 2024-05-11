#prg to find the sum of even nos till 'n'
x=0
n=int(input("Enter a no:"))
for i in range(2,n,2):
    x+=i
print("The sum of even numbers till",n,"is",x)