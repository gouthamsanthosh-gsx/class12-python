#WAP to create a dictionary with following parameters- Adm.No, Name, Age, Ph.No
#Write a menu driven prg to do the following:
'''
1. enter
2. update
3. delete a record with a specific key entered by the user
4. search the details of a particular Adm.No
5. exit
'''
print("Select an option")
print("1. Add new record")
print("2. Update an existing record")
print("3. Delete record")
print("4. Search record")
print("5. Show all records")
print("6. Exit")

d=dict()
while True:
	ch=int(input("\nYour choice: "))
	if ch==1:
		#Add new record
		admno=int(input("Enter Adm.No: "))
		if admno not in d.keys():
			name=input("Enter name: ")
			age=int(input("Enter age: "))
			phno=int(input("Enter Ph.No: "))
			d[admno]=[name,age,phno]
			print(">>Added new record")
		else:
			print(">>There's already another record with the same Adm.No. If you want to update details, use update option")
	elif ch==2:
		#Update an existing record
		admno=int(input("Enter Adm.No of record you want to update: "))
		name=input("Enter new name: ")
		age=int(input("Enter new age: "))
		phno=int(input("Enter new Ph.No: "))
		d1={admno:[name,age,phno]}
		d.update(d1)
		print(">>Record updated")
	elif ch==3:
		#Delete record
		admno=int(input("Enter Adm.No of record to be deleted: "))
		if admno in d.keys():
			d.pop(admno)
			print(">>Record deleted")
		else:
			print(">>There's no record with the given Adm.No")
	elif ch==4:
		#Search record
		admno=int(input("Enter the Adm.No of record you want to search: "))
		if admno in d.keys():
			print(">>Details of Adm.No:",admno)
			l=d[admno]
			print("Name:",l[0])
			print("Age:",l[1])
			print("Ph.No:",l[2])
		else:
			print(">>There's no record with the given Adm.No")
	elif ch==5:
		#Show all records
		if len(d)==0:
			print(">>No records available")
		else:
			print(">>Total records:",len(d))
			for j in d:
				l=d[j]
				print("\nAdm.No:",j)
				print("Name:",l[0])
				print("Age:",l[1])
				print("Ph.No:",l[2])
	elif ch==6:
		#Exit from program
		print(">>Exitted from program")
		break
	else:
		print(">>Please input a valid option!")