import tkinter as tk
from tkinter import messagebox
import csv
import sqlite3
from tkinter.ttk import Combobox
import mysql.connector as mysql 

def getIntJam(jam):
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

def PrintArray(arr):
    for x in arr:
        print(x)

def getID(data, mapel, ting, jen):
    for x in data:
        if(x[1] == mapel and x[2] == jen and x[3] == ting):
            return x[0]
    return 0

def getID2(data, data2) :
    for x in data:
        if(x == data2):
            return x[0]
    return 0

def message(title, text):
   tk.MessageBox.showinfo(title, text)

def saveForm():
    # conn = sqlite3.connect('Tutorin.db')
    # c = conn.cursor()
    
    conn = mysql.connect(host="localhost", user="root", password="", database="tutorin")
    c = conn.cursor()

    id = int(textbox1.get())
    nama = textbox3.get()
    jen = ""
    if(int(varje.get()) == 1) :
        jen = "SMP"
    elif(int(varje.get()) == 2) :
        jen = "SMA"
    ting = varting.get()
    mapel = varmapel.get()
    durasi = vardur.get()
    hari = varhari.get()
    jam = getIntJam(varjam.get())
    desc = textbox4.get()
    if(desc == ""):
        desc = "Tidak Ada"
    #id, nama, jenjang, tingkat, mapel, durasi, hari, jam, des
    if(id=="" or nama=="" or jen=="" or ting==0 or durasi==0 or mapel =="" or hari=="" or jam==0):
        #show messagebox
        messagebox.showerror("Error", "Data Tidak Lengkap.\nCek Kembali Data Anda!")
        #print("gagal")
    else:
        #dapetin IDcourse
        c.execute("SELECT * FROM detailcourse")
        data = c.fetchall()
        courseid = getID(data, mapel, ting, jen)

        #print(courseid)
        nrow = [id,courseid,hari,jam,durasi,desc]
        print(nrow)
        #insert data to database
        # c.execute("INSERT INTO JadwalTutor VALUES (id,courseid,'"+courseid+"'")")
        # print("(",id,",",courseid,",'" +hari +"',",jam,",",durasi,",'"+ desc +"')")
        c.execute("insert into jadwaltutor(tutorid, courseid, hari, jamMulai, durasi, deskripsi) values(",id,",",courseid,",'"+hari+"',",jam,",",durasi,",'"+desc+"')")
        
        #show messagebox
        messagebox.showinfo("Info", "Berhasil Menyimpan Data")
        #print("sukses")
    conn.commit()
    conn.close()

def raise_frame(fname):
    fname.tkraise()
    


HEIGHT = 670
WIDTH = 800

jadwal = tk.Tk()

#create canvas
canvas = tk.Canvas(jadwal, height = HEIGHT, width = WIDTH)
canvas.pack()


#create frame
frame = tk.Frame(jadwal, bg = '#80c1ff', bd = 2)
frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

frame2 = tk.Frame(jadwal, bg = '#80c1ff', bd = 2) #ini buat lihat calender
frame2.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)


#==============frame1===================
label1 = tk.Label(frame, text="Form Jadwal Tutor", bg = '#80c1ff', font=50)
label1.place(relx=0.4, rely=0)

#username/ID
label2 = tk.Label(frame, text='ID', font=40, bg = '#80c1ff')
label2.place(relx=0.1, rely=0.1)

textbox1 = tk.Entry(frame, font=40)
textbox1.place(relx=0.3, rely=0.1, relwidth=0.6)

#nama
label3 = tk.Label(frame, text='Nama', font=40, bg = '#80c1ff')
label3.place(relx=0.1, rely=0.15)

textbox3 = tk.Entry(frame, font=40)
textbox3.place(relx=0.3, rely=0.15, relwidth=0.6)

#jenjang pendidikan mapel
label4 = tk.Label(frame, text='Jenjang ', font=40, bg = '#80c1ff')
label4.place(relx=0.1, rely=0.20)

varje = tk.IntVar()
jeng1 = tk.Radiobutton(frame, text="SMP", variable=varje, value=1)
jeng1.place(relx=0.3, rely=0.2)

jeng2 = tk.Radiobutton(frame, text="SMA", variable=varje, value=2)
jeng2.place(relx=0.5, rely=0.2)

#tingkat
label4 = tk.Label(frame, text='Tingkat', font=40, bg = '#80c1ff')
label4.place(relx=0.1, rely=0.25)

varting = tk.IntVar()
ting1 = tk.Radiobutton(frame, text="Kelas 1", variable=varting, value=1)
ting1.place(relx=0.3, rely=0.25)

ting2 = tk.Radiobutton(frame, text="Kelas 2", variable=varting, value=2)
ting2.place(relx=0.5, rely=0.25)

ting3 = tk.Radiobutton(frame, text="Kelas 3", variable=varting, value=3)
ting3.place(relx=0.7, rely=0.25)

#matapelajaran
label4 = tk.Label(frame, text='Mata Pelajaran', font=40, bg = '#80c1ff')
label4.place(relx=0.1, rely=0.3)

mapelAva = ('Biologi', 'Matematika', 'Fisika', 'Kimia', 'Ekonomi', 'Sosiologi', 'Geografi', 
            'Bahasa Inggris', 'Bahasa Indonesia', 'Sejarah')
varmapel = tk.StringVar()
mapelEntry = Combobox(frame, value=mapelAva, textvariable = varmapel,state="readonly")
mapelEntry.place(relx=0.3, rely=0.3, relwidth=0.6)

#durasi
label4 = tk.Label(frame, text='Durasi', font=40, bg = '#80c1ff')
label4.place(relx=0.1, rely=0.35)

vardur = tk.IntVar()
dur1 = tk.Radiobutton(frame, text="1 Jam", variable=vardur, value=1)
dur1.place(relx=0.3, rely=0.35)

dur2 = tk.Radiobutton(frame, text="2 Jam", variable=vardur, value=2)
dur2.place(relx=0.5, rely=0.35)

#hari
label4 = tk.Label(frame, text='Hari ', font=40, bg = '#80c1ff')
label4.place(relx=0.1, rely=0.4)

hariAva = ('Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu',)
varhari = tk.StringVar()
hariEntry = Combobox(frame, value=hariAva, textvariable = varhari,state="readonly")
hariEntry.place(relx=0.3, rely=0.4, relwidth=0.6)
              

#jam
label4 = tk.Label(frame, text='Jam Mulai', font=40, bg = '#80c1ff')
label4.place(relx=0.1, rely=0.45)

varjam = tk.StringVar()
jamAva = ('08.00 WIB', '09.00 WIB','10.00 WIB','11.00 WIB','12.00 WIB','13.00 WIB','14.00 WIB','15.00 WIB',
            '16.00 WIB','17.00 WIB','18.00 WIB','19.00 WIB','20.00 WIB')
jamEntry = Combobox(frame, value=jamAva, textvariable = varjam, state="readonly")
jamEntry.place(relx=0.3, rely=0.45, relwidth=0.6)

#deskripsi
label4 = tk.Label(frame, text='Deskripsi', font=40, bg = '#80c1ff')
label4.place(relx=0.1, rely=0.5)

textbox4 = tk.Entry(frame, font=25)
textbox4.place(relx=0.3, rely=0.5, relwidth=0.6, relheight=0.25)

button = tk.Button(frame, text="Submit Form", bd=2, command=saveForm)
button.place(relx=0.75, rely=0.8)

button2 = tk.Button(frame, text="Back", bd=2, command=lambda:raise_frame(frame2))
button2.place(relx=0.65, rely=0.8)

#======frame2=====
def showSchedule(list) :
    conn = sqlite3.connect('Tutorin.db')
    c = conn.cursor()

    #tampilkan schedule dari tutor
    id = textboxf1.get()

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

def deleteJadwal(list):
    MsgBox = messagebox.askquestion("askquestion", "Are you sure?")
    if (MsgBox == 'yes'):
        conn = sqlite3.connect('Tutorin.db')
        c = conn.cursor()

        id = textboxf1.get()
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

        row = int(getID2(data, data2[i]))
        #print(row)
        #hapus data dari database
        c.execute("DELETE FROM JadwalTutor WHERE rowid = (?)",(row,))
        #print('sukses')

        #show messagebox
        messagebox.showinfo("Info", "Berhasil Menghapus Data. \nSilahkan Menekan Tombol 'Submit' \nUntuk Memperbaharui Tampilan Jadwal")
        #mylist.delete(tk.ANCHOR)

        conn.commit()
        conn.close()


labelf1 = tk.Label(frame2, text="Jadwal Tutor", bg = '#80c1ff', font=50)
labelf1.place(relx=0.4, rely=0)

labelf2 = tk.Label(frame2, text='My ID', font=40, bg = '#80c1ff')
labelf2.place(relx=0.1, rely=0.1)

textboxf1 = tk.Entry(frame2, font=25)
textboxf1.place(relx=0.2, rely=0.1, relwidth=0.5)

scrollbar = tk.Scrollbar(frame2, orient=tk.VERTICAL)
scrollbar.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.7)

mylist = tk.Listbox(frame2, yscrollcommand = scrollbar.set, font=40 )
mylist.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.7)

scrollbar.config( command = mylist.yview )

buttonf1 = tk.Button(frame2, text="Submit", bd=2, command=lambda:showSchedule(mylist))
buttonf1.place(relx=0.75, rely=0.1)

buttonf2 = tk.Button(frame2, text="Add Schedule", bd=2, command=lambda:raise_frame(frame))
buttonf2.place(relx=0.75, rely=0.93)

buttonf3 = tk.Button(frame2, text="Delete Selected Schedule", bd=2, command=lambda:deleteJadwal(mylist))
buttonf3.place(relx=0.5, rely=0.93)




raise_frame(frame2)
jadwal.mainloop()