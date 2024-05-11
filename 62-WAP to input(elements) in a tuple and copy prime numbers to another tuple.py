n=int(input("Enter limit: "))
t=()
t1=()
for i in range(n):
    x=int(input("Enter element: "))
    t+=(x,)

for i in t:
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        t1+=(i,)
print("Prime numbers:",t1)