#Write a menu driven prg to:
#1. find the biggest word
#2. count the 4 letter words
print('Select an option')
print('1. Find the biggest word')
print('2. Count the 4 letter words')
print('3. End program')
s=input('Enter a string:')
s1=s.split()
while True:
    c=0
    lc=0 #longest char
    bw='' #biggest word
    ch=int(input('Your choice:'))
    if ch==1:
        for i in s1:
            l=len(i)
            if l>=lc:
                lc=l
                bw=i
        print('Biggest word is',bw,'and it has',lc,'characters')
    elif ch==2:
        for i in s1:
            if len(i)==4:
                c+=1
        print('No of 4 letter words is',c)
    elif ch==3:
        break
    else:
        print('Wrong choice!')