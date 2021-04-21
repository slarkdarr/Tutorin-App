import tkinter as tk
import csv
from tkinter.ttk import Combobox
from tkinter import messagebox
import sqlite3

class jadwalTutor:
    def __init__(self):
        self.jadwal = tk.Tk()
        self.jadwal.title('Jadwal Tutor')
        self.jadwal.geometry('800x670')
        HEIGHT = 670
        WIDTH = 800
        #create canvas
        self.canvas = tk.Canvas(self.jadwal, height = HEIGHT, width = WIDTH)
        self.canvas.pack()


        #create frame
        self.frame = tk.Frame(self.jadwal, bg = '#80c1ff', bd = 2)
        self.frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

        self.frame2 = tk.Frame(self.jadwal, bg = '#80c1ff', bd = 2) #ini buat lihat calender
        self.frame2.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)


        #==============frame1===================
        self.label1 = tk.Label(self.frame, text="Form Jadwal Tutor", bg = '#80c1ff', font=50)
        self.label1.place(relx=0.4, rely=0)

        #username/ID
        self.label2 = tk.Label(self.frame, text='ID', font=40, bg = '#80c1ff')
        self.label2.place(relx=0.1, rely=0.1)

        self.textbox1 = tk.Entry(self.frame, font=40)
        self.textbox1.place(relx=0.3, rely=0.1, relwidth=0.6)

        #nama
        self.label3 = tk.Label(self.frame, text='Nama', font=40, bg = '#80c1ff')
        self.label3.place(relx=0.1, rely=0.15)

        self.textbox3 = tk.Entry(self.frame, font=40)
        self.textbox3.place(relx=0.3, rely=0.15, relwidth=0.6)

        #jenjang pendidikan mapel
        self.label4 = tk.Label(self.frame, text='Jenjang ', font=40, bg = '#80c1ff')
        self.label4.place(relx=0.1, rely=0.20)

        self.varje = tk.IntVar()
        self.jeng1 = tk.Radiobutton(self.frame, text="SMP", variable=self.varje, value=1)
        self.jeng1.place(relx=0.3, rely=0.2)

        self.jeng2 = tk.Radiobutton(self.frame, text="SMA", variable=self.varje, value=2)
        self.jeng2.place(relx=0.5, rely=0.2)

        #tingkat
        self.label5 = tk.Label(self.frame, text='Tingkat', font=40, bg = '#80c1ff')
        self.label5.place(relx=0.1, rely=0.25)

        self.varting = tk.IntVar()
        self.ting1 = tk.Radiobutton(self.frame, text="Kelas 1", variable=self.varting, value=1)
        self.ting1.place(relx=0.3, rely=0.25)

        self.ting2 = tk.Radiobutton(self.frame, text="Kelas 2", variable=self.varting, value=2)
        self.ting2.place(relx=0.5, rely=0.25)

        self.ting3 = tk.Radiobutton(self.frame, text="Kelas 3", variable=self.varting, value=3)
        self.ting3.place(relx=0.7, rely=0.25)

        #matapelajaran
        self.label6 = tk.Label(self.frame, text='Mata Pelajaran', font=40, bg = '#80c1ff')
        self.label6.place(relx=0.1, rely=0.3)

        self.mapelAva = ('Biologi', 'Matematika', 'Fisika', 'Kimia', 'Ekonomi', 'Sosiologi', 'Geografi', 
                    'Bahasa Inggris', 'Bahasa Indonesia', 'Sejarah')
        self.varmapel = tk.StringVar()
        self.mapelEntry = Combobox(self.frame, value=self.mapelAva, textvariable = self.varmapel,state="readonly")
        self.mapelEntry.place(relx=0.3, rely=0.3, relwidth=0.6)

        #durasi
        self.label7 = tk.Label(self.frame, text='Durasi', font=40, bg = '#80c1ff')
        self.label7.place(relx=0.1, rely=0.35)

        self.vardur = tk.IntVar()
        self.dur1 = tk.Radiobutton(self.frame, text="1 Jam", variable=self.vardur, value=1)
        self.dur1.place(relx=0.3, rely=0.35)

        self.dur2 = tk.Radiobutton(self.frame, text="2 Jam", variable=self.vardur, value=2)
        self.dur2.place(relx=0.5, rely=0.35)

        #hari
        self.label8 = tk.Label(self.frame, text='Hari ', font=40, bg = '#80c1ff')
        self.label8.place(relx=0.1, rely=0.4)

        self.hariAva = ('Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu',)
        self.varhari = tk.StringVar()
        self.hariEntry = Combobox(self.frame, value=self.hariAva, textvariable = self.varhari,state="readonly")
        self.hariEntry.place(relx=0.3, rely=0.4, relwidth=0.6)
                    

        #jam
        self.label9 = tk.Label(self.frame, text='Jam Mulai', font=40, bg = '#80c1ff')
        self.label9.place(relx=0.1, rely=0.45)

        self.varjam = tk.StringVar()
        self.jamAva = ('08.00 WIB', '09.00 WIB','10.00 WIB','11.00 WIB','12.00 WIB','13.00 WIB','14.00 WIB','15.00 WIB',
                    '16.00 WIB','17.00 WIB','18.00 WIB','19.00 WIB','20.00 WIB')
        self.jamEntry = Combobox(self.frame, value=self.jamAva, textvariable = self.varjam, state="readonly")
        self.jamEntry.place(relx=0.3, rely=0.45, relwidth=0.6)

        #deskripsi
        self.label10 = tk.Label(self.frame, text='Deskripsi', font=40, bg = '#80c1ff')
        self.label10.place(relx=0.1, rely=0.5)

        self.textbox4 = tk.Entry(self.frame, font=25)
        self.textbox4.place(relx=0.3, rely=0.5, relwidth=0.6, relheight=0.25)

        self.button = tk.Button(self.frame, text="Submit Form", bd=2, command=self.saveForm)
        self.button.place(relx=0.75, rely=0.8)

        self.button2 = tk.Button(self.frame, text="Back", bd=2, command=lambda:self.raise_frame(self.frame2))
        self.button2.place(relx=0.65, rely=0.8)

        #======frame2=====
        self.labelf1 = tk.Label(self.frame2, text="Jadwal Tutor", bg = '#80c1ff', font=50)
        self.labelf1.place(relx=0.4, rely=0)

        self.labelf2 = tk.Label(self.frame2, text='My ID', font=40, bg = '#80c1ff')
        self.labelf2.place(relx=0.1, rely=0.1)

        self.textboxf1 = tk.Entry(self.frame2, font=25)
        self.textboxf1.place(relx=0.2, rely=0.1, relwidth=0.5)

        self.scrollbar = tk.Scrollbar(self.frame2, orient=tk.VERTICAL)
        self.scrollbar.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.7)

        self.mylist = tk.Listbox(self.frame2, yscrollcommand = self.scrollbar.set, font=40 )
        self.mylist.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.7)

        self.scrollbar.config( command = self.mylist.yview )

        self.buttonf1 = tk.Button(self.frame2, text="Submit", bd=2, command=lambda:self.showSchedule(self.mylist))
        self.buttonf1.place(relx=0.75, rely=0.1)

        self.buttonf2 = tk.Button(self.frame2, text="Add Schedule", bd=2, command=lambda:self.raise_frame(self.frame))
        self.buttonf2.place(relx=0.75, rely=0.93)

        self.buttonf3 = tk.Button(self.frame2, text="Delete Selected Schedule", bd=2, command=lambda:self.deleteJadwal(self.mylist))
        self.buttonf3.place(relx=0.5, rely=0.93)

    def getIntJam(self, jam):
        value = 0
        if(jam == "08.00 WIB"):
            value = 8
        elif(jam == "09.00 WIB"):
            value = 9
        elif(jam == "10.00 WIB"):
            value = 10
        elif(jam == "11.00 WIB"):
            value = 11
        elif(jam == "12.00 WIB"):
            value = 12
        elif(jam == "13.00 WIB"):
            value = 13
        elif(jam == "14.00 WIB"):
            value = 14
        elif(jam == "15.00 WIB"):
            value = 15
        elif(jam == "16.00 WIB"):
            value = 16
        elif(jam == "17.00 WIB"):
            value = 17
        elif(jam == "18.00 WIB"):
            value = 18
        elif(jam == "19.00 WIB"):
            value = 19
        elif(jam == "20.00 WIB"):
            value = 20
        return value

    def getID(self, data, mapel, ting, jen):
        for x in data:
            #print(x)
            if(x[1] == mapel and x[2] == jen and x[3] == ting):
                return x[0]
        return 0

    def getID2(self, data, data2) :
        for x in data:
            if(x == data2):
                return x[0]
        return 0

    def saveForm(self):
        conn = sqlite3.connect('Tutorin.db')
        c = conn.cursor()

        id = self.textbox1.get()
        nama = self.textbox3.get()
        jen = ""
        if(int(self.varje.get()) == 1) :
            jen = "SMP"
        elif(int(self.varje.get()) == 2) :
            jen = "SMA"
        ting = self.varting.get()
        mapel = self.varmapel.get()
        durasi = self.vardur.get()
        hari = self.varhari.get()
        jam = self.getIntJam(self.varjam.get())
        desc = self.textbox4.get()
        if(desc == ""):
            desc = "Tidak Ada"
        #id, nama, jenjang, tingkat, mapel, durasi, hari, jam, des
        if(id=="" or nama=="" or jen=="" or ting==0 or durasi==0 or mapel =="" or hari=="" or jam==0):
            #show messagebox
            messagebox.showerror("Error", "Data Tidak Lengkap.\nCek Kembali Data Anda!")
            #print("gagal")
        else:
            #dapetin IDcourse
            c.execute("SELECT rowid, * FROM DetailCourse")
            data = c.fetchall()
            courseid = self.getID(data, mapel, ting, jen)

            #print(courseid)
            nrow = [id,courseid,hari,jam,durasi,desc]
            #insert data to database
            c.execute("INSERT INTO JadwalTutor VALUES (?,?,?,?,?,?)", nrow)
            #show messagebox
            messagebox.showinfo("Info", "Berhasil Menyimpan Data")
            #print("sukses")
        conn.commit()
        conn.close()

    def showSchedule(self, list) :
        conn = sqlite3.connect('Tutorin.db')
        c = conn.cursor()

        #tampilkan schedule dari tutor
        id = self.textboxf1.get()

        #ambil data jadwal
        c.execute("SELECT rowid, * FROM JadwalTutor WHERE tutorID = (?)", (id,))
        data = c.fetchall()
        #print(data)
        #print(data)

        list.delete(0,list.size())
        i = 1
        for x in data :
            c.execute("SELECT rowid, * FROM DetailCourse WHERE rowid = (?)", (x[2],))
            data2 = c.fetchall()
            #print(data2)
            text = (str(i) + ". Mata Pelajaran : " + data2[0][1] + " | " + data2[0][2] + " Kelas " + str(data2[0][3]) + " | Hari : " + x[3] + " | " + "Jam Mulai : " + str(x[4]) + ".00 WIB")
            i = i + 1
            list.insert(tk.END,text)
            #print(text)
        conn.commit()
        conn.close()

    def deleteJadwal(self, list):
        MsgBox = messagebox.askquestion("askquestion", "Are you sure?")
        if (MsgBox == 'yes'):
            conn = sqlite3.connect('Tutorin.db')
            c = conn.cursor()

            id = self.textboxf1.get()
            sel = list.curselection()
            i = int(list.get(sel)[0]) - 1
            #print(list.get(sel)[0])
            #print(i)


            #ambil data jadwal
            c.execute("SELECT rowid, * FROM JadwalTutor")
            data = c.fetchall()
            #print(data)

            c.execute("SELECT rowid, * FROM JadwalTutor WHERE tutorID = (?)", (id,))
            data2 = c.fetchall()

            row = int(self.getID2(data, data2[i]))
            #print(row)
            #hapus data dari database
            c.execute("DELETE FROM JadwalTutor WHERE rowid = (?)",(row,))
            #print('sukses')

            #show messagebox
            messagebox.showinfo("Info", "Berhasil Menghapus Data. \nSilahkan Menekan Tombol 'Submit' \nUntuk Memperbaharui Tampilan Jadwal")
            #mylist.delete(tk.ANCHOR)

            conn.commit()
            conn.close()


    def raise_frame(self, fname):
        fname.tkraise()

    def run(self):
        self.raise_frame(self.frame2)
        self.jadwal.mainloop()

# e = jadwalTutor()
# e.run()