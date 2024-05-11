#Reverse a number and check whether the number is palindrome or not
n=n2=int(input("Enter a no:"))
new=0
while n>0:
    r=n%10
    new=(new*10)+r
    n=n//10
print("Reverse is",new)
if n2==new:
    print("It is palindrome.")
else:
    print("It is not palindrome.")