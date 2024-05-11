n=int(input("Enter limit: "))
t=()
for i in range(n):
    x=int(input("Enter element: "))
    t+=(x,)

l=list(t)
l.sort()
t=tuple(l)
print("Sorted tuple:",t)