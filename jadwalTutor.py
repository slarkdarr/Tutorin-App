import tkinter as tk
import csv
import sqlite3

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

def saveForm():
    id = textbox1.get()
    nama = textbox3.get()
    jenjang = ""
    if(int(varje.get()) == 1) :
        jenjang = "SMP"
    elif(int(varje.get()) == 2) :
        jenjang = "SMA"
    tingkat = varting.get()
    mapel = varmapel.get()
    durasi = vardur.get()
    hari = varhari.get()
    jam = getIntJam(varjam.get())
    desc = textbox4.get()
    if(desc == ""):
        desc = "Tidak Ada"
    #id, nama, jenjang, tingkat, mapel, durasi, hari, jam, des
    if(id=="" or nama=="" or jenjang=="" or tingkat==0 or durasi==0):
        print("gagal")
    else:
        newrow=[id,nama,jenjang,tingkat,mapel,durasi,hari,jam,desc]
        with open(r'DatabaseJadwalTutor.csv', 'a', newline='') as appendobj :
            append=csv.writer(appendobj)
            append.writerow(newrow)
        print("sukses")

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
mapelEntry = tk.Spinbox(frame, value=mapelAva, textvariable = varmapel)
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

hariAva = ('Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu')
varhari = tk.StringVar()
hariEntry = tk.Spinbox(frame, value=hariAva, textvariable = varhari)
hariEntry.place(relx=0.3, rely=0.4, relwidth=0.6)
              

#jam
label4 = tk.Label(frame, text='Jam Mulai', font=40, bg = '#80c1ff')
label4.place(relx=0.1, rely=0.45)

varjam = tk.StringVar()
jamAva = ('08.00 WIB', '09.00 WIB','10.00 WIB','11.00 WIB','12.00 WIB','13.00 WIB','14.00 WIB','15.00 WIB',
            '16.00 WIB','17.00 WIB','18.00 WIB','19.00 WIB','20.00 WIB')
jamEntry = tk.Spinbox(frame, value=jamAva, textvariable = varjam)
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
listschedule = []

def showSchedule(list) :
    #tampilkan schedule dari tutor
    id = textboxf1.get()
    array = []

    with open('DatabaseJadwalTutor.csv', 'r') as file:
        file_reader = csv.reader(file)
        for line in file_reader:
            array.append(line)

    list.delete(0,list.size())
    listschedule.clear()
    for x in array :
        text = ""
        if(x[0] == id):
            listschedule.append(x)
            text = ("Mata Pelajaran : " + x[4] + " | " + x[2] + " Kelas " + x[3] + " | Hari : " + x[6] + " | " + "Jam Mulai : " + x[7] + ".00 WIB")
            list.insert(tk.END,text)
    # for y in listschedule:
    #     print(y)

def deleteJadwal(list):
    sel = list.curselection()
    deleted = []
    array = []

    with open('DatabaseJadwalTutor.csv', 'r') as file:
        file_reader = csv.reader(file)
        for line in file_reader:
            array.append(line)
        row = list(file_reader)
    
    for x in sel:
        for y in array :
            if(listschedule[x] == y):
                array.remove(y)
        #         print(y)
        # print(x)

    # with open('DatabaseJadwalTutor.csv', 'r') as writeobj:
    #     write = csv.writer(writeobj)
    #     for x in array:
    #         newrow=[x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]] 
    #         write.writerows(newrow)
    #     #newrow = list(array)
        
    
    for x in row:
        print(x)
        #deleted.append(listschedule[x])
    # for y in deleted:
    #     print(y)
    # for y in listschedule:
    #     print("ok")


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