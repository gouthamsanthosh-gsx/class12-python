#prg to find the factors of n(n is entered by user)
n=int(input("Enter a no:"))
print("The factors of",n,"are:")
for i in range(1,n+1):
    if n%i==0:
        print(i)