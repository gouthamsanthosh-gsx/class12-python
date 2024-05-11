#Input elements in a list and convert each number into it's binary equivalent and store it in another list
n=int(input("Enter the no. of elements: "))
l=[]
l1=[]
for i in range(n):
    x=int(input("Enter element: "))
    l.append(x)
print("Original list:",l)
for i in l:
    c=s=0
    while i>0:
        r=i%2
        s+=r*(10**c)
        c+=1
        i//=2
    l1.append(s)
print("New list:",l1)