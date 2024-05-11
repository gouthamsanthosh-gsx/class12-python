#Prg to input elements in a list and display only 2 digit nos from it
n=int(input("Enter the no. of elements: "))
l=[]
l1=[]
for i in range(n):
    x=int(input("Enter element: "))
    l.append(x)
for i in l:
    if i>=10 and i<=99:
        l1.append(i)
print("Two digit nos are",l1)