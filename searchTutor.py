import tkinter as tk
import csv

HEIGHT = 670
WIDTH = 800

search = tk.Tk()

#create canvas
canvas = tk.Canvas(search, height = HEIGHT, width = WIDTH)
canvas.pack()

#create frame
frame = tk.Frame(canvas, bg = '#80c1ff', bd = 2)
frame.place(relwidth=0.9, relheight=0.3, relx=0.05, rely=0.05)

lower_frame = tk.Frame(search, bg = '#80c1ff', bd = 2)
lower_frame.place(relwidth=0.9, relheight=0.6, relx=0.05, rely=0.35)

#judul
label1 = tk.Label(frame, text="Search Tutor", bg = '#80c1ff', font=40)
label1.place(relx=0.4, rely=0)

#matapelajaran
label4 = tk.Label(frame, text='Mata Pelajaran', font=40, bg = '#80c1ff')
label4.place(relx=0.1, rely=0.2)

mapelAva = ('Biologi', 'Matematika', 'Fisika', 'Kimia', 'Ekonomi', 'Sosiologi', 'Geografi', 
            'Bahasa Inggris', 'Bahasa Indonesia', 'Sejarah')
varmapel = tk.StringVar()
mapelEntry = tk.Spinbox(frame, value=mapelAva, textvariable = varmapel)
mapelEntry.place(relx=0.3, rely=0.2, relwidth=0.6)

#jenjang pendidikan mapel
label2 = tk.Label(frame, text='Jenjang ', font=40, bg = '#80c1ff')
label2.place(relx=0.1, rely=0.35)

varje = tk.IntVar()
jeng1 = tk.Radiobutton(frame, text="SMP", variable=varje, value=1)
jeng1.place(relx=0.3, rely=0.35)

jeng2 = tk.Radiobutton(frame, text="SMA", variable=varje, value=2)
jeng2.place(relx=0.5, rely=0.35)

#tingkat
label3 = tk.Label(frame, text='Tingkat', font=40, bg = '#80c1ff')
label3.place(relx=0.1, rely=0.5)

varting = tk.IntVar()
ting1 = tk.Radiobutton(frame, text="Kelas 1", variable=varting, value=1)
ting1.place(relx=0.3, rely=0.5)

ting2 = tk.Radiobutton(frame, text="Kelas 2", variable=varting, value=2)
ting2.place(relx=0.5, rely=0.5)

ting3 = tk.Radiobutton(frame, text="Kelas 3", variable=varting, value=3)
ting3.place(relx=0.7, rely=0.5)


#hari
label5 = tk.Label(frame, text='Hari ', font=40, bg = '#80c1ff')
label5.place(relx=0.1, rely=0.65)

hariAva = ('Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu')
varhari = tk.StringVar()
hariEntry = tk.Spinbox(frame, value=hariAva, textvariable = varhari)
hariEntry.place(relx=0.3, rely=0.65, relwidth=0.6)


button = tk.Button(frame, text="Search", bd=2)
button.place(relx=0.75, rely=0.8)

#lower
# label7 = tk.Label(lower_frame)
# label7.place(relx=0.05, rely=0, relwidth=0.9, relheight=0.9)

scrollbar = tk.Scrollbar(lower_frame, orient=tk.VERTICAL)
scrollbar.place(relx=0.05, rely=0, relwidth=0.9, relheight=0.9)

mylist = tk.Listbox(lower_frame, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(tk.END,"This is line number " + str(line))

mylist.place(relx=0.05, rely=0, relwidth=0.9, relheight=0.9)
scrollbar.config( command = mylist.yview )

def searchTutor():
   x=0

search.mainloop()