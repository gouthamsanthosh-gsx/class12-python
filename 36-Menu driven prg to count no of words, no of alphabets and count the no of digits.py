#Write a menu driven prg to:
#1.Count no.of words
#2.Count the no.of alphabets
#3.Count the no.of digits
#4.Exit from program
s=input('Enter a string:')

while True:
    c=0
    print('\n1.Count no.of words')
    print('2.Count the no.of alphabets')
    print('3.Count the no.of digits')
    print('4.Exit from program')
    ch=int(input('You choice:'))

    if ch==1: #Count no.of words
        s1=s.split()
        for i in s1:
            c+=1
        print('Number of words in',s,"=",c)

    elif ch==2: #Count no.of alphabets
        for i in s:
            if i.isalpha():
                c+=1
        print('Number of alphabets in',s,'=',c)

    elif ch==3: #Count the no.of digits
        for i in s:
            if i.isdigit():
                c+=1
        print('Number of digits in',s,'=',c)
        
    elif ch==4: #Exit from program
        print('Program stopped!')
        break

    else:
        print('Wrong Choice!')