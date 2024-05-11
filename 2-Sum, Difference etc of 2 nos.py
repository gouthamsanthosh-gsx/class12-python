#Prg to make sum, difference,
#multiplication, quotient and remainder of 2 nos
#entered by the user
a=int(input("Enter first no:"))
b=int(input("Enter second no:"))
sum=a+b
dif=a-b
mul=a*b
quo=a//b
rem=a%b
pow=a**b
print(a,'+',b,'=',sum)
print(a,'-',b,'=',dif)
print(a,'*',b,'=',mul)
print(a,'//',b,'=',quo)
print(a,'%',b,'=',rem)
print(a,'**',b,'=',pow)