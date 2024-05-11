#Input elements in a list, arrange in ascending or descending without built-in function(INSERTION SELECTION SORT)
#Just the opposite of bubble sort
n=int(input("Enter the no. of elements: "))
l1=[]
for i in range(n):
    x=int(input("Enter element: "))
    l1.append(x)
print("Original list:",l1)

for i in range(1,n):
    j=i
    while l1[j-1]>l1[j] and j>0:
        l1[j-1],l1[j]=l1[j],l1[j-1]
        j-=1
print("New list:",l1)