#Linear search in a list
n=int(input("Enter the no. of elements: "))
l1=[]
for i in range(n):
    x=int(input("Enter element: "))
    l1.append(x)
print("Original list:",l1)
s_value=int(input("Enter the no. to be searched: "))
index=c=0
for i in l1:
    index+=1
    if s_value==i:
        print("Data:",i,"Index:",index)
        #Count the results
        c+=1
if c==0:
    print("'",s_value,"'","is not present in the list.")
else:
    print("Items found:",c)