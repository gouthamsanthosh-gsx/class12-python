#Input elements in a list. Shift the elements towards left, such that the first element will take last position, second will take first position and so on.
#eg:[1,2,3,4] is changed into [2,3,4,1]
n=int(input("Enter the no. of elements: "))
l1=[]
for i in range(n):
    x=int(input("Enter element: "))
    l1.append(x)
print("Original list:",l1)
b=l1[0]
for i in range(0,n-1):
    l1[i]=l1[i+1]
l1[n-1]=b
print(l1)