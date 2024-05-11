#Write a prg to enter elements in a list. Count and display the number of even and odd numbers
n=int(input("Enter the no. of elements: "))
l=[]
for i in range(n):
    x=int(input("Enter element: "))
    l.append(x)
print("The list is:",l)
c_even=c_odd=0 #counters
for i in l:
    if i%2==0:
        c_even+=1
    else:
        c_odd+=1
print("The number of even numbers in list is",c_even,"and the number of odd numbers is",c_odd)