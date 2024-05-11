#prg to enter marks of 5 subjects to find the average
a=float(input("Enter mark of 1st subject:"))
b=float(input("Enter mark of 2nd subject:"))
c=float(input("Enter mark of 3rd subject:"))
d=float(input("Enter mark of 4th subject:"))
e=float(input("Enter mark of 5th subject:"))
#Avg out of 100
avg=(a+b+c+d+e)*1/5
print("The average is",avg)
#Print grade
if avg>=91:
    print("Grade:A1")
elif avg>=81:
    print("Grade:A2")
elif avg>=71:
    print("Grade:B1")
elif avg>=61:
    print("Grade:B2")
elif avg>=51:
    print("Grade:C1")
elif avg>=41:
    print("Grade:C2")
elif avg>=33:
    print("Grade:D")
else:
    print("Grade:E")