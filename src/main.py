import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
import sqlite3
from tkinter.ttk import Combobox
import mysql.connector as mysql

from jadwalTutor import *
from searchTutor import *
from pemesanan import *
from home import *

from akunMain import *


def raise_frame(fname):
    fname.tkraise()


def main_run():

    HEIGHT = 670
    WIDTH = 800

    main = tk.Tk()

    # create canvas
    canvas = tk.Canvas(main, height=HEIGHT, width=WIDTH)
    canvas.pack()

    # create frame
    # halaman form jadwal tutor
    frame = tk.Frame(main, bg='#80c1ff', bd=2)
    frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

    # halaman jadwal tutor
    frame2 = tk.Frame(main, bg='#80c1ff', bd=2)  # ini buat lihat calender
    frame2.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

    #
    frame3 = tk.Frame(main, bg='#80c1ff', bd=2)
    frame3.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

    # Halaman Main
    frame4 = tk.Frame(main, bg='#80c1ff', bd=2)
    frame4.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

    # search tutor
    frame5 = tk.Frame(main, bg='#80c1ff', bd=2)
    frame5.place(relwidth=0.9, relheight=0.3, relx=0.05, rely=0.05)

    # lower search tutor
    frame6 = tk.Frame(main, bg='#80c1ff', bd=2)
    frame6.place(relwidth=0.9, relheight=0.6, relx=0.05, rely=0.35)

    # Kehadiran
    frame7 = tk.Frame(main, bg='#80c1ff', bd=2)
    frame7.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

    # ==============frame1===================
    label1 = tk.Label(frame, text="Form Jadwal Tutor", bg='#80c1ff', font=50)
    label1.place(relx=0.4, rely=0)

    # username/ID
    label2 = tk.Label(frame, text='ID', font=40, bg='#80c1ff')
    label2.place(relx=0.1, rely=0.1)

    textbox1s = tk.Entry(frame, font=40)
    textbox1s.place(relx=0.3, rely=0.1, relwidth=0.6)

    # nama
    label3 = tk.Label(frame, text='Nama', font=40, bg='#80c1ff')
    label3.place(relx=0.1, rely=0.15)

    textbox3s = tk.Entry(frame, font=40)
    textbox3s.place(relx=0.3, rely=0.15, relwidth=0.6)

    # jenjang pendidikan mapel
    label4 = tk.Label(frame, text='Jenjang ', font=40, bg='#80c1ff')
    label4.place(relx=0.1, rely=0.20)

    varje2 = tk.IntVar()
    jeng1 = tk.Radiobutton(frame, text="SMP", variable=varje2, value=1)
    jeng1.place(relx=0.3, rely=0.2)

    jeng2 = tk.Radiobutton(frame, text="SMA", variable=varje2, value=2)
    jeng2.place(relx=0.5, rely=0.2)

    # tingkat
    label4 = tk.Label(frame, text='Tingkat', font=40, bg='#80c1ff')
    label4.place(relx=0.1, rely=0.25)

    varting2 = tk.IntVar()
    ting1 = tk.Radiobutton(frame, text="Kelas 1", variable=varting2, value=1)
    ting1.place(relx=0.3, rely=0.25)

    ting2 = tk.Radiobutton(frame, text="Kelas 2", variable=varting2, value=2)
    ting2.place(relx=0.5, rely=0.25)

    ting3 = tk.Radiobutton(frame, text="Kelas 3", variable=varting2, value=3)
    ting3.place(relx=0.7, rely=0.25)

    # matapelajaran
    label4 = tk.Label(frame, text='Mata Pelajaran', font=40, bg='#80c1ff')
    label4.place(relx=0.1, rely=0.3)

    mapelAva = ('Biologi', 'Matematika', 'Fisika', 'Kimia', 'Ekonomi', 'Sosiologi', 'Geografi',
                'Bahasa Inggris', 'Bahasa Indonesia', 'Sejarah')
    varmapel2 = tk.StringVar()
    mapelEntry = Combobox(frame, value=mapelAva,
                          textvariable=varmapel2, state="readonly")
    mapelEntry.place(relx=0.3, rely=0.3, relwidth=0.6)

    # durasi
    label4 = tk.Label(frame, text='Durasi', font=40, bg='#80c1ff')
    label4.place(relx=0.1, rely=0.35)

    vardur2 = tk.IntVar()
    dur1 = tk.Radiobutton(frame, text="1 Jam", variable=vardur2, value=1)
    dur1.place(relx=0.3, rely=0.35)

    dur2 = tk.Radiobutton(frame, text="2 Jam", variable=vardur2, value=2)
    dur2.place(relx=0.5, rely=0.35)

    # hari
    label4 = tk.Label(frame, text='Hari ', font=40, bg='#80c1ff')
    label4.place(relx=0.1, rely=0.4)

    hariAva = ('Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu')
    varhari2 = tk.StringVar()
    hariEntry = Combobox(frame, value=hariAva,
                         textvariable=varhari2, state="readonly")
    hariEntry.place(relx=0.3, rely=0.4, relwidth=0.6)

    # jam
    label4 = tk.Label(frame, text='Jam Mulai', font=40, bg='#80c1ff')
    label4.place(relx=0.1, rely=0.45)

    varjam2 = tk.StringVar()
    jamAva = ('08.00 WIB', '09.00 WIB', '10.00 WIB', '11.00 WIB', '12.00 WIB', '13.00 WIB', '14.00 WIB', '15.00 WIB',
              '16.00 WIB', '17.00 WIB', '18.00 WIB', '19.00 WIB', '20.00 WIB')
    jamEntry = Combobox(frame, value=jamAva,
                        textvariable=varjam2, state="readonly")
    jamEntry.place(relx=0.3, rely=0.45, relwidth=0.6)

    # deskripsi
    label4 = tk.Label(frame, text='Deskripsi', font=40, bg='#80c1ff')
    label4.place(relx=0.1, rely=0.5)

    textbox4s = tk.Entry(frame, font=25)
    textbox4s.place(relx=0.3, rely=0.5, relwidth=0.6, relheight=0.25)

    # fungsiantara
    def saveFormAntara():
        saveForm(int(textbox1s.get()), textbox3s.get(), varje2.get(), varting2.get(
        ), varmapel2.get(), vardur2.get(), varhari2.get(), varjam2.get(), textbox4s.get())

    buttonsave = tk.Button(frame, text="Submit Form",
                           bd=2, command=saveFormAntara)
    buttonsave.place(relx=0.75, rely=0.8)

    button2 = tk.Button(frame, text="Back", bd=2,
                        command=lambda: raise_frame(frame2))
    button2.place(relx=0.65, rely=0.8)

    # ==============frame2===================
    labelf1 = tk.Label(frame2, text="Jadwal Tutor", bg='#80c1ff', font=50)
    labelf1.place(relx=0.4, rely=0)

    labelf2 = tk.Label(frame2, text='My ID', font=40, bg='#80c1ff')
    labelf2.place(relx=0.1, rely=0.1)

    varid = tk.StringVar()
    textboxf1 = tk.Entry(frame2, font=25, textvariable=varid)
    textboxf1.place(relx=0.2, rely=0.1, relwidth=0.5)

    scrollbar = tk.Scrollbar(frame2, orient=tk.VERTICAL)
    scrollbar.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.7)

    mylist2 = tk.Listbox(frame2, yscrollcommand=scrollbar.set, font=40)
    mylist2.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.7)
    # mylist.insert(tk.END,'1')

    scrollbar.config(command=mylist2.yview)

    # fungsi antara
    def ScheduleShow():
        showSchedule(mylist2, varid.get())

    buttonf1 = tk.Button(frame2, text="Submit", bd=2, command=ScheduleShow)
    buttonf1.place(relx=0.75, rely=0.1)
    # print(textboxf1.get())

    buttonf2 = tk.Button(frame2, text="Add Schedule", bd=2,
                         command=lambda: raise_frame(frame))
    buttonf2.place(relx=0.75, rely=0.93)

    # fungsi antara
    def deleteSchedule():
        deleteJadwal(mylist2, varid.get())

    buttonf3 = tk.Button(
        frame2, text="Delete Selected Schedule", bd=2, command=deleteSchedule)
    buttonf3.place(relx=0.5, rely=0.93)

    button2 = tk.Button(frame2, text="Back", bd=2,
                        command=lambda: raise_frame(frame4))
    button2.place(relx=0.25, rely=0.93)

    # #==============frame5===================
    # judul
    label1 = tk.Label(frame5, text="Search Tutor", bg='#80c1ff', font=40)
    label1.place(relx=0.4, rely=0)

    # matapelajaran
    label4 = tk.Label(frame5, text='Mata Pelajaran', font=40, bg='#80c1ff')
    label4.place(relx=0.1, rely=0.2)

    mapelAva = ('Biologi', 'Matematika', 'Fisika', 'Kimia', 'Ekonomi', 'Sosiologi', 'Geografi',
                'Bahasa Inggris', 'Bahasa Indonesia', 'Sejarah')
    varmapel = tk.StringVar()
    mapelEntry = Combobox(frame5, value=mapelAva,
                          textvariable=varmapel, state="readonly")
    mapelEntry.place(relx=0.3, rely=0.2, relwidth=0.6)

    # jenjang pendidikan mapel
    label2 = tk.Label(frame5, text='Jenjang ', font=40, bg='#80c1ff')
    label2.place(relx=0.1, rely=0.35)

    varje = tk.IntVar()
    jeng1 = tk.Radiobutton(frame5, text="SMP", variable=varje, value=1)
    jeng1.place(relx=0.3, rely=0.35)

    jeng2 = tk.Radiobutton(frame5, text="SMA", variable=varje, value=2)
    jeng2.place(relx=0.5, rely=0.35)

    # tingkat
    label3 = tk.Label(frame5, text='Tingkat', font=40, bg='#80c1ff')
    label3.place(relx=0.1, rely=0.5)

    varting = tk.IntVar()
    ting1 = tk.Radiobutton(frame5, text="Kelas 1", variable=varting, value=1)
    ting1.place(relx=0.3, rely=0.5)

    ting2 = tk.Radiobutton(frame5, text="Kelas 2", variable=varting, value=2)
    ting2.place(relx=0.5, rely=0.5)

    ting3 = tk.Radiobutton(frame5, text="Kelas 3", variable=varting, value=3)
    ting3.place(relx=0.7, rely=0.5)

    # hari
    label5 = tk.Label(frame5, text='Hari ', font=40, bg='#80c1ff')
    label5.place(relx=0.1, rely=0.65)

    hariAva = ('Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu')
    varhari = tk.StringVar()
    hariEntry = Combobox(frame5, value=hariAva,
                         textvariable=varhari, state="readonly")
    hariEntry.place(relx=0.3, rely=0.65, relwidth=0.6)

    # # #==============frame6===================
    scrollbar = tk.Scrollbar(frame6, orient=tk.VERTICAL)
    scrollbar.place(relx=0.05, rely=0, relwidth=0.9, relheight=0.85)

    mylist = tk.Listbox(frame6, yscrollcommand=scrollbar.set)
    mylist.place(relx=0.05, rely=0, relwidth=0.9, relheight=0.85)

    scrollbar.config(command=mylist.yview)

    def searchTutorAntara():
        searchTutor(mylist, varje.get(), varting.get(),
                    varmapel.get(), varhari.get())

    button = tk.Button(frame5, text="Search", bd=2, command=searchTutorAntara)
    button.place(relx=0.75, rely=0.8)

    def konfirmasiPemesanan():
        MsgBox = messagebox.askquestion(
            "askquestion", "Apakah Ada Yakin Ingin Melakukan Pemesanan?")

    button2 = tk.Button(frame6, text="Pesan Tutor", bd=2,
                        command=konfirmasiPemesanan)
    button2.place(relx=0.75, rely=0.9)

    button2 = tk.Button(frame6, text="Back", bd=2,
                        command=lambda: raise_frame(frame4))
    button2.place(relx=0.5, rely=0.9)

    # #==============frame7===================

    labelf1 = tk.Label(frame7, text="Kehadiran", bg='#80c1ff', font=50)
    labelf1.place(relx=0.45, rely=0.1)

    labelf2 = tk.Label(frame7, text='Course ID', font=40, bg='#80c1ff')
    labelf2.place(relx=0.1, rely=0.2)

    textboxf1 = tk.Entry(frame7, font=25)
    textboxf1.place(relx=0.23, rely=0.2, relwidth=0.5)

    tv = ttk.Treeview(frame7, columns=(1, 2, 3, 4),
                      show="headings", height="5")
    tv.place(relx=0, rely=0.4, relwidth=1, relheight=0.45)
    # tv.pack()

    arrays = [['INV-001', 'Openlane', '05/10/2020', 'Attended'],
              ['INV-002', 'Gogozoom', '05/10/2020', 'Attended'],
              ['INV-003', 'Nam-zim', '05/10/2020', 'Missed']]

    tv.heading(1, text="Course ID")
    tv.heading(2, text="Tutor Name")
    tv.heading(3, text="Course Date")
    tv.heading(4, text="Status")

    for i in arrays:
        tv.insert('', 'end', values=i)

    # fungsi antara
    # def textboxf1F():
    #     showSchedule(mylist, textboxf1.get())

    # buttonf1 = tk.Button(frame7, text="Submit", bd=2, command=textboxf1F)
    # buttonf1.place(relx=0.8, rely=0.2)
    button2 = tk.Button(frame7, text="Back", bd=2,
                        command=lambda: raise_frame(frame4))
    button2.place(relx=0.8, rely=0.9)
    # print(textboxf1.get())

    # #==============frame4===================

    labelf1 = tk.Label(frame4, text="Tutorin Application",
                       bg='#80c1ff', font=50)
    labelf1.place(relx=0.4, rely=0)

    buttonf1 = tk.Button(frame4, text="Jadwal Tutor", bd=2,
                         command=lambda: raise_frame(frame2))
    buttonf1.place(relx=0.65, rely=0.1)

    buttonf2 = tk.Button(frame4, text="Search Tutor", bd=2, command=lambda: [
                         raise_frame(frame5), raise_frame(frame6)])
    buttonf2.place(relx=0.5, rely=0.1)

    #
    def goto_pesanan():
        Pemesanan.makeForm()

    buttonf3 = tk.Button(frame4, text="Pemesanan", bd=2, command=goto_pesanan)
    buttonf3.place(relx=0.35, rely=0.1)

    buttonf4 = tk.Button(frame4, text="Kehadiran", bd=2,
                         command=lambda: raise_frame(frame7))
    buttonf4.place(relx=0.2, rely=0.1)

    buttonf5 = tk.Button(frame4, text="Edit Akun", bd=2, command=editRun)
    buttonf5.place(relx=0, rely=0.1)

    raise_frame(frame4)
    main.mainloop()
