#Convert Binary into Decimal and vice-versa
print("Select a choice:")
print("1.Binary to Decimal\n2.Decimal to Binary")
ch=int(input("Your choice:"))
c=s=0
if ch==1:
    n=n2=int(input("Enter a Binary number:"))
    #Binary to Decimal
    while n>0:
        r=n%10
        s+=r*(2**c)
        c+=1
        n=n//10
    print("Decimal of",n2,"is",s)
elif ch==2:
    n=n2=int(input("Enter a Decimal number:"))
    #Decimal to Binary
    while n>0:
        r=n%2
        s+=r*(10**c)
        c+=1
        n=n//2
    print("Binary of",n2,"is",s)
else:
    print("Wrong choice")