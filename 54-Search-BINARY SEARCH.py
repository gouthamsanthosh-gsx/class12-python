#Binary search in a list
#1.List should be sorted
n=int(input("Enter the no. of elements: "))
l1=[]
for i in range(n):
    x=int(input("Enter element: "))
    l1.append(x)
print("Original list:",l1)
#Sort the list(bubble sort)
for i in range(n):
    for j in range(n-1):
        if l1[j]>l1[j+1]:
            l1[j],l1[j+1]=l1[j+1],l1[j]
print("Sorted list:",l1)
#Binary Search
a=int(input("Enter the value to be searched: "))
l=0
u=n-1
c=0
while l<=u:
    m=(l+u)//2
    if l1[m]==a:
        print("Item found at:",m+1)
        c+=1
        break
    elif l1[m]>a:
        u=m-1
    else:
        l=m+1
if c==0:
    print("Couldn't find",a)