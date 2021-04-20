import tkinter as tk
import csv
from tkinter.ttk import Combobox
from tkinter import messagebox
import sqlite3

class searchTutor:
    def __init__(self):
        self.search = tk.Tk()
        HEIGHT = 670
        WIDTH = 800

        #create canvas
        self.canvas = tk.Canvas(self.search, height = HEIGHT, width = WIDTH)
        self.canvas.pack()

        #create frame
        self.frame = tk.Frame(self.canvas, bg = '#80c1ff', bd = 2)
        self.frame.place(relwidth=0.9, relheight=0.3, relx=0.05, rely=0.05)

        self.lower_frame = tk.Frame(self.search, bg = '#80c1ff', bd = 2)
        self.lower_frame.place(relwidth=0.9, relheight=0.6, relx=0.05, rely=0.35)

        #judul
        self.label1 = tk.Label(self.frame, text="Search Tutor", bg = '#80c1ff', font=40)
        self.label1.place(relx=0.4, rely=0)

        #matapelajaran
        self.label4 = tk.Label(self.frame, text='Mata Pelajaran', font=40, bg = '#80c1ff')
        self.label4.place(relx=0.1, rely=0.2)

        self.mapelAva = ('Biologi', 'Matematika', 'Fisika', 'Kimia', 'Ekonomi', 'Sosiologi', 'Geografi', 
                    'Bahasa Inggris', 'Bahasa Indonesia', 'Sejarah')
        self.varmapel = tk.StringVar()
        self.mapelEntry = Combobox(self.frame, value=self.mapelAva, textvariable = self.varmapel, state="readonly")
        self.mapelEntry.place(relx=0.3, rely=0.2, relwidth=0.6)

        #jenjang pendidikan mapel
        self.label2 = tk.Label(self.frame, text='Jenjang ', font=40, bg = '#80c1ff')
        self.label2.place(relx=0.1, rely=0.35)

        self.varje = tk.IntVar()
        self.jeng1 = tk.Radiobutton(self.frame, text="SMP", variable=self.varje, value=1)
        self.jeng1.place(relx=0.3, rely=0.35)

        self.jeng2 = tk.Radiobutton(self.frame, text="SMA", variable=self.varje, value=2)
        self.jeng2.place(relx=0.5, rely=0.35)

        #tingkat
        self.label3 = tk.Label(self.frame, text='Tingkat', font=40, bg = '#80c1ff')
        self.label3.place(relx=0.1, rely=0.5)

        self.varting = tk.IntVar()
        self.ting1 = tk.Radiobutton(self.frame, text="Kelas 1", variable=self.varting, value=1)
        self.ting1.place(relx=0.3, rely=0.5)

        self.ting2 = tk.Radiobutton(self.frame, text="Kelas 2", variable=self.varting, value=2)
        self.ting2.place(relx=0.5, rely=0.5)

        self.ting3 = tk.Radiobutton(self.frame, text="Kelas 3", variable=self.varting, value=3)
        self.ting3.place(relx=0.7, rely=0.5)


        #hari
        self.label5 = tk.Label(self.frame, text='Hari ', font=40, bg = '#80c1ff')
        self.label5.place(relx=0.1, rely=0.65)

        self.hariAva = ('Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu')
        self.varhari = tk.StringVar()
        self.hariEntry = Combobox(self.frame, value=self.hariAva, textvariable = self.varhari, state="readonly")
        self.hariEntry.place(relx=0.3, rely=0.65, relwidth=0.6)


        #lower
        self.scrollbar = tk.Scrollbar(self.lower_frame, orient=tk.VERTICAL)
        self.scrollbar.place(relx=0.05, rely=0, relwidth=0.9, relheight=0.85)

        self.mylist = tk.Listbox(self.lower_frame, yscrollcommand = self.scrollbar.set )
        self.mylist.place(relx=0.05, rely=0, relwidth=0.9, relheight=0.85)

        self.scrollbar.config( command = self.mylist.yview )

        self.button = tk.Button(self.frame, text="Search", bd=2, command=lambda:self.searchTutorFunction(self.mylist))
        self.button.place(relx=0.75, rely=0.8)

        self.button2 = tk.Button(self.lower_frame, text="Pesan Tutor", bd=2)
        self.button2.place(relx=0.75, rely=0.9)

    def searchTutorFunction(self, list):
        conn = sqlite3.connect('Tutorin.db')
        c = conn.cursor()
        list.delete(0,list.size())
        jen = ""
        if(int(self.varje.get()) == 1) :
            jen = "SMP"
        elif(int(self.varje.get()) == 2) :
            jen = "SMA"
        ting = self.varting.get() #default = 0
        mapel = self.varmapel.get()
        hari = str(self.varhari.get())
        # print(hari)
        # print(mapel)
        # print(ting)
        # print(jen)
        if(mapel == "" or jen == ""):
            messagebox.showerror("Error", "Data Tidak Lengkap.\nWajib Memasukkan Nilai Mata Pelajaran dan Jenjang!")
            #print('gagal')
        #untuk tingkat kosong
        elif(ting == 0):
            c.execute("SELECT rowid, * FROM DetailCourse WHERE namaMapel = (?) AND jenjang = (?)", (mapel,jen,))
            dataMapel = c.fetchall()
            #print(dataMapel)
            #untuk tingkat dan hari kosong
            if(hari == ""):
                for x in dataMapel :
                    c.execute("SELECT rowid, * FROM JadwalTutor WHERE courseID = (?)", (x[0],))
                    dataJadwal = c.fetchall()
                    for y in dataJadwal:
                    #print(y)
                        text = ("ID Tutor : "+ str(y[1])+ " | Nama : "+" | Mata Pelajaran : " + x[1] + " | " + x[2] + " Kelas " + str(x[3]) + " | Hari : " + y[3] + " | " + "Jam Mulai : " + str(y[4]) + ".00 WIB" + " | Durasi : " + str(y[5]) + " Jam")
                        # print(text)
                        list.insert(tk.END,text)
            #untuk tingkat kosong dan hari tidak kosong
            else:
                for x in dataMapel :
                    c.execute("SELECT rowid, * FROM JadwalTutor WHERE courseID = (?) AND hari = (?)", (x[0],hari,))
                    dataJadwal = c.fetchall()
                    for y in dataJadwal:
                    #print(y)
                        text = ("ID Tutor : "+ str(y[1])+ " | Nama : "+" | Mata Pelajaran : " + x[1] + " | " + x[2] + " Kelas " + str(x[3]) + " | Hari : " + y[3] + " | " + "Jam Mulai : " + str(y[4]) + ".00 WIB" + " | Durasi : " + str(y[5]) + " Jam")
                        #print(text)
                        list.insert(tk.END,text)
        #untuk tingkat terisi
        else :
            c.execute("SELECT rowid, * FROM DetailCourse WHERE namaMapel = (?) AND jenjang = (?) AND tingkat = (?)", (mapel,jen,ting,))
            dataMapel = c.fetchall()
            #print(dataMapel)
            #untuk tingkat terisi dan hari kosong
            if(hari == ""):
                for x in dataMapel :
                    c.execute("SELECT rowid, * FROM JadwalTutor WHERE courseID = (?)", (x[0],))
                    dataJadwal = c.fetchall()
                    for y in dataJadwal:
                    #print(y)
                        text = ("ID Tutor : "+ str(y[1])+ " | Nama : "+" | Mata Pelajaran : " + x[1] + " | " + x[2] + " Kelas " + str(x[3]) + " | Hari : " + y[3] + " | " + "Jam Mulai : " + str(y[4]) + ".00 WIB" + " | Durasi : " + str(y[5]) + " Jam")
                        # print(text)
                        list.insert(tk.END,text)
            #untuk semua terisi
            else:
                for x in dataMapel :
                    c.execute("SELECT rowid, * FROM JadwalTutor WHERE courseID = (?) AND hari = (?)", (x[0],hari,))
                    dataJadwal = c.fetchall()
                    for y in dataJadwal:
                    #print(y)
                        text = ("ID Tutor : "+ str(y[1])+ " | Nama : "+" | Mata Pelajaran : " + x[1] + " | " + x[2] + " Kelas " + str(x[3]) + " | Hari : " + y[3] + " | " + "Jam Mulai : " + str(y[4]) + ".00 WIB" + " | Durasi : " + str(y[5]) + " Jam")
                        #print(text)
                        list.insert(tk.END,text)
        #print(list.size())
        if(list.size() == 0) :
            list.insert(tk.END,"0 Results Found")
        conn.commit()
        conn.close()

    def konfirmasiPemesanan(self):
        MsgBox = messagebox.askquestion("askquestion", "Apakah Ada Yakin Ingin Melakukan Pemesanan?")

    def run(self):
        self.search.mainloop()

# e = searchTutor()
# e.run()