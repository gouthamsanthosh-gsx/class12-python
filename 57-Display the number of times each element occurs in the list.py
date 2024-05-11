#Input elements in a list. Display the number of times each element occurs in the list.
#eg: list is [1,1,2,3,4,4,5,6,7,8,8,8,9,0,0]
#number-1 frequency-2
n=int(input("Enter the no. of elements: "))
l=[]
l1=[]
l2=[]
for i in range(n):
    x=int(input("Enter element: "))
    l.append(x)
print("Original list:",l)
for i in l:
    if i not in l1:
        l1.append(i)
        x=l.count(i)
        l2.append(x)
print("Number | Frequency")
for i in range(len(l1)):
    print(" ",l1[i],"       ",l2[i])