#Write a menu driven program to convert:
#Celsius to Fahrenheit f=c*9/5+32
#Fahrenheit to Celsius c=(f-32)*(5/9)
print('1.Celsius to Fahrenheit')
print('2.Fahrenheit to Celsius')
ch=int(input("Enter your choice:"))
if ch==1:
    c=float(input("Enter temp in Celsius:"))
    f=c*9/5+32
    print(c,"in Fahrenheit is",f)
elif ch==2:
    f=float(input("Enter temp in Fahrenheit:"))
    c=(f-32)*(5/9)
    print(f,"in Celsius:",c)
else:
    print("Wrong choice")