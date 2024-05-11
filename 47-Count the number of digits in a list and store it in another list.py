#Input elements in a list,  count the number of digits and store it in another list
n=int(input("Enter the no. of elements: "))
l=[]
l1=[]
for i in range(n):
    x=int(input("Enter element: "))
    l.append(x)
print("Original list:",l)
for i in l:
    c=0
    while i>0:
        i//=10
        c+=1
    l1.append(c)
print("New list:",l1)