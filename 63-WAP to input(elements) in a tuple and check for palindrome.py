n=int(input("Enter limit: "))
t=()
for i in range(n):
    x=int(input("Enter element: "))
    t+=(x,)

for i in t:
    nn=0
    i2=i
    while i>0:
        r=i%10
        nn=(nn*10)+r
        i//=10
    if nn==i2:
        print(nn)