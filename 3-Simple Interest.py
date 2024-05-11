#prg to calculate Simple Interest, pricipal, rate and time are entered by the user
p=int(input("Enter principal:"))
r=float(input("Enter rate:"))
t=int(input("Time period(year):"))
si=(p*r*t)/100
print("Simple Interest is",si)