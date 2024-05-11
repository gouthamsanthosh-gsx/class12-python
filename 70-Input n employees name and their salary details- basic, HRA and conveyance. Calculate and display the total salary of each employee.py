#WAP to input n employees name and their salary details- basic, HRA and conveyance. Calculate and display the total salary of each employee
n=int(input("Total entries: "))
d=dict()
for i in range(n):
    name=input("\nEmployee name: ")
    basic=int(input("Enter basic: "))
    hra=int(input("Enter HRA: "))
    conveyance=int(input("Enter conveyance: "))
    d[name]=[basic,hra,conveyance]

#Print output
print("\nEmployee Salary Details\n************************")
print("Name\tBasic\tHRA\tConveyance\tTotal")
for i in d.keys():
    l=d[i]
    print(i,"\t",l[0],"\t",l[1],"\t",l[2],"\t\t",l[0]+l[1]+l[2])