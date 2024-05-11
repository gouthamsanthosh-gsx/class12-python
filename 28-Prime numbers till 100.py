#prg to display all the prime numbers till 100
#2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
for j in range(1,101):
    c=0
    for i in range(1,j+1):
        if j%i==0:
            c+=1
    if c==2:
        print(j,end=',')