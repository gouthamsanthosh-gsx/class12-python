#Prg to find the greatest of 3 nos
a=int(input("Enter first no:"))
b=int(input("Enter second no:"))
c=int(input("Enter third no:"))
if a>b and a>c:
    print(a,"is the greatest")
elif b>a and b>c:
    print(b,"is the greatest")
else:
    print(c,"is the greatest")