#Find the greatest and smallest elements from a list without using built-in functions
n=int(input("Enter the no. of elements: "))
l1=[]
for i in range(n):
    x=int(input("Enter element: "))
    l1.append(x)
print("Original list:",l1)
sn=l1[0]
ln=l1[0]
for i in l1:
    if i>ln:
        ln=i
    elif i<sn:
        sn=i
print("Smallest element:",sn)
print("Largest element:",ln)