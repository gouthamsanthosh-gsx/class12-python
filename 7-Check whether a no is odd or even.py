#Prg to check whether a number is even or not. If reminder is zero when a number is divided by 2, then it's an even number.
num=int(input("Enter a number:"))
if (num%2)==0:
    print("It is an even number")
else:
    print("It is an odd number")