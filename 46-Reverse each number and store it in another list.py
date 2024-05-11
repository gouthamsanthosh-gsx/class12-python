#Input elements in a list, reverse each number and store it in another list
n=int(input("Enter the no. of elements: "))
l=[]
l1=[]
for i in range(n):
    x=int(input("Enter element: "))
    l.append(x)
for i in l:
    new=0
    while i>0:
        r=i%10
        new=(new*10)+r
        i=i//10
    l1.append(new)
print(l1)