#Write a menu driven prg to
#1. Count the vowels(both lower and upper case)
#2. Count the words starting with vowel
print('Choose an option')
print('1. Count the vowels(both lower and upper case)')
print('2. Count the words starting with vowel')
print('3. End program')
s=input('Enter a string:')
s1=s.lower()
s2=s1.split()
vowels='aeiou'
while True:
    ch=int(input('Your choice:'))
    c=0
    if ch==1:
        for i in vowels:
            for j in s1:
                if i in j:
                    c+=1
        print("The no. of vowels is",c)
    elif ch==2:
        for i in s2:
            if i[0] in vowels:
                c+=1
        print("No. of words starting with vowels is",c)
    elif ch==3:
        break
    else:
        print('Wrong choice!')