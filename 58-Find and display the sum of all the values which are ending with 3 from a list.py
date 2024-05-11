#Find and display the sum of all the values which are ending with 3 from a list
n=int(input("Enter the no. of elements: "))
l1=[]
l2=[]
for i in range(n):
    x=int(input("Enter element: "))
    l1.append(x)
print("Original list:",l1)
for i in l1:
    if i%10==3:
        l2.append(i)
print("New list:",l2)
#Sum of values
s=0
for i in l2:
    s+=i
print("Sum of all the values ending with 3:",s)