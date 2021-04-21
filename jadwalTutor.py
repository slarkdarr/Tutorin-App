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

def saveForm(textbox1, textbox3, varje, varting, varmapel, vardur, varhari, varjam, textbox4): 
    conn = mysql.connect(host="localhost", user="root", password="", database="tutorin")
    c = conn.cursor()

    id = textbox1
    nama = textbox3
    jen = ""
    if(int(varje) == 1) :
        jen = "SMP"
    elif(int(varje) == 2) :
        jen = "SMA"
    ting = varting
    mapel = varmapel
    durasi = vardur
    hari = varhari
    jam = getIntJam(varjam)
    desc = textbox4
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
        c.execute("insert into jadwaltutor(tutorid, courseid, hari, jamMulai, durasi, deskripsi) values(",id,","+ str(courseid)+",'"+hari+"',"+str(jam)+","+ str(durasi)+",'"+desc+"')")
         #show messagebox
        messagebox.showinfo("Info", "Berhasil Menyimpan Data")
        #print("sukses")
    conn.commit()
    conn.close()

def raise_frame(fname):
    fname.tkraise()
    


# HEIGHT = 670
# WIDTH = 800

# jadwal = tk.Tk()

# #create canvas
# canvas = tk.Canvas(jadwal, height = HEIGHT, width = WIDTH)
# canvas.pack()


#======frame2=====
def showSchedule(list, textf1) :
    conn = sqlite3.connect('Tutorin.db')
    c = conn.cursor()
    # conn = mysql.connect(host="localhost", user="root", password="", database="tutorin")
    # c = conn.cursor()
    

    #tampilkan schedule dari tutor
    #print(textf1)
    id = textf1

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

