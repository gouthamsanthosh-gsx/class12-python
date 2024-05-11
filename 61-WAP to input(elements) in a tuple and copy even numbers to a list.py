n=int(input("Enter limit: "))
t=()
for i in range(n):
    x=int(input("Enter element: "))
    t+=(x,)
l=[]
for i in t:
    if i%2==0:
        l.append(i)
print("Even numbers:",l)