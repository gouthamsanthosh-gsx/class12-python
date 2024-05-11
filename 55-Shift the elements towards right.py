#Input elements in a list. Shift the elements towards right, such that the last element will take first position, first will take second position and so on.
#eg:[1,2,3,4] is changed into [4,1,2,3]
n=int(input("Enter the no. of elements: "))
l1=[]
for i in range(n):
    x=int(input("Enter element: "))
    l1.append(x)
print("Original list:",l1)
b=l1[n-1]
for i in range(n-1,0,-1):
    l1[i]=l1[i-1]
l1[0]=b
print(l1)