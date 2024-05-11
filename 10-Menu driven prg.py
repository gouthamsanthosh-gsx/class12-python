#Prg to execute according to user's choice
#Addition
#Subtraction
#Multiplication
#Division
print('1.Addition')
print('2.Subtraction')
print('3.Multiplication')
print('4.Division')
ch=int(input("Enter your choice:"))
if ch>4 or ch<1:
    print("Wrong choice")
else:
    x=int(input("Enter first no:"))
    y=int(input("Enter second no:"))
    if ch==1:
        print(x+y)
    elif ch==2:
        print(x-y)
    elif ch==3:
        print(x*y)
    else:
        print(x/y)