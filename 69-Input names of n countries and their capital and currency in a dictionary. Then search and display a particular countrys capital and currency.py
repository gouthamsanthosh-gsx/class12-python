#WAP to input names of n countries and their capital and currency in a dictionary. Then search and display a particular country's capital and currency
n=int(input("Total entries: "))
d=dict()
for i in range(n):
    name=input("\nEnter country name: ")
    capital=input("Enter capital: ")
    currency=input("Enter currency: ")
    d[name]=[capital,currency]

s=input("\nCountry to be searched: ")
if s in d.keys():
    l=d[s]
    print("Country-",s,", Capital-",l[0],", Currency-",l[1])
else:
    print("Data not found!")