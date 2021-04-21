import tkinter as tk
import csv
from tkinter.ttk import Combobox
from tkinter import messagebox
import sqlite3
import sys
import os

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

def searchTutor(list, varje, varting, varmapel, varhari):
   conn = sqlite3.connect('Tutorin.db')
   c = conn.cursor()
   list.delete(0,list.size())
   jen = ""
   if(int(varje) == 1) :
      jen = "SMP"
   elif(int(varje) == 2) :
      jen = "SMA"
   ting = varting #default = 0
   mapel = varmapel
   hari = str(varhari)
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

def konfirmasiPemesanan():
   MsgBox = messagebox.askquestion("askquestion", "Apakah Ada Yakin Ingin Melakukan Pemesanan?")

def checkSearch(list, varje, varting, varmapel, varhari):
   searchTutor(list, varje, varting, varmapel, varhari)
   if(list.size == 0):
      return 0 #listbox kosong, pencarian tidak berhasil
   return 1 #pencarian berhasil

# HEIGHT = 670
# WIDTH = 800

# search = tk.Tk()

# #create canvas
# canvas = tk.Canvas(search, height = HEIGHT, width = WIDTH)
# canvas.pack()

# #create frame
# frame = tk.Frame(canvas, bg = '#80c1ff', bd = 2)
# frame.place(relwidth=0.9, relheight=0.3, relx=0.05, rely=0.05)

# lower_frame = tk.Frame(search, bg = '#80c1ff', bd = 2)
# lower_frame.place(relwidth=0.9, relheight=0.6, relx=0.05, rely=0.35)

# #judul
# label1 = tk.Label(frame, text="Search Tutor", bg = '#80c1ff', font=40)
# label1.place(relx=0.4, rely=0)

# #matapelajaran
# label4 = tk.Label(frame, text='Mata Pelajaran', font=40, bg = '#80c1ff')
# label4.place(relx=0.1, rely=0.2)

# mapelAva = ('Biologi', 'Matematika', 'Fisika', 'Kimia', 'Ekonomi', 'Sosiologi', 'Geografi', 
#             'Bahasa Inggris', 'Bahasa Indonesia', 'Sejarah')
# varmapel = tk.StringVar()
# mapelEntry = Combobox(frame, value=mapelAva, textvariable = varmapel, state="readonly")
# mapelEntry.place(relx=0.3, rely=0.2, relwidth=0.6)

# #jenjang pendidikan mapel
# label2 = tk.Label(frame, text='Jenjang ', font=40, bg = '#80c1ff')
# label2.place(relx=0.1, rely=0.35)

# varje = tk.IntVar()
# jeng1 = tk.Radiobutton(frame, text="SMP", variable=varje, value=1)
# jeng1.place(relx=0.3, rely=0.35)

# jeng2 = tk.Radiobutton(frame, text="SMA", variable=varje, value=2)
# jeng2.place(relx=0.5, rely=0.35)

# #tingkat
# label3 = tk.Label(frame, text='Tingkat', font=40, bg = '#80c1ff')
# label3.place(relx=0.1, rely=0.5)

# varting = tk.IntVar()
# ting1 = tk.Radiobutton(frame, text="Kelas 1", variable=varting, value=1)
# ting1.place(relx=0.3, rely=0.5)

# ting2 = tk.Radiobutton(frame, text="Kelas 2", variable=varting, value=2)
# ting2.place(relx=0.5, rely=0.5)

# ting3 = tk.Radiobutton(frame, text="Kelas 3", variable=varting, value=3)
# ting3.place(relx=0.7, rely=0.5)


# #hari
# label5 = tk.Label(frame, text='Hari ', font=40, bg = '#80c1ff')
# label5.place(relx=0.1, rely=0.65)

# hariAva = ('Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu')
# varhari = tk.StringVar()
# hariEntry = Combobox(frame, value=hariAva, textvariable = varhari, state="readonly")
# hariEntry.place(relx=0.3, rely=0.65, relwidth=0.6)


# #lower
# scrollbar = tk.Scrollbar(lower_frame, orient=tk.VERTICAL)
# scrollbar.place(relx=0.05, rely=0, relwidth=0.9, relheight=0.85)

# mylist = tk.Listbox(lower_frame, yscrollcommand = scrollbar.set )
# mylist.place(relx=0.05, rely=0, relwidth=0.9, relheight=0.85)

# scrollbar.config( command = mylist.yview )

# button = tk.Button(frame, text="Search", bd=2, command=lambda:searchTutor(mylist))
# button.place(relx=0.75, rely=0.8)

# button2 = tk.Button(lower_frame, text="Pesan Tutor", bd=2, command=konfirmasiPemesanan)
# button2.place(relx=0.75, rely=0.9)

# search.mainloop()