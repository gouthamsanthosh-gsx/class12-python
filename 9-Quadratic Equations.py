#Solving quadratic equations
import math
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))
#Find discriminant
D=(b**2)-(4*a*c)
#Find the roots
if D>0:
    #Square root of discriminant
    d=math.sqrt(D)
    x1=(-b+d)/(2*a)
    x2=(-b-d)/(2*a)
    print("Equation has real and distinct roots.\nThe roots are:",x1,"and",x2)
elif D==0:
    x1=(-b/(2*a))
    x2=x1
    print("Equation has 2 real and equal roots.\nThe roots are:",x1,"and",x2)
else:
    print("No roots(Imaginary roots)")