#Menu driven prg to
#1. Reverse a string
#2. Check for palindrome or not
print('Choose an option:')
print('1. Reverse a string')
print('2. Check for palindrome or not')
print('3. End program')
s=input('Enter a string:')
s1=s.lower()
n=(len(s))-1
while True:
    fs='' #final string
    ch=int(input('Your choice:'))
    if ch==1:
      for i in range(n,-1,-1):
          r=s[i]
          fs+=r
      print("Reverse string is",fs)
    elif ch==2:
        for i in range(n,-1,-1):
          r=s1[i]
          fs+=r
        if fs==s1:
            print('Yes it is pallindrome')
        else:
            print('No it is not pallindrome')
    elif ch==3:
        break
    else:
        print('Wrong choice')