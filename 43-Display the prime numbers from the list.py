#Prg to input n elements and display the prime numbers from the list
n=int(input("Enter the no. of elements: "))
l=[]
l1=[]
for i in range(n):
    x=int(input("Enter element: "))
    l.append(x)
print("The list is:",l)
for i in l:
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        l1.append(i)
print(l1)