from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import mysql.connector as mysql
import math
from PIL import ImageTk,Image  

class AkunMurid :
    def __init__(self, usernameS):
        self.akun = Tk()
        self.akun.title('Akun')
        self.akun.geometry('335x250')
        self.getData(usernameS)
        
        #profile picture
        stringimg = usernameS + ".png"
        try :
            self.img = ImageTk.PhotoImage(Image.open(stringimg).resize((100,100), Image.ANTIALIAS))
        except :
            self.img = ImageTk.PhotoImage(Image.open("default.PNG").resize((100,100), Image.ANTIALIAS))
        self.picture = Label(self.akun, image = self.img, anchor = "nw", height = 90, width = 100)
        self.picture.pack(side = TOP, fill = "both", padx = 20)

        #Line
        self.line1 = Canvas(self.akun, height = 10, width = 400)
        self.line1.create_line(15, 5, 320, 5)
        self.line1.pack(side = TOP, fill = "both")
        
        #Nama
        self.nama = Label(self.akun, anchor = "nw", text = self.namaS, font = "Arial 10 bold")
        self.nama.pack(side = TOP, fill = "both", padx = 30)

        #Sebagai
        self.sebagai = Label(self.akun, anchor = "nw", text = "Murid", font = "Arial 10")
        self.sebagai.pack(side = TOP, fill = "both", padx = 30)

        #balance
        self.balance = Label(self.akun, anchor = "nw", text = "Balance : " + str(self.balanceS), font = "Arial 10")
        self.balance.pack(side = TOP, fill = "both", padx = 30)

        #rating
        self.rating = Label(self.akun, anchor = "nw", text = "Rating : " + str(self.ratingS) + "/5.0", font = "Arial 10")
        self.rating.pack(side = TOP, fill = "both", padx = 30)
    
    def getData(self, username):
        con = mysql.connect(host = "localhost", user="root", password="iyvlinriminis30", database = "tutorin")
        cursor = con.cursor()

        cursor.execute("SELECT * FROM user WHERE username = '"+ username +"'")
        row = cursor.fetchall()
        self.namaS = row[0][3]
        self.balanceS = row[0][6]
        self.ratingS = row[0][8]
        con.close()
    
    def run(self):
        self.akun.mainloop()

class AkunTutor :
    def __init__(self, usernameS):
        self.akun = Tk()
        self.akun.title('Akun')
        self.akun.geometry('500x500')
        self.getData(usernameS)
        self.usernameS = usernameS
        #profile picture
        stringimg = usernameS + ".png"
        try :
            self.img = ImageTk.PhotoImage(Image.open(stringimg).resize((100,100), Image.ANTIALIAS))
        except :
            self.img = ImageTk.PhotoImage(Image.open("default.PNG").resize((100,100), Image.ANTIALIAS))
        self.picture = Label(self.akun, image = self.img, anchor = "nw", height = 90, width = 100)
        self.picture.pack(side = TOP, fill = "both", padx = 10)

        #Line
        self.line1 = Canvas(self.akun, height = 10, width = 400)
        self.line1.create_line(15, 5, 485, 5)
        self.line1.pack(side = TOP, fill = "both")

        # #-------------Frame 1-----------
        self.frame1 = Frame(self.akun, bd=1, relief=FLAT)
        self.frame1.columnconfigure(0, weight = 1)
        self.frame1.columnconfigure(1, weight = 1)
        self.frame1.pack(side = TOP, fill="both", padx=20)

        self.nama = Label(self.frame1, text=self.namaS, font = "Arial 10 bold").grid(row = 0, column = 0, sticky = "w")
        self.balance = Label(self.frame1, text="IDR "+self.toCurrency(self.balanceS), font = "Arial 10 bold").grid(row = 0, column = 1, sticky = "e")

        self.sebagai = Label(self.frame1, text = "Tutor", font = "Arial 10").grid(row = 1, column = 0, sticky = "w")
        self.tarif = Label(self.frame1, text = self.toCurrency(self.tarifS)+"/session", font = "Arial 10").grid(row = 1, column = 1, sticky = "e")
        self.kontak = Label(self.frame1, text ="Kontak\t: " + self.kontakS, font = "Arial 10").grid(row = 2, column = 0, sticky = "w")
        self.rating = Label(self.frame1, text = "Rating\t: "+ str(self.ratingS) + "/5.0", font = "Arial 10").grid(row = 3, column = 0, sticky = "w")

        self.update = Button(self.frame1, text="Update Info", pady=5, command=self.update).grid(row = 4, column = 1, sticky = "e")

        # #-------------Frame 2-----------
        self.frame2 = Frame(self.akun, bd=1, relief= GROOVE)
        self.frame2.pack(side = TOP, fill="both", padx=20, pady = 10)

        self.heading1 = Label(self.frame2, text = "About Me", font = "Arial 12 bold").grid(sticky = "w")
        self.headline = Label(self.frame2, text = self.headlineS, font = "Arial 10").grid(sticky = "w")

        # #-------------Frame 3-----------
        self.frame3 = Frame(self.akun, bd=1, relief= GROOVE)
        self.frame3.pack(side = TOP, fill="both", padx=20, pady = 10)

        self.heading2 = Label(self.frame3, text = "Experience", font = "Arial 12 bold").grid(sticky = "w")
        self.exp = Label(self.frame3, text = self.pengalamanS, font = "Arial 10").grid(sticky = "w")

         # #-------------Frame 4-----------
        self.frame4 = Frame(self.akun, bd=1, relief= GROOVE)
        self.frame4.pack(side = TOP, fill="both", padx=20, pady = 10)

        self.heading3 = Label(self.frame4, text = "Education", font = "Arial 12 bold").grid(sticky = "w")
        self.edu = Label(self.frame4, text = self.pendidikanS, font = "Arial 10").grid(sticky = "w")

    def update(self):
        app2 = UpdateAkun(self.usernameS)
        app2.run()

    def toCurrency(self, uang):
        builder = ""
        count = 0
        if(uang == 0): return "0"
        while(uang>0):
            x = uang%10
            s = ""
            if(x == 0): s = "0"
            elif(x == 1): s = "1"
            elif(x == 2): s = "2"
            elif(x == 3): s = "3"
            elif(x == 4): s = "4"
            elif(x == 5): s = "5"
            elif(x == 6): s = "6"
            elif(x == 7): s = "7"
            elif(x == 8): s = "8"
            elif(x == 9): s = "9"
            if(count == 3):
                builder = s + "." + builder
                count -= 3
            else:
                builder = s + builder
            count+=1
            uang= math.floor(uang/10)
        return builder
        
            

    def getData(self, username):
        con = mysql.connect(host = "localhost", user="root", password="iyvlinriminis30", database = "tutorin")
        cursor = con.cursor()

        cursor.execute("SELECT * FROM user WHERE username = '"+ username +"'")
        row = cursor.fetchall()
        self.namaS = row[0][3]
        self.kontakS = row[0][4]
        self.balanceS = row[0][6]
        self.ratingS = row[0][8]
        cursor.execute("SELECT * FROM tutor WHERE username = '"+ username +"'")
        row = cursor.fetchall()
        self.jenjangS = row[0][1]
        self.tarifS = row[0][2]
        self.pengalamanS = row[0][4]
        self.pendidikanS = row[0][5]
        self.headlineS = row[0][6]
        con.close()

    def run(self) :
        self.akun.mainloop()

class UpdateAkun :
    def __init__(self, usernameS):
        self.akun = Toplevel()
        self.akun.title('Update Akun')
        self.akun.geometry('500x500')
    
    def update(self):
        print("a")

    def run(self):
        self.akun.mainloop()