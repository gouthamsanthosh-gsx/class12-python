#Input elements in a list, arrange in ascending or descending without built-in function(SELECTION SORT)
n=int(input("Enter the no of elements: "))
l1=[]
for i in range(n):
    x=int(input("Enter the elements: "))
    l1.append(x)
print(l1)

for i in range(n):
    #sm-Smallest no
    #p-Position
    sm=l1[i]
    p=i
    for j in range(i+1,n):
        if sm>l1[j]:
            sm=l1[j]
            p=j
    #Shifting
    for k in range(p,i,-1):
        l1[k]=l1[k-1]
    l1[i]=sm
print(l1)