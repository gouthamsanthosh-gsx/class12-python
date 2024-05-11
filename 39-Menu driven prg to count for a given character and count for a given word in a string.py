#Menu driven prg to
#1. Count for a given character
#2. Count for a given word in a string
print('Select choice')
print('1. Count for a given character')
print('2. Count for a given word in a string')
print('3. End program')
s=input('Enter a string:')
s1=s.split()

while True:
    c=0
    ch=int(input('Your choice:'))
    if ch==1:
        gc=input('Enter character to count for:')
        for i in s:
            if i==gc:
                c+=1
        print("Number of",gc,"in",s,"is",c)
    elif ch==2:
        gw=input('Enter the word to count for:')
        for j in s1:
            if j==gw:
                c+=1
        print('Number of',gw,"in",s,"is",c)
    elif ch==3:
        break
    else:
        print('Wrong choice!')