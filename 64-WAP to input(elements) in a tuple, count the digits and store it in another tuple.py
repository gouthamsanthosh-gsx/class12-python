n=int(input("Enter limit: "))
t=()
t1=()
for i in range(n):
    x=int(input("Enter element: "))
    t+=(x,)

for i in t:
    c=0
    while i>0:
        r=i%10
        i//=10
        c+=1
    t1+=(c,)
print("\nNumbers -> Digits")
for i in range(len(t1)):
    print(t[i],"->",t1[i])