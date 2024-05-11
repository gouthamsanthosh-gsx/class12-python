# Prg to display the perfect square numbers till 100 eg.4,9,16,25,36
for i in range(1,101):
    x=i**2
    for j in range(1,101):
        if x==j:
            print(j,end=" ")