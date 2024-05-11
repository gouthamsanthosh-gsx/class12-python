'''
Prototype: <LIBRARY MANAGEMENT>
Status: Final stage
Submission date: 28/10/2022
Developers: Alffin Poly, Adwaith Naveen, Goutham Santhosh
'''
#Modules
import pickle
import webbrowser
from tkinter import *
from tkinter import messagebox
from datetime import timedelta, date

#Functions
def register():
	'''Add student record'''
	f = open("registration.dat","ab+")
	f.seek(0)
	records = []
	try:
	    while True:                    
		    records = (pickle.load(f))
	except EOFError:
	      f.close()
	RN = int(input("Enter Registration No: "))
	N = input("Enter Name: ")
	D = input("Enter Class: ")
	S = input("Enter Section: ")
	P = input("Create New Password: ")
	data = [RN,N,D,S,P]
	records.append(data)
	
	f = open("registration.dat","wb")
	pickle.dump(records,f)
	f.close()
	print("Registered")

def loginpage():
    root = Tk()
    root.geometry("800x220")
    root.title("Login")
    root.configure(background="light blue")
    # Creating a label widget
    myLabel = Label(root, text= "Library Mangement System", fg="Dark blue", bg="light blue", width="50", height="2", font="algerian 14 ")
    # Displaying it on screen
    myLabel.grid(row=0, column=1,)
    # Creating a enter widget (text box)
    e = Entry(root,width=15, bg= "white")
    e.grid(row=1 , column =1, sticky="w")
    e1 = Entry(root,width=15, bg= "white")
    e1.grid(row=3 , column =1, sticky= "w")
     # Creating a label widget
    myLabel1 = Label(root, text= "Reg No: ", bg="light blue")
    # Displaying it on screen
    myLabel1.grid(row=1, column=0, sticky="w") 
    # Creating a label widget
    myLabel2 = Label(root, text= "Password: ", bg="light blue")
    # Displaying it on screen
    myLabel2.grid(row=3, column=0, sticky="w")
    def Reg_No():
        global c
        c = e.get()
        rn= "Registration No: " + str(c)
        regno = Label(root, text= rn)
        # Displaying it on screen
        regno.grid(row=2, column=0)
    def Pass_No():
        global p
        p = e1.get()
        P= "Password: " + str(p)
        regno = Label(root, text= P)
        # Displaying it on screen
        regno.grid(row=4, column=0, sticky="w")
    # Creating a button widget
    myButton = Button(root, text="Enter", command=Reg_No, padx=5, pady=5, fg="blue", bg="light blue")
    myButton1 = Button(root, text="Enter", command=Pass_No, padx=5, pady=5, fg="blue", bg="light blue")
    # Displaying it on screen
    myButton.grid(row=1, column=2)
    myButton1.grid(row=3, column=2)
    button_quit= Button(root, text="Click Here!!", command=root.destroy, padx=4, pady=4, fg="white", bg="blue")
    button_quit.grid(row=5, column=1)
    root.mainloop()

def incorrectp():
	'''Incorrect password message'''
	root = Tk()
	root.withdraw()
	def errormsg():
		messagebox.showerror("Invalid Login","Incorrect Password!")
	errormsg()
	root.destroy()
	root.mainloop()

def incorrectregno():
	'''Incorrect registration no. message'''
	root = Tk()
	root.withdraw()
	def errormsg():
		messagebox.showerror("Invalid Reg No.!","Registration No. does not exist")
	errormsg()
	root.destroy()
	root.mainloop()

def success():
	'''Successful login message'''
	root = Tk()
	root.withdraw()
	def Lsuccessmsg():
		messagebox.showinfo("Logged In","Log in Successful")
	Lsuccessmsg()
	root.destroy()
	root.mainloop()

def login():
	ch = input("Registered user? Y/N: ")
	if ch in "nN":
		register()
		login()
	else:
		print ("Login with your respective Registration No.")
		loginpage()
		with open("registration.dat", 'rb') as f1:
			try:
				rec = pickle.load(f1)
			except:
				pass
			stud_exists = False
			for i in rec:
				if i[0] == int(c):
					stud_exists = True
					passwd = i[4]
			if stud_exists:
				if p == passwd:
					success()
					print("Log in Successful")
				else:
					incorrectp()
					print("Incorrect passsword!")
					tr =input("Try again Y/N: ")
					if tr in 'Yy':
						login()
					else:
						print("Exit")
						exit()
			else:
				incorrectregno()
				tr = input("Try again Y/N: ")
				if tr in 'Yy':
					login()
				else:
					print("Exit")
					exit()

def draw_box(s):
	'''Print line(s) inside a box. The lines has to be passed into the function
	as a list'''
	l = 0 #Length of the box
	#Calculate the length of the biggest line
	for i in s:
		if len(i) > l:
			l = len(i)
	l += 1
	#Printing box
	print("\n✯" + "✯"*(l+1) + "✯")
	for i in s:
		print("✯ " + i + " "*(l-len(i)) + "✯")
	print("✯" + "✯"*(l+1) + "✯")

print("*"*130)
draw_box(["WELCOME TO LIBRARY MANAGEMENT SOFTWARE"])

def draw_table1(x):
	'''Draws a table. Each row has to be passed as a list/tuple inside a main list(nested list/tuple)'''
	t = tuple(x)
	cell_width = []
	for i in range(len(t[0])):
		cell_width.append(0)
	for row in t:
		for i in range(len(row)):
			if len(str(row[i])) > cell_width[i]:
				cell_width[i] = len(str(row[i]))
	total_width = 3*len(cell_width)
	for i in cell_width:
		total_width += i
	print("+","-"*(total_width),"+",sep='')
	for i in range(len(t)):
		x = "| "
		row = t[i]
		for j in range(len(row)):
			x += " " + str(row[j]) + " "*(cell_width[j]-len(str(row[j]))) + " |"
		print(x)
		if i == 0 or i == len(t)-1:
			print("+","-"*(total_width),"+",sep='')

def view():
	f = open("books.dat","ab+")
	a = [["ID","Name","Category","Author","Publisher","Price","Availability"]]
	f.seek(0)
	try:
		while True:
			r= pickle.load(f)
			a.append(r)
	except EOFError:
		f.close()
	draw_table1(a)

def add():
	f = open("books.dat","ab+")
	id_list = [] #To prevent duplicate book ID
	while True:
		BKID = int(input("\nEnter Book ID: "))
		bk_exists = False
		try:
			f.seek(0)
			#Check whether the book exists in file
			while True:
				if pickle.load(f)[0] == BKID:
					bk_exists = True
		except EOFError:
			pass #Don't close the file here!. Pass -> nothing(dummy statement)
		#Check whether BKID already exists
		if BKID in id_list:
			bk_exists = True

		if bk_exists:
			print("A book with same ID already exists!")
		else:
			id_list.append(BKID)
			BN = input("Enter Book name: ")
			CAT = input("Enter Category: ")
			AUTH = input("Enter Author: ")
			PUB = input("Enter Publisher: ")
			PRICE = float(input("Enter Price: "))
			STAT = input("Enter Status (a/na): ")
			d = [BKID,BN,CAT,AUTH,PUB,PRICE,STAT]
			pickle.dump(d,f)
			ch = input("Add more records? (y/n): ")
			if ch in "nN":
				break
	f.close()

def search():
	while True:
		print("CHOICE")
		print("1. Search by Book ID")
		print("2. Search by Book Name")
		print("3. Search by Category")
		print("4. Search by Author")
		print("5. Search by Publisher")
		print("6. Return")
		ch = int(input("Enter your choice: "))
		if ch == 1:
			s = int(input("Enter Book ID: "))
			f = open("books.dat","rb")
			l = [["ID","Name","Category","Author","Publisher","Price","Status"]]
			bk_exists = False
			try:
				while True:
					rec = pickle.load(f)
					if rec[0] == s: #Book ID is unique
						bk_exists = True
						l.append(rec)
			except EOFError:
				f.close()
			if bk_exists:
				print("\nBooks with ID:",s)
				draw_table1(l)
			else:
				print("Couldn't find the book(s)!")
		elif ch == 2:
			s = input("Enter Book Name: ")
			f = open("books.dat","rb")
			l = [["ID","Name","Category","Author","Publisher","Price","Status"]]
			bk_exists = False
			try:
				while True:
					rec = pickle.load(f)
					if s.lower() in rec[1].lower():
						bk_exists = True
						l.append(rec)
			except EOFError:
				f.close()
			if bk_exists:
				print("\nBooks with Name:",s)
				draw_table1(l)
			else:
				print("Couldn't find the book(s)!")
		elif ch == 3:
			s = input("Enter Category: ")
			f = open("books.dat","rb")
			l = [["ID","Name","Category","Author","Publisher","Price","Status"]]
			bk_exists = False
			try:
				while True:
					rec = pickle.load(f)
					if s.lower() in rec[2].lower():
						bk_exists = True
						l.append(rec)
			except EOFError:
				f.close()
			if bk_exists:
				print("\nBooks in Category:",s)
				draw_table1(l)
			else:
				print("Couldn't find the book(s)!")
		elif ch == 4:
			s = input("Enter Author's Name: ")
			f = open("books.dat","rb")
			l = [["ID","Name","Category","Author","Publisher","Price","Status"]]
			bk_exists = False
			try:
				while True:
					rec = pickle.load(f)
					if s.lower() in rec[3].lower():
						bk_exists = True
						l.append(rec)
			except EOFError:
				f.close()
			if bk_exists:
				print("\nBooks written by:",s)
				draw_table1(l)
			else:
				print("Couldn't find the book(s)!")
		elif ch == 5:
			s = input("Enter Publisher's Name: ")
			f = open("books.dat","rb")
			l = [["ID","Name","Category","Author","Publisher","Price","Status"]]
			bk_exists = False
			try:
				while True:
					rec = pickle.load(f)
					if s.lower() in rec[4].lower():
						bk_exists = True
						l.append(rec)
			except EOFError:
				f.close()
			if bk_exists:
				print("\nBooks published by:",s)
				draw_table1(l)
			else:
				print("Couldn't find the book(s)!")
		else:
			break

def delete():
	BKID = int(input("Book ID to be deleted: "))
	f = open("books.dat","rb+")
	bk_exists = False
	a = [["ID","Name","Category","Author","Publisher","Price","Availability"]]
	books = []
	try:
		while True:
			rec = pickle.load(f)
			if rec[0] == BKID:
				bk_exists = True
				a.append(rec)
			else:
				books.append(rec)
	except EOFError:
		f.close()
	if bk_exists:
		print("\nBook to be deleted")
		draw_table1(a)
		ch = input("Do you want to delete this book?(y/n): ")
		if ch in "yY":
			f = open("books.dat","wb")
			for rec in books:
				pickle.dump(rec,f)
			f.close()
			print("Book deleted")
	else:
		print("This Book ID doesn't exist!")

def update():
	BKID = int(input("Enter book ID that needs to be updated: "))
	f = open("books.dat","rb")
	c = 0
	index = 0
	books = []
	bk_exists = False
	try:
		while True:
			rec = pickle.load(f)
			books.append(rec)
			if rec[0] == BKID:
				index = c
				bk_exists = True
			c += 1
	except EOFError:
		f.close()

	if bk_exists:
		books[index][1] = input("Updated book name: ")
		books[index][2] = input("Updated category: ")
		books[index][3] = input("Updated author's name: ")
		books[index][4] = input("Updated publisher's name: ")
		books[index][5] = float(input("Updated price: "))
		books[index][6] = input("Updated status(a/na): ")
		f = open("books.dat","wb")
		for book in books:
			pickle.dump(book,f)
		f.close()
	else:
		#If the book is not there in the file
		print("This book ID doesn't exist!")

def Studentreg():
	f= open("Student Reg.dat","ab+")
	a = [["Student ID","Student Name"," Class","Section","Borrowed Book ID","Borrowed Book","No. of Days","Borrowed Date","Return Date","Returned On","Fine"]]
	f.seek(0)
	try:
		while True:
			r= pickle.load(f)
			a.append(r)
	except EOFError:
		f.close()
	draw_table1(a)

def borrow():
	f= open("Student Reg.dat","ab+")
	f.seek(0)
	# To get Student Id and Name from Registration.dat
	with open("registration.dat", 'rb') as f1:
			try:
				rec = pickle.load(f1)
			except:
				pass
			stud_exists = False
			for i in rec:
				if i[0] == int(c):
					stud_exists = True
					SID=int(c)
					SN,C,D=i[1],i[2],i[3]
					passwd = i[4]
			if stud_exists:
				if p == passwd:
					f1.close()
	# To check if Book Id is available from Books.dat
	with open("books.dat","rb") as f2:
		bk_exists = False
		BID = int(input("Enter Book ID: "))
		try:
			while True :
				rec1 = pickle.load(f2)
				if rec1[0]== BID and rec1[6] in 'Aa':
					bk_exists = True
					BB = input("Enter Book name: ")
					NOD= int(input("No. of days borrowed for: "))
					F= "NA"
					RO= "NA"
					BD= date.today()
					RD= BD + timedelta(days=NOD)
					d=[SID,SN,C,D,BID,BB,NOD,BD,RD,RO,F]
					pickle.dump(d,f)
					print("Book Borrowed")
					break
		except EOFError:
			f2.close()

	if bk_exists:
			f.close()
	else:
		print("Book ID does not exist/available!")

def cbrb():
	f = open("Student Reg.dat","rb")
	a = [["Borrowed Book ID","Borrowed Book / Returned Book","Return Date"]]
	bk_exists=False
	try:
		while True:
			r= pickle.load(f)
			if r[0]== int(c):
				bk_exists = True
				d=[r[4],r[5],r[8]]
				a.append(d)
	except EOFError:
		f.close()
	if bk_exists:
		draw_table1(a)
	else:
		print("No Borrowed or Returned Books !")

def Return():
    f = open("Student Reg.dat","rb")
    bk_to_rtn = False
    records = []
    t = [["Book ID","Book Name","Return Date","Returned On","Fine"]]
    try:
        while True:
            r = pickle.load(f)
            if r[0] == int(c):
                bk_to_rtn = True
                r[9] = date.today()
                if r[10] == "NA":
                    r[10] = 0
                else:
                    if r[9] > r[8]:
                        r[10] += 100
                t.append((r[4],r[5],r[8],r[9],r[10]))
            records.append(r)
    except:
        f.close()
    if bk_to_rtn:
        draw_table1(t)
        print("Book Returned")
        f = open("Student Reg.dat","wb")
        for record in records:
            pickle.dump(record,f)
        f.close()
    else:
        print("No book to return")
def fine():
	f = open("Student Reg.dat","rb")
	a = [["Borrowed Book ID","Borrowed Book","Return Date","Returned On","Fine"]]
	bk_exists=False
	try:
		while True:
			r= pickle.load(f)
			if r[0]== int(c):
				bk_exists = True
				d=[r[4],r[5],r[8],r[9],r[10]]
				a.append(d)
	except EOFError:
		f.close()
	if bk_exists:
		draw_table1(a)
	else:
		print("No Borrowed or Returned Books !")

def Eresource():
    root = Tk()
    root.geometry("800x220")
    root.title("E RESOURCE")
    root.configure(background="orange")
    # Creating a label widget
    myLabel = Label(root, text= "E RESOURCE - NCERT TEXTBOOKS", fg="Purple", bg="orange", width="50", height="2", font="algerian 14 underline")
    # Displaying it on screen
    myLabel.grid(row=0, column=1,)
    # Creating a enter widget (text box)
    e = Entry(root,width=15, bg= "white")
    e.grid(row=1 , column =1, sticky="w")
    e1 = Entry(root,width=15, bg= "white")
    e1.grid(row=3 , column =1, sticky= "w")
    # Creating a label widget
    myLabel1 = Label(root, text= "Class: ", fg="Purple", bg="orange", font=('Times New Roman',10,'bold'))
    # Displaying it on screen
    myLabel1.grid(row=1, column=0, sticky="w") 
    # Creating a label widget
    myLabel2 = Label(root, text= "Subject: ", fg="Purple",bg="orange", font=('Times New Roman',10,'bold'))
    # Displaying it on screen
    myLabel2.grid(row=3, column=0, sticky="w")
    def Class():
        global d
        d = e.get()
        rn= "Class: " + str(d)
        regno = Label(root, text= rn)
        # Displaying it on screen
        regno.grid(row=2, column=0, sticky="w")
    def Subject():
        global s
        s = e1.get()
        P= "Subject:  " + str(s)
        regno = Label(root, text= P)
        # Displaying it on screen
        regno.grid(row=4, column=0, sticky="w")
    # Creating a button widget
    myButton = Button(root, text="Enter", command=Class, padx=5, pady=5, fg="white", bg="purple")
    myButton1 = Button(root, text="Enter", command=Subject, padx=5, pady=5, fg="white", bg="purple")
    # Displaying it on screen
    myButton.grid(row=1, column=2,)
    myButton1.grid(row=3, column=2)
    button_quit= Button(root, text="Find Text", command=root.destroy, padx=4, pady=4, fg="white", bg="purple")
    button_quit.grid(row=5, column=1)
    root.mainloop()

def websites():
    root = Tk()
    root.geometry("900x200")
    root.title("NCERT TEXTBOOKS")
    root.configure(background="light green")
    # Creating a label widget
    myLabel = Label(root, text= "NCERT " + "CLASS " + d + " " + s.upper() + " TEXT BOOK", fg="green", bg="light green", width="50", height="2", font="algerian 22 ")
    # Displaying it on screen
    myLabel.grid(row=0, column=1,)    
    def Eng12(e):     
       # Creating a label widget
       myLabel3 = Label(root, text= "Click Here for Class 12 NCERT ENGLISH TEXT !!", bg="light green")
       # Displaying it on screen
       myLabel3.grid(row=2, column=1,)       
       myLabel3.bind("<Button-1>", Eng12)  
       webbrowser.open_new("https://ncert.nic.in/textbook.php?lefl1=0-14") 
    def Chem12(e):     
       # Creating a label widget
       myLabel3 = Label(root, text= "Click Here for Class 12 NCERT CHEMISTRY TEXT !!", bg="light green")
       # Displaying it on screen
       myLabel3.grid(row=2, column=1,)       
       myLabel3.bind("<Button-1>", Chem12)  
       webbrowser.open_new("https://ncert.nic.in/textbook.php?lech1=0-9") 
    def Phy12(e):     
       # Creating a label widget
       myLabel3 = Label(root, text= "Click Here for Class 12 NCERT PHYSICS TEXT !!", bg="light green")
       # Displaying it on screen
       myLabel3.grid(row=2, column=1,)       
       myLabel3.bind("<Button-1>", Phy12)  
       webbrowser.open_new("https://ncert.nic.in/textbook.php?leph1=0-8") 
    def CS12(e):     
       # Creating a label widget
       myLabel3 = Label(root, text= "Click Here for Class 12 NCERT COMPUTER SCIENCE TEXT !!", bg="light green")
       # Displaying it on screen
       myLabel3.grid(row=2, column=1,)       
       myLabel3.bind("<Button-1>", CS12)  
       webbrowser.open_new("https://ncert.nic.in/textbook.php?lecs1=0-13") 
    def Maths12(e):     
       # Creating a label widget
       myLabel3 = Label(root, text= "Click Here for Class 12 NCERT MATHS TEXT !!", bg="light green")
       # Displaying it on screen
       myLabel3.grid(row=2, column=1,)       
       myLabel3.bind("<Button-1>", Maths12)  
       webbrowser.open_new("https://ncert.nic.in/textbook.php?lemh1=0-6")
    def Eng11(e):     
       # Creating a label widget
       myLabel3 = Label(root, text= "Click Here for Class 11 NCERT ENGLISH TEXT !!", bg="light green")
       # Displaying it on screen
       myLabel3.grid(row=2, column=1,)       
       myLabel3.bind("<Button-1>", Eng11)  
       webbrowser.open_new("https://ncert.nic.in/textbook.php?kehb1=0-14") 
    def Chem11(e):     
       # Creating a label widget
       myLabel3 = Label(root, text= "Click Here for Class 11 NCERT CHEMISTRY TEXT !!", bg="light green")
       # Displaying it on screen
       myLabel3.grid(row=2, column=1,)       
       myLabel3.bind("<Button-1>", Chem11)  
       webbrowser.open_new("https://ncert.nic.in/textbook.php?kech1=0-7") 
    def Phy11(e):     
       # Creating a label widget
       myLabel3 = Label(root, text= "Click Here for Class 11 NCERT PHYSICS TEXT !!", bg="light green")
       # Displaying it on screen
       myLabel3.grid(row=2, column=1,)       
       myLabel3.bind("<Button-1>", Phy11)  
       webbrowser.open_new("https://ncert.nic.in/textbook.php?keph1=0-8") 
    def CS11(e):     
       # Creating a label widget
       myLabel3 = Label(root, text= "Click Here for Class 11 NCERT COMPUTER SCIENCE TEXT !!", bg="light green")
       # Displaying it on screen
       myLabel3.grid(row=2, column=1,)       
       myLabel3.bind("<Button-1>", CS11)  
       webbrowser.open_new("https://ncert.nic.in/textbook.php?kecs1=0-11") 
    def Maths11(e):     
       # Creating a label widget
       myLabel3 = Label(root, text= "Click Here for Class 11 NCERT MATHS TEXT !!", bg="light green")
       # Displaying it on screen
       myLabel3.grid(row=2, column=1,)       
       myLabel3.bind("<Button-1>", Maths11)  
       webbrowser.open_new("https://ncert.nic.in/textbook.php?kemh1=0-16") 
    def Eng10(e):     
       # Creating a label widget
       myLabel3 = Label(root, text= "Click Here for Class 10 NCERT ENGLISH TEXT !!", bg="light green")
       # Displaying it on screen
       myLabel3.grid(row=2, column=1,)       
       myLabel3.bind("<Button-1>", Eng10)  
       webbrowser.open_new("https://ncert.nic.in/textbook.php?iebe1=0-11") 
    def Science10(e):     
       # Creating a label widget
       myLabel3 = Label(root, text= "Click Here for Class 10 NCERT SCIENCE TEXT !!", bg="light green")
       # Displaying it on screen
       myLabel3.grid(row=2, column=1,)       
       myLabel3.bind("<Button-1>", Science10)  
       webbrowser.open_new("https://ncert.nic.in/textbook.php?jesc1=0-16") 
    def SS10(e):     
       # Creating a label widget
       myLabel3 = Label(root, text= "Click Here for Class 10 NCERT SOCIAL SCIENCE TEXT !!", bg="light green")
       # Displaying it on screen
       myLabel3.grid(row=2, column=1,)       
       myLabel3.bind("<Button-1>", SS10)  
       webbrowser.open_new("https://ncert.nic.in/textbook.php?jess1=0-7") 
    def Hin10(e):     
       # Creating a label widget
       myLabel3 = Label(root, text= "Click Here for Class 10 NCERT HINDI TEXT !!", bg="light green")
       # Displaying it on screen
       myLabel3.grid(row=2, column=1,)       
       myLabel3.bind("<Button-1>", Hin10)  
       webbrowser.open_new("https://ncert.nic.in/textbook.php?jhks1=0-17") 
    def Maths10(e):     
       # Creating a label widget
       myLabel3 = Label(root, text= "Click Here for Class 10 NCERT MATHS TEXT !!", bg="light green")
       # Displaying it on screen
       myLabel3.grid(row=2, column=1,)       
       myLabel3.bind("<Button-1>", Maths10)  
       webbrowser.open_new("https://ncert.nic.in/textbook.php?jemh1=0-15")
    if d =="12" and s.upper() == "ENGLISH":
       myButton3 = Button(root, text="Open Browser", command=lambda: Eng12(1), padx=5, pady=5, fg="blue", bg="cyan")
       # Displaying it on screen
       myButton3.grid(row=1, column=1)
    elif d =="12" and s.upper() == "CHEMISTRY":
        myButton3 = Button(root, text="Open Browser", command=lambda: Chem12(1), padx=5, pady=5, fg="blue", bg="cyan")
        # Displaying it on screen
        myButton3.grid(row=1, column=1)
    elif d =="12" and s.upper() == "PHYSICS":
        myButton3 = Button(root, text="Open Browser", command=lambda: Phy12(1), padx=5, pady=5, fg="blue", bg="cyan")
        # Displaying it on screen
        myButton3.grid(row=1, column=1)
    elif d =="12" and s.upper() == "CS":
        myButton3 = Button(root, text="Open Browser", command=lambda: CS12(1), padx=5, pady=5, fg="blue", bg="cyan")
        # Displaying it on screen
        myButton3.grid(row=1, column=1)
    elif d =="12" and s.upper() == "MATHS":
        myButton3 = Button(root, text="Open Browser", command=lambda: Maths12(1), padx=5, pady=5, fg="blue", bg="cyan")
        # Displaying it on screen
        myButton3.grid(row=1, column=1)
    elif d =="11" and s.upper() == "ENGLISH":
       myButton3 = Button(root, text="Open Browser", command=lambda: Eng11(1), padx=5, pady=5, fg="blue", bg="cyan")
       # Displaying it on screen
       myButton3.grid(row=1, column=1)
    elif d =="11" and s.upper() == "CHEMISTRY":
        myButton3 = Button(root, text="Open Browser", command=lambda: Chem11(1), padx=5, pady=5, fg="blue", bg="cyan")
        # Displaying it on screen
        myButton3.grid(row=1, column=1)
    elif d =="11" and s.upper() == "PHYSICS":
        myButton3 = Button(root, text="Open Browser", command=lambda: Phy11(1), padx=5, pady=5, fg="blue", bg="cyan")
        # Displaying it on screen
        myButton3.grid(row=1, column=1)
    elif d =="11" and s.upper() == "CS":
        myButton3 = Button(root, text="Open Browser", command=lambda: CS11(1), padx=5, pady=5, fg="blue", bg="cyan")
        # Displaying it on screen
        myButton3.grid(row=1, column=1)
    elif d =="11" and s.upper() == "MATHS":
        myButton3 = Button(root, text="Open Browser", command=lambda: Maths11(1), padx=5, pady=5, fg="blue", bg="cyan")
        # Displaying it on screen
        myButton3.grid(row=1, column=1)
    elif d =="10" and s.upper() == "ENGLISH":
       myButton3 = Button(root, text="Open Browser", command=lambda: Eng10(1), padx=5, pady=5, fg="blue", bg="cyan")
       # Displaying it on screen
       myButton3.grid(row=1, column=1)
    elif d =="10" and s.upper() == "SCIENCE":
        myButton3 = Button(root, text="Open Browser", command=lambda: Science10(1), padx=5, pady=5, fg="blue", bg="cyan")
        # Displaying it on screen
        myButton3.grid(row=1, column=1)
    elif d =="10" and s.upper() == "SS":
        myButton3 = Button(root, text="Open Browser", command=lambda: SS10(1), padx=5, pady=5, fg="blue", bg="cyan")
        # Displaying it on screen
        myButton3.grid(row=1, column=1)
    elif d =="10" and s.upper() == "HINDI":
        myButton3 = Button(root, text="Open Browser", command=lambda: Hin10(1), padx=5, pady=5, fg="blue", bg="cyan")
        # Displaying it on screen
        myButton3.grid(row=1, column=1)
    elif d =="10" and s.upper() == "MATHS":
        myButton3 = Button(root, text="Open Browser", command=lambda: Maths10(1), padx=5, pady=5, fg="blue", bg="cyan")
        # Displaying it on screen
        myButton3.grid(row=1, column=1)
    else: 
       root.geometry("650x100")
       myLabel.destroy()
       myLabelq = Label(root, text= "TEXT IS NOT AVAILABLE!!", bg="light green",  fg="Purple", width="50", height="2", font="algerian 16 ")
       # Displaying it on screen
       myLabelq.grid(row=2, column=1,) 
       tr =input("Try again Y/N: ")
       if tr in 'Yy':
            Eresource()
       else:
            print("Exit")
            root.destroy()
            exit()          
    button_quit1= Button(root, text="Exit!!", command=root.quit, padx=5, pady=5, fg="blue", bg="cyan")
    button_quit1.grid(row=3, column=1)
    root.mainloop()

def choice1():
	while True:
		print("1. View Books")
		print("2. Add a Book")
		print("3. Update a Book")
		print("4. Search for a book")
		print("5. Delete a Book")
		print("6. Student Records")
		print("7. E-RESOURCE")
		print("8. Exit")
		ch= int(input("Enter your choice: "))
		if ch==1:
			view()
		elif ch==2:
			add()
		elif ch==3:
			update()
		elif ch==4:
			search()
		elif ch==5:
			delete()
		elif ch==6:
			Studentreg()
		elif ch==7:
			Eresource()
			websites()
		else:
			print("Thank you for using our Library Management System")
			break

def choice():
	while True:
		print("1. View Books")
		print("2. Search for a book")
		print("3. Borrow a Book")
		print("4. Return a Book")
		print("5. Currently Borrowed and Returned Books")
		print("6. Late Return/Fine")
		print("7. E-RESOURCE")
		print("8. Exit")
		ch= int(input("Enter Choice: "))
		if ch==1:
			view()
		elif ch==2:
			search()			
		elif ch==3:
			borrow()
		elif ch==4:
			pass
			Return()
		elif ch==5:
			cbrb()
		elif ch==6:
			pass
			fine()
		elif ch==7:
			Eresource()
			websites()
		else:
			print("Thank you for using our Library Management System ☺")
			break

def acode():
	code = int(input("Enter Admin Code: "))
	if code == 1928:
		login()
		print("*"*130)		
		choice1()
	else:
		print("Incorrect Password")
		ch2= input("Try Again? Y/N: ")
		if ch2 in "Yy":
			acode()
		else:
			person()

def person():
	ch= 0
	print("1. Admin (Pass-1928)")
	print("2. Student")
	ch= int(input("Enter Input: "))
	if ch==1:
		acode()
	else:
		login()
		print("*"*130)		
		choice()

person()
print("*"*130)
draw_box(["Done By:","Alffin","Adwaith","Goutham"])
