#Write a prg to input a string and copy the string into another string after removing vowels
s=input('Enter a string:')
fs='' #final string
vowels='aeiouAEIOU'
for i in s:
    if i not in vowels:
        fs+=i
print(fs)