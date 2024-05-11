#Prg to input elements in a list and swap the alternate elements in the list
'''eg: l=[10,20,30,40,50,60] then output should be l=[20,10,40,30,60,50]'''
n=int(input("Enter the no. of elements: "))
l=[]
for i in range(n):
    x=int(input("Enter element: "))
    l.append(x)
for i in range(1,n,2):
    l[i],l[i-1]=l[i-1],l[i]
print(l)