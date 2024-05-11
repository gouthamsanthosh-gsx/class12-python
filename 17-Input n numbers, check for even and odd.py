#prg to input n numbers, check for even and odd numbers
limit=int(input("Enter the limit:"))
for i in range(1,limit+1):
    x=int(input("Enter a no:"))
    if x%2==0:
        print(x,"is an even number.")
    else:
        print(x,"is an odd number.")