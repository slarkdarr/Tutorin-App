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
    # self.username = ''
    # self.password = ''
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
        self.usernameE = Entry(self.loginWindow, relief=FLAT)
        self.usernameE.place(x=70, y=80)
        self.passwordE = Entry(self.loginWindow, show='*', relief=FLAT)
        self.passwordE.place(x=70, y=120)
        # Actual Variales

        self.submit = Button(self.loginWindow, text='Submit', pady=5, padx=20, command=self.validate)
        self.submit.place(x=100, y=150)

    def validate(self):
        con = mysql.connect(host="localhost", user="root", password="", database="tutorin")
        cursor = con.cursor()
        cursor.execute("select * from user where username= '"+ self.usernameE.get() +"'")
        rows = cursor.fetchall()
        if len(rows) > 0 : 
            messagebox.showinfo('Successful', 'Login was sucessful')
        else : 
            messagebox.showerror('Error', 'Wrong Credentials')
        # cursor.execute("insert into user values('"+ self.username +"','" + self.hashed +"','" + self.name +"','" + self.contact +"','" + self.address +"','" +  "')")
        # cursor.execute('commit')
        # messagebox.showinfo('Successful', 'Username was added')
        # con.close()



        # data = (self.username,)
        # inputData = (self.username, self.password,)
        # try:
        #     if (db.validateData(data, inputData)):
        #         messagebox.showinfo('Successful', 'Login was sucessful')
        #     else:
        #         messagebox.showerror('Error', 'Wrong Credentials')
        # except IndexError:
        #     messagebox.showerror('Error', 'Wrong Credentials')
    def run(self):
        self.loginWindow.mainloop()




class Register:
    '''
    Class for Register
    @param username
    @param password
    '''
    def __init__(self):
        self.registerWindow = Tk()
        self.registerWindow.title('Register')
        self.registerWindow.geometry('300x800')
        self.label = Label(self.registerWindow, text='Register')
        self.label.place(x=110, y=40)
        # Tkinter Stuff
        # dropdown select account type
        self.clicked = StringVar()
        self.categ = Combobox(self.registerWindow, state="readonly", width = 5, textvariable=self.clicked)
        self.categ['values'] = ("Tutor", "Murid")
        # self.categ.grid(column=2, row=4)
        self.categ.current(0)
        
        self.categ.place(x=110, y=60)
        if (self.categ.get() == "Tutor"):
            self.categ.bind("<<ComboBoxSelected>>", self.comboClick)

        # self.usernameS = StringVar()
        # self.passwordS = StringVar()
        # self.nameS = StringVar()
        # self.contactS = StringVar()
        # self.addressS = StringVar()

        self.usernameL = Label(self.registerWindow, text="Username", font=(10))
        self.usernameL.place(x=70, y=90)
        self.usernameE = Entry(self.registerWindow, relief=FLAT)
        self.usernameE.place(x=70, y=110)

        self.passwordL = Label(self.registerWindow, text="Password", font=(10))
        self.passwordL.place(x=70, y=160)
        self.passwordE = Entry(self.registerWindow, show='*', relief=FLAT)
        self.passwordE.place(x=70, y=180)

        self.nameL = Label(self.registerWindow, text="Name", font=(10))
        self.nameL.place(x=70, y=230)
        self.nameE = Entry(self.registerWindow, relief=FLAT)
        self.nameE.place(x=70, y=250)

        self.contacL = Label(self.registerWindow, text="Contact", font=(10))
        self.contacL.place(x=70, y=300)
        self.contactS = Entry(self.registerWindow, relief=FLAT)
        self.contactS.place(x=70, y=320)

        self.addressL = Label(self.registerWindow, text="Address", font=(10))
        self.addressL.place(x=70, y=370)
        self.addressS = Entry(self.registerWindow, relief=FLAT)
        self.addressS.place(x=70, y=390)

        self.addressL = Label(self.registerWindow, text="Jenjang Pendidikan", font=(10))
        self.addressL.place(x=70, y=420)
        self.jenjangPendClicked = StringVar()
        self.jenjangPend = Combobox(self.registerWindow, state="readonly", width = 5)
        self.jenjangPend['values'] = ("SD", "SMP", "SMA")
        # self.categ.grid(column=2, row=4)
        self.jenjangPend.current(0)
        self.jenjangPend.place(x=70, y=440)
        

        self.submit = Button(self.registerWindow, text='Submit', pady=5, padx=20, command=self.add)
        self.submit.place(x=110, y=430)
        # Actual Variables
        # self.username = self.usernameS.get()
        # self.password = self.passwordS.get()
        # self.name = self.nameS.get()
        # self.contact = self.contactS.get()
        # self.address = self.addressS.get()
        
        self.salt = bcrypt.gensalt()
        self.hashed = bcrypt.hashpw(self.password.encode(), self.salt)

    def comboClick(self, event):
        self.fareS = IntVar()
        self.ktpS = StringVar()

        self.fareL = Label(self.registerWindow, text="Fare", font=(10))
        self.fareL.place(x=70, y=420)
        self.fareS = Entry(self.registerWindow, relief=FLAT, textvariable=self.fareS)
        self.fareS.place(x=70, y=440)  

        self.ktpL = Label(self.registerWindow, text="Fare", font=(10))
        self.ktpL.place(x=70, y=420)
        self.ktpE = Entry(self.registerWindow, relief=FLAT, textvariable=self.ktpS)
        self.ktpE.place(x=70, y=440) 

    def run(self):
        self.registerWindow.mainloop()

    def add(self):

        con = mysql.connect(host="localhost", user="root", password="", database="tutorin")
        cursor = con.cursor()
        # cursor.execute("insert into user values('','abc','djdjd','jdjdjd','ddjjdjd','ddjjdjd')")
        cursor.execute("insert into user values('"+ self.username +"','" + self.hashed +"','" + self.name +"','" + self.contact +"','" + self.address +"','" +  "')")
        cursor.execute('commit')
        messagebox.showinfo('Successful', 'Username was added')
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