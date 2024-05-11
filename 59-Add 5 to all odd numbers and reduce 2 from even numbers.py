#Add 5 to all odd numbers and reduce 2 from even numbers
n=int(input("Enter the no. of elements: "))
l1=[]
l2=[]
for i in range(n):
    x=int(input("Enter element: "))
    l1.append(x)
print("Original list:",l1)
for i in l1:
    #nn is new number
    if i%2==0:
        nn=i-2
    else:
        nn=i+5
    l2.append(nn)
print("New list:",l2)