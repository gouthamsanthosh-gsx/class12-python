n=int(input("Enter limit: "))
t=()
for i in range(n):
    x=int(input("Enter element: "))
    t+=(x,)

l=list(t)
d=int(input("Index to be deleted:"))
l.pop(d)
t=tuple(l)
print("New tuple:",t)