from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import bcrypt
from database import Database
import mysql.connector as mysql

db = Database()
db.createTable()

class Login:
    '''
    Class for Login
    @param username
    @param password
    '''
    def __init__(self):
        '''
        Class Init Method for GUI
        :params — loginWindow, label, username
        '''
        # Variables for Tkinter
        self.loginWindow = Tk()
        self.loginWindow.title('Login')
        self.loginWindow.geometry('300x250')
        self.label = Label(self.loginWindow, text='Login')
        self.label.place(x=95, y=40)
        # Just Creepy Tkinter Stuff
        self.usernameS = StringVar()
        self.passwordS = StringVar()
        self.usernameE = Entry(self.loginWindow, relief=FLAT, textvariable=self.usernameS)
        self.usernameE.place(x=70, y=80)
        self.passwordE = Entry(self.loginWindow, show='*', relief=FLAT, textvariable=self.passwordS)
        self.passwordE.place(x=70, y=120)
        # Actual Variales
        self.username = self.usernameS.get()
        self.password = self.passwordS.get()
        print(self.password)
        self.submit = Button(self.loginWindow, text='Submit', pady=5, padx=20, command=self.validate)
        self.submit.place(x=100, y=150)

    def checkDatabase(self, username, password):
        con = mysql.connect(host="localhost", user="root", password="root", database="tutorin")
        cursor = con.cursor()

        cursor.execute("SELECT * FROM user WHERE username ='"+username+"'")
        row = cursor.fetchall()
        print(row)
        if row[0][1] == username:
            return row[0][2] == password


    def validate(self):

        username = self.usernameE.get()
        password = self.passwordE.get()

        try :
            if (self.checkDatabase(username, password)):
                messagebox.showinfo('Successful', 'Login was sucessful')
            else :
                messagebox.showerror('Error', 'Wrong Credentials')
        except :
            messagebox.showerror('Error', 'Wrong Credentials')
        

    def run(self):
        self.loginWindow.mainloop()

class RegisterTutor:
    '''
    Class for Register
    @param username
    @param password
    '''
    def __init__(self):
        self.registerWindow = Tk()
        self.registerWindow.title('Register')
        self.registerWindow.geometry('300x800')
        self.label = Label(self.registerWindow, text='Register as Tutor')
        self.label.place(x=110, y=40)
        self.label.pack(side=TOP, padx=70, pady= 10)

        self.usernameS = StringVar()
        self.passwordS = StringVar()
        self.nameS = StringVar()
        self.contactS = StringVar()
        self.addressS = StringVar()

        self.usernameL = Label(self.registerWindow, text="Username", font=(10))
        # self.usernameL.place(x=70, y=90)
        self.usernameL.pack(side=TOP, padx=50)
        self.usernameE = Entry(self.registerWindow, relief=FLAT, textvariable=self.usernameS)
        # self.usernameE.place(x=70, y=110)
        self.usernameE.pack(side=TOP, padx=70)

        self.passwordL = Label(self.registerWindow, text="Password", font=(10))
        # self.passwordL.place(x=70, y=160)
        self.passwordL.pack(side=TOP, padx=70)
        self.passwordE = Entry(self.registerWindow, show='*', relief=FLAT, textvariable=self.passwordS)
        # self.passwordE.place(x=70, y=180)
        self.passwordE.pack(side=TOP, padx=70)

        self.nameL = Label(self.registerWindow, text="Name", font=(10))
        # self.nameL.place(x=70, y=230)
        self.nameL.pack(side=TOP, padx=70)
        self.nameE = Entry(self.registerWindow, relief=FLAT, textvariable=self.nameS)
        # self.nameE.place(x=70, y=250)
        self.nameE.pack(side=TOP, padx=70)

        self.contacL = Label(self.registerWindow, text="Contact", font=(10))
        # self.contacL.place(x=70, y=300)
        self.contacL.pack(side=TOP, padx=70)
        self.contactE = Entry(self.registerWindow, relief=FLAT)
        # self.contactE.place(x=70, y=320)
        self.contactE.pack(side=TOP, padx=70)

        self.addressL = Label(self.registerWindow, text="Address", font=(10))
        # self.addressL.place(x=70, y=370)
        self.addressL.pack(side=TOP, padx=70)
        self.addressE = Entry(self.registerWindow, relief=FLAT)
        # self.addressE.place(x=70, y=390)
        self.addressE.pack(side=TOP, padx=70)

        self.jenjangPendL = Label(self.registerWindow, text="Jenjang Pendidikan", font=(10))
        # self.jenjangPendL.place(x=70, y=420)
        self.jenjangPendL.pack(side=TOP, padx=70)
        self.jenjangPendClicked = StringVar()
        self.jenjangPend = Combobox(self.registerWindow, state="readonly", width = 5, textvariable=self.jenjangPendClicked)
        self.jenjangPend['values'] = ("SD", "SMP", "SMA")
        # self.categ.grid(column=2, row=4)
        self.jenjangPend.current(0)
        # self.jenjangPend.place(x=70, y=440)
        self.jenjangPend.pack(side=TOP, padx=70)

        self.fareS = StringVar()
        self.ktpS = StringVar()
        self.expS = StringVar()
        self.headlineS = StringVar()

        self.fareL = Label(self.registerWindow, text="Fare", font=(10))
        # self.fareL.place(x=70, y=490)
        self.fareL.pack(side=TOP, padx=70)
        self.fareE = Entry(self.registerWindow, relief=FLAT, textvariable=self.fareS)
        # self.fareE.place(x=70, y=510) 
        self.fareE.pack(side=TOP, padx=70) 

        self.ktpL = Label(self.registerWindow, text="KTP", font=(10))
        # self.ktpL.place(x=70, y=560)
        self.ktpL.pack(side=TOP, padx=70)
        self.ktpE = Entry(self.registerWindow, relief=FLAT, textvariable=self.ktpS)
        # self.ktpE.place(x=70, y=580) 
        self.ktpE.pack(side=TOP, padx=70)

        self.expL = Label(self.registerWindow, text="Experience", font=(10))
        # self.ktpL.place(x=70, y=560)
        self.expL.pack(side=TOP, padx=70)
        self.expE = Entry(self.registerWindow, relief=FLAT, textvariable=self.expS)
        # self.ktpE.place(x=70, y=580) 
        self.expE.pack(side=TOP, padx=70)

        self.pendL = Label(self.registerWindow, text="Education", font=(10))
        # self.ktpL.place(x=70, y=560)
        self.pendL.pack(side=TOP, padx=70)
        self.PendClicked = StringVar()
        self.Pend = Combobox(self.registerWindow, state="readonly", width = 5, textvariable=self.PendClicked)
        self.Pend['values'] = ("SMA", "S1", "S2", "S3")
        # self.categ.place(relx=0.1, rely=4)
        self.Pend.current(0)
        # self.Pend.place(x=110, y=60)
        self.Pend.pack(side=TOP)

        self.headlineL = Label(self.registerWindow, text="Headline", font=(10))
        # self.ktpL.place(x=70, y=560)
        self.headlineL.pack(side=TOP, padx=70)
        self.headlineE = Entry(self.registerWindow, relief=FLAT, textvariable=self.headlineS)
        # self.ktpE.place(x=70, y=580) 
        self.headlineE.pack(side=TOP, padx=70)
        
        self.submit = Button(self.registerWindow, text='Submit', pady=5, padx=20, command=self.add)
        # self.submit.place(x=110, y=630)
        self.submit.pack(side=TOP, padx=70, pady=10)
            
        
    def run(self):
        self.registerWindow.mainloop()
    
    def searchData(self, username):
        con = mysql.connect(host="localhost", user="root", password="root", database="tutorin")
        cursor = con.cursor()

        cursor.execute("SELECT * FROM user WHERE username ='"+username+"'")
        row = cursor.fetchall()
        print(row)
        if row == []:
            return 1
        return 0

    def add(self):

        con = mysql.connect(host="localhost", user="root", password="root", database="tutorin")
        cursor = con.cursor()

        id = 1;
        username = self.usernameE.get()
        password = self.passwordE.get()
        name = self.nameE.get()
        contact = self.contactE.get()
        address = self.addressE.get()
        balance = 0
        flag = 0
        rating = 0
        jenjPend = self.jenjangPend.get()
        ktp = self.ktpE.get()
        tarif = self.fareE.get()
        xp = self.expE.get()
        ed = self.Pend.get()
        hl = self.headlineE.get()
        # jenjang =  self.jenjangPend.get()
        # cursor.execute("insert into user values(2,'abc','djdjd','jdjdjd','ddjjdjd','ddjjdjd', 0, 0, 0)")
        # print("('"+ username +"','" + password +"','" + name +"','" + contact +"','" + address, balance, flag, rating +"')")
        if (self.searchData(username)):
            cursor.execute("insert into user(username, password, nama, kontak, alamat) values('"+ username +"','" + password +"','" + name +"','" + contact +"','" + address +"')")
            cursor.execute('commit')
            cursor.execute("insert into tutor(username, jenjang, tarif, noKTP, pengalaman, pendidikan, headline) values('"+ username +"','" + jenjPend +"',"+tarif+",'" + ktp +"','" + xp +"','" + ed +"','"+ hl +"')")
            cursor.execute('commit')
            messagebox.showinfo('Successful', 'Username was added')
        else :
            messagebox.showwarning("Warning", 'Username already exists')

        con.close()

class RegisterMurid:
    '''
    Class for Register
    @param username
    @param password
    '''
    def __init__(self):
        self.registerWindow = Tk()
        self.registerWindow.title('Register')
        self.registerWindow.geometry('300x800')
        self.label = Label(self.registerWindow, text='Register as Murid')
        self.label.place(x=110, y=40)
        self.label.pack(side=TOP, padx=70, pady= 10)
        # Tkinter Stuff

        self.usernameS = StringVar()
        self.passwordS = StringVar()
        self.nameS = StringVar()
        self.contactS = StringVar()
        self.addressS = StringVar()

        self.usernameL = Label(self.registerWindow, text="Username", font=(10))
        # self.usernameL.place(x=70, y=90)
        self.usernameL.pack(side=TOP, padx=50)
        self.usernameE = Entry(self.registerWindow, relief=FLAT, textvariable=self.usernameS)
        # self.usernameE.place(x=70, y=110)
        self.usernameE.pack(side=TOP, padx=70)

        self.passwordL = Label(self.registerWindow, text="Password", font=(10))
        # self.passwordL.place(x=70, y=160)
        self.passwordL.pack(side=TOP, padx=70)
        self.passwordE = Entry(self.registerWindow, show='*', relief=FLAT, textvariable=self.passwordS)
        # self.passwordE.place(x=70, y=180)
        self.passwordE.pack(side=TOP, padx=70)

        self.nameL = Label(self.registerWindow, text="Name", font=(10))
        # self.nameL.place(x=70, y=230)
        self.nameL.pack(side=TOP, padx=70)
        self.nameE = Entry(self.registerWindow, relief=FLAT, textvariable=self.nameS)
        # self.nameE.place(x=70, y=250)
        self.nameE.pack(side=TOP, padx=70)

        self.contacL = Label(self.registerWindow, text="Contact", font=(10))
        # self.contacL.place(x=70, y=300)
        self.contacL.pack(side=TOP, padx=70)
        self.contactE = Entry(self.registerWindow, relief=FLAT)
        # self.contactE.place(x=70, y=320)
        self.contactE.pack(side=TOP, padx=70)

        self.addressL = Label(self.registerWindow, text="Address", font=(10))
        # self.addressL.place(x=70, y=370)
        self.addressL.pack(side=TOP, padx=70)
        self.addressE = Entry(self.registerWindow, relief=FLAT)
        # self.addressE.place(x=70, y=390)
        self.addressE.pack(side=TOP, padx=70)

        self.jenjangPendL = Label(self.registerWindow, text="Jenjang Pendidikan", font=(10))
        # self.jenjangPendL.place(x=70, y=420)
        self.jenjangPendL.pack(side=TOP, padx=70)
        self.jenjangPendClicked = StringVar()
        self.jenjangPend = Combobox(self.registerWindow, state="readonly", width = 5, textvariable=self.jenjangPendClicked)
        self.jenjangPend['values'] = ("SD", "SMP", "SMA")
        # self.categ.grid(column=2, row=4)
        self.jenjangPend.current(0)
        # self.jenjangPend.place(x=70, y=440)
        self.jenjangPend.pack(side=TOP, padx=70)
        
        self.submit = Button(self.registerWindow, text='Submit', pady=5, padx=20, command=self.add)
        # self.submit.place(x=110, y=630)
        self.submit.pack(side=TOP, pady=10)
            
        
        
    def run(self):
        self.registerWindow.mainloop()
    
    def searchData(self, username):
        con = mysql.connect(host="localhost", user="root", password="root", database="tutorin")
        cursor = con.cursor()

        cursor.execute("SELECT * FROM user WHERE username ='"+username+"'")
        row = cursor.fetchall()
        print(row)
        if row == []:
            return 1
        return 0

    def add(self):

        con = mysql.connect(host="localhost", user="root", password="root", database="tutorin")
        cursor = con.cursor()

        id = 1;
        username = self.usernameE.get()
        password = self.passwordE.get()
        name = self.nameE.get()
        contact = self.contactE.get()
        address = self.addressE.get()
        balance = 0
        flag = 0
        rating = 0
        # jenjang =  self.jenjangPend.get()
        # cursor.execute("insert into user values(2,'abc','djdjd','jdjdjd','ddjjdjd','ddjjdjd', 0, 0, 0)")
        # print("('"+ username +"','" + password +"','" + name +"','" + contact +"','" + address, balance, flag, rating +"')")
        if (self.searchData(username)):
            cursor.execute("insert into user(username, password, nama, kontak, alamat) values('"+ username +"','" + password +"','" + name +"','" + contact +"','" + address +"')")
            cursor.execute('commit')
            messagebox.showinfo('Successful', 'Username was added')
        else :
            messagebox.showwarning("Warning", 'Username already exists')

        con.close()

        # data = (self.username,)
        # result = db.searchData(data)
        # print(result)
        # if result != 0:
        #     data = (self.username, self.hashed, self.name, self.contact, self.address)
        #     db.insertData(data)
        #     messagebox.showinfo('Successful', 'Username was added')
        # else:
        #     messagebox.showwarning("Warning", 'Username already exists')
