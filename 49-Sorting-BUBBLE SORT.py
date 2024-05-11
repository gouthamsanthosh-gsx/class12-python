#Input elements in a list, arrange in ascending or descending without built-in function(BUBBLE SORT)
n=int(input("Enter the no. of elements: "))
l=[]
for i in range(n):
    x=int(input("Enter element: "))
    l.append(x)
print(l)

for i in range(n):
    for j in range(n-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print("Sorted list:",l)