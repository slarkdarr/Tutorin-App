from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import mysql.connector as mysql
import math
from PIL import ImageTk, Image


class AkunMurid:
    def __init__(self, usernameS):
        self.akun = Tk()
        self.akun.title('Akun')
        self.akun.geometry('335x250')
        self.getData(usernameS)

        # profile picture
        stringimg = usernameS + ".png"
        try:
            self.img = ImageTk.PhotoImage(Image.open(
                stringimg).resize((100, 100), Image.ANTIALIAS))
        except:
            self.img = ImageTk.PhotoImage(Image.open(
                "default.PNG").resize((100, 100), Image.ANTIALIAS))
        self.picture = Label(self.akun, image=self.img,
                             anchor="nw", height=90, width=100)
        self.picture.pack(side=TOP, fill="both", padx=20)

        # Line
        self.line1 = Canvas(self.akun, height=10, width=400)
        self.line1.create_line(15, 5, 320, 5)
        self.line1.pack(side=TOP, fill="both")

        # Nama
        self.nama = Label(self.akun, anchor="nw",
                          text=self.namaS, font="Arial 10 bold")
        self.nama.pack(side=TOP, fill="both", padx=30)

        # Sebagai
        self.sebagai = Label(self.akun, anchor="nw",
                             text="Murid", font="Arial 10")
        self.sebagai.pack(side=TOP, fill="both", padx=30)

        # balance
        self.balance = Label(
            self.akun, anchor="nw", text="Balance : " + str(self.balanceS), font="Arial 10")
        self.balance.pack(side=TOP, fill="both", padx=30)

        # rating
        self.rating = Label(self.akun, anchor="nw", text="Rating : " +
                            str(self.ratingS) + "/5.0", font="Arial 10")
        self.rating.pack(side=TOP, fill="both", padx=30)

    def getData(self, username):
        con = mysql.connect(host="localhost", user="root",
                            password="", database="tutorin")
        cursor = con.cursor()

        cursor.execute(
            "SELECT * FROM user WHERE username = '" + username + "'")
        row = cursor.fetchall()
        self.namaS = row[0][3]
        self.balanceS = row[0][6]
        self.ratingS = row[0][8]
        con.close()

    def run(self):
        self.akun.mainloop()


class AkunTutor:
    def __init__(self, usernameS):
        self.akun = Tk()
        self.akun.title('Akun')
        self.akun.geometry('500x500')
        self.getData(usernameS)
        self.usernameS = usernameS
        # profile picture
        stringimg = usernameS + ".png"
        try:
            self.img = ImageTk.PhotoImage(Image.open(
                stringimg).resize((100, 100), Image.ANTIALIAS))
        except:
            self.img = ImageTk.PhotoImage(Image.open(
                "default.PNG").resize((100, 100), Image.ANTIALIAS))
        self.picture = Label(self.akun, image=self.img,
                             anchor="nw", height=90, width=100)
        self.picture.pack(side=TOP, fill="both", padx=10)

        # Line
        self.line1 = Canvas(self.akun, height=10, width=400)
        self.line1.create_line(15, 5, 485, 5)
        self.line1.pack(side=TOP, fill="both")

        # #-------------Frame 1-----------
        self.frame1 = Frame(self.akun, bd=1, relief=FLAT)
        self.frame1.columnconfigure(0, weight=1)
        self.frame1.columnconfigure(1, weight=1)
        self.frame1.pack(side=TOP, fill="both", padx=20)

        self.nama = Label(self.frame1, text=self.namaS, font="Arial 10 bold")
        self.nama.grid(row=0, column=0, sticky="w")
        self.balance = Label(self.frame1, text="IDR " +
                             self.toCurrency(self.balanceS), font="Arial 10 bold")
        self.balance.grid(row=0, column=1, sticky="e")

        self.sebagai = Label(self.frame1, text="Tutor", font="Arial 10")
        self.sebagai.grid(row=1, column=0, sticky="w")
        self.tarif = Label(self.frame1, text=self.toCurrency(
            self.tarifS)+"/session", font="Arial 10")
        self.tarif.grid(row=1, column=1, sticky="e")
        self.kontak = Label(self.frame1, text="Kontak\t: " +
                            self.kontakS, font="Arial 10")
        self.kontak.grid(row=2, column=0, sticky="w")
        self.rating = Label(self.frame1, text="Rating\t: " +
                            str(self.ratingS) + "/5.0", font="Arial 10")
        self.rating.grid(row=3, column=0, sticky="w")

        self.update = Button(self.frame1, text="Update Info",
                             pady=5, command=self.update)
        self.update.grid(row=4, column=1, sticky="e")

        # #-------------Frame 2-----------
        self.frame2 = Frame(self.akun, bd=1, relief=GROOVE)
        self.frame2.pack(side=TOP, fill="both", padx=20, pady=10)

        self.heading1 = Label(
            self.frame2, text="About Me", font="Arial 12 bold")
        self.heading1.grid(sticky="w")
        self.headline = Label(
            self.frame2, text=self.headlineS, font="Arial 10")
        self.headline.grid(sticky="w")

        # #-------------Frame 3-----------
        self.frame3 = Frame(self.akun, bd=1, relief=GROOVE)
        self.frame3.pack(side=TOP, fill="both", padx=20, pady=10)

        self.heading2 = Label(
            self.frame3, text="Experience", font="Arial 12 bold")
        self.heading2.grid(sticky="w")
        self.exp = Label(self.frame3, text=self.pengalamanS, font="Arial 10")
        self.exp.grid(sticky="w")

        # #-------------Frame 4-----------
        self.frame4 = Frame(self.akun, bd=1, relief=GROOVE)
        self.frame4.pack(side=TOP, fill="both", padx=20, pady=10)

        self.heading3 = Label(
            self.frame4, text="Education", font="Arial 12 bold")
        self.heading3.grid(sticky="w")
        self.edu = Label(self.frame4, text=self.pendidikanS, font="Arial 10")
        self.edu.grid(sticky="w")

    def update(self):
        app2 = UpdateAkun(self.usernameS)
        app2.run()
        username = self.usernameS

    def toCurrency(self, uang):
        builder = ""
        count = 0
        if(uang == 0):
            return "0"
        while(uang > 0):
            x = uang % 10
            s = ""
            if(x == 0):
                s = "0"
            elif(x == 1):
                s = "1"
            elif(x == 2):
                s = "2"
            elif(x == 3):
                s = "3"
            elif(x == 4):
                s = "4"
            elif(x == 5):
                s = "5"
            elif(x == 6):
                s = "6"
            elif(x == 7):
                s = "7"
            elif(x == 8):
                s = "8"
            elif(x == 9):
                s = "9"
            if(count == 3):
                builder = s + "." + builder
                count -= 3
            else:
                builder = s + builder
            count += 1
            uang = math.floor(uang/10)
        return builder

    def getData(self, username):
        con = mysql.connect(host="localhost", user="root",
                            password="", database="tutorin")
        cursor = con.cursor()

        cursor.execute(
            "SELECT * FROM user WHERE username = '" + username + "'")
        row = cursor.fetchall()
        self.namaS = row[0][3]
        self.kontakS = row[0][4]
        self.balanceS = row[0][6]
        self.ratingS = row[0][8]
        cursor.execute(
            "SELECT * FROM tutor WHERE username = '" + username + "'")
        row = cursor.fetchall()
        self.jenjangS = row[0][1]
        self.tarifS = row[0][2]
        self.pengalamanS = row[0][4]
        self.pendidikanS = row[0][5]
        self.headlineS = row[0][6]
        con.close()

    def run(self):
        self.akun.mainloop()


class UpdateAkun:
    def __init__(self, usernameS):
        self.akun = Toplevel()
        self.akun.title('Update Akun')
        self.akun.geometry('500x550')
        self.getData(usernameS)
        self.usernameS = usernameS
        self.frame1 = Frame(self.akun, bd=1, relief=FLAT)
        self.frame1.columnconfigure(0, weight=1)
        self.frame1.columnconfigure(1, weight=2)
        self.frame1.pack(side=TOP, fill="both", padx=20, pady=10)
        # Nama
        self.label1 = Label(self.frame1, text="Nama\t:", font="Arial 10")
        self.label1.grid(row=0, column=0, sticky="nw")
        self.nama = Text(self.frame1, font="Arial 10", height=1, width=50)
        self.nama.insert("1.0", self.namaS)
        self.nama.grid(row=0, column=1, sticky="w")
        # Kontak
        self.label2 = Label(self.frame1, text="Kontak\t:", font="Arial 10")
        self.label2.grid(row=1, column=0, sticky="nw")
        self.kontak = Text(self.frame1, font="Arial 10", height=1, width=50)
        self.kontak.insert("1.0", self.kontakS)
        self.kontak.grid(row=1, column=1, sticky="w")
        # Alamat
        self.label3 = Label(self.frame1, text="Alamat\t:", font="Arial 10")
        self.label3.grid(row=2, column=0, sticky="nw")
        self.alamat = Text(self.frame1, font="Arial 10", height=2, width=50)
        self.alamat.insert("1.0", self.alamatS)
        self.alamat.grid(row=2, column=1, sticky="w")
        # Jenjang
        self.label4 = Label(self.frame1, text="Jenjang\t:", font="Arial 10")
        self.label4.grid(row=3, column=0, sticky="nw")
        self.jenjangClicked = StringVar()
        self.jenjang = Combobox(self.frame1, state="readonly",
                                font="Arial 10", width=5, textvariable=self.jenjangClicked)

        self.jenjang['values'] = ("SD", "SMP", "SMA")
        self.jenjang.current(0)
        try:
            if(self.jenjangS == "SMP"):
                self.jenjang.current(1)
            elif(self.jenjangS == "SMA"):
                self.jenjang.current(2)
        except:
            self.jenjang.current(0)
        self.jenjang.grid(row=3, column=1, sticky="w")

        # Tarif
        self.label5 = Label(self.frame1, text="Tarif\t:", font="Arial 10")
        self.label5.grid(row=4, column=0, sticky="nw")
        self.tarif = Text(self.frame1, font="Arial 10", height=1, width=50)
        self.tarif.insert("1.0", str(self.tarifS))
        self.tarif.grid(row=4, column=1, sticky="w")

        # #----------Frame2---------
        self.frame2 = Frame(self.akun, bd=1, relief=FLAT)
        self.frame2.pack(side=TOP, fill="both", padx=20, pady=10)
        # Pengalaman
        self.label6 = Label(self.frame2, text="Experience\t:",
                            font="Arial 10", pady=5)
        self.label6.grid(row=0, column=0, sticky="nw")
        self.pengalaman = Text(self.frame2, font="Arial 10",
                               height=4, width=60, wrap=WORD)
        self.pengalaman.insert("1.0", self.pengalamanS)
        self.pengalaman.grid(row=1, column=0, sticky="nsew")
        self.scrollbar = Scrollbar(self.frame2, command=self.pengalaman.yview)
        self.scrollbar.grid(row=1, column=1, sticky="ns")
        self.pengalaman['yscrollcommand'] = self.scrollbar.set
        # Pendidikan
        self.label7 = Label(self.frame2, text="Education\t:",
                            font="Arial 10", pady=5)
        self.label7.grid(row=2, column=0, sticky="nw")
        self.pendidikan = Text(self.frame2, font="Arial 10",
                               height=4, width=60, wrap=WORD)
        self.pendidikan.insert("1.0", self.pendidikanS)
        self.pendidikan.grid(row=3, column=0, sticky="nsew")
        self.scrollbar = Scrollbar(self.frame2, command=self.pendidikan.yview)
        self.scrollbar.grid(row=3, column=1, sticky="ns")
        self.pendidikan['yscrollcommand'] = self.scrollbar.set
        # Headline
        self.label8 = Label(self.frame2, text="Headline\t:",
                            font="Arial 10", pady=5)
        self.label8.grid(row=4, column=0, sticky="nw")
        self.headline = Text(self.frame2, font="Arial 10",
                             height=4, width=60, wrap=WORD)
        self.headline.insert("1.0", self.headlineS)
        self.headline.grid(row=5, column=0, sticky="nsew")
        self.scrollbar = Scrollbar(self.frame2, command=self.headline.yview)
        self.scrollbar.grid(row=5, column=1, sticky="ns")
        self.headline['yscrollcommand'] = self.scrollbar.set

        # #-----------Frame 3----------------
        self.frame3 = Frame(self.akun, bd=1, relief=FLAT)
        self.frame3.pack(side=TOP, fill="both", padx=20, pady=10)
        self.frame3.columnconfigure(0, weight=1)
        self.frame3.columnconfigure(1, weight=3)
        self.frame3.columnconfigure(2, weight=1)
        self.back = Button(self.frame3, text='back',
                           padx=5, command=self.exit_btn)
        self.back.grid(row=0, column=1, sticky="e")
        self.update = Button(self.frame3, text="Submit",
                             padx=5, command=self.update)
        self.update.grid(row=0, column=2, sticky="n")

    def exit_btn(self):
        self.akun.destroy()

    def update(self):
        con = mysql.connect(host="localhost", user="root",
                            password="", database="tutorin")
        cursor = con.cursor()
        stringbuilder = self.nama.get("1.0", END)
        self.namaS = stringbuilder[:len(stringbuilder)-1]

        stringbuilder = self.kontak.get("1.0", END)
        self.kontakS = stringbuilder[:len(stringbuilder)-1]

        stringbuilder = self.alamat.get("1.0", END)
        self.alamatS = stringbuilder[:len(stringbuilder)-1]

        stringbuilder = self.jenjang.get()
        self.jenjangS = stringbuilder

        stringbuilder = self.pengalaman.get("1.0", END)
        self.pengalamanS = stringbuilder[:len(stringbuilder)-1]

        stringbuilder = self.pendidikan.get("1.0", END)
        self.pendidikanS = stringbuilder[:len(stringbuilder)-1]

        stringbuilder = self.headline.get("1.0", END)
        self.headlineS = stringbuilder[:len(stringbuilder)-1]

        try:
            stringbuilder = self.tarif.get("1.0", END)
            self.tarifS = int(stringbuilder[:len(stringbuilder)-1])
            cursor.execute("UPDATE user SET nama = '"+self.namaS+"', kontak = '"+self.kontakS +
                           "', alamat = '"+self.alamatS+"' WHERE username = '"+self.usernameS+"'")
            cursor.execute('commit')
            try:
                cursor.execute("UPDATE tutor SET jenjang = '"+self.jenjangS+"', tarif = '"+str(self.tarifS)+"', pengalaman = '"+self.pengalamanS +
                               "', pendidikan = '"+self.pendidikanS+"', headline = '"+self.headlineS+"' WHERE username = '"+self.usernameS+"'")
                cursor.execute('commit')
                messagebox.showinfo(
                    'Successful', 'Your account has been updated')
                self.akun.destroy()
            except:
                messagebox.showwarning(
                    "Warning", 'There is an error in your input')
        except:
            messagebox.showwarning(
                "Warning", 'There is an error in your input')

    def getData(self, username):
        con = mysql.connect(host="localhost", user="root",
                            password="", database="tutorin")
        cursor = con.cursor()

        cursor.execute(
            "SELECT * FROM user WHERE username = '" + username + "'")
        row = cursor.fetchall()
        self.namaS = row[0][3]
        self.kontakS = row[0][4]
        self.alamatS = row[0][5]
        cursor.execute(
            "SELECT * FROM tutor WHERE username = '" + username + "'")
        row = cursor.fetchall()
        self.jenjangS = row[0][1]
        self.tarifS = row[0][2]
        self.pengalamanS = row[0][4]
        self.pendidikanS = row[0][5]
        self.headlineS = row[0][6]
        con.close()

    def run(self):
        self.akun.mainloop()
