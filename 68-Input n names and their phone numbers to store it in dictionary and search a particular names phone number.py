#WAP to input n names and their phone numbers to store it in dictionary and search a particular name's phone number
n=int(input("Total entries: "))
d=dict()
for i in range(n):
    name=input("\nEnter name: ")
    number=int(input("Enter phone number: "))
    d[name]=number

#Search
s=input("\nName to be searched: ")
if s in d.keys():
    print("Phone number of",s,"is",d[s])