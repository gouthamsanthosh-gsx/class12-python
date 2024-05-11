#Input elements in a list, arrange in ascending or descending without built-in function(EXCHANGE SELECTION SORT)
#Here instead of shifting, we use swapping or exchanging
n=int(input("Enter the no of elements: "))
l1=[]
for i in range(n):
    x=int(input("Enter the elements: "))
    l1.append(x)
print(l1)

for i in range(n):
    sm=l1[i]
    p=i
    for j in range(i+1,n):
        if sm>l1[j]:
            sm=l1[j]
            p=j
    l1[p],l1[i]=l1[i],l1[p]
print(l1)