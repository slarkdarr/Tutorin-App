from tkinter import *
from tkinter import ttk
root = Tk()

# my_label = Label(root, text="Hello world")


window = Canvas(root, width=800, height=150, bg="white")

window.pack()


frameJudul = Frame(window, bg="white")
frameJudul.place(rely=0.05, relx=0.5, relheight=0.5,
                 relwidth=0.8, anchor='e')
judul = Label(frameJudul, bg="white", text="Attendance")
judul.place(relheight=1, relwidth=1)

# frameTabel = Frame(root, bg="white")
# frameTabel.place(rely=0.2, relx=0.5, relheight=0.1,
#                  relwidth=0.8, anchor='n')
# tabel = Label(frameTabel, bg="white", text="Kehadiran")
# tabel.place(relheight=1, relwidth=1)


arrays = [['INV-001', 'Openlane', '05/10/2020', 'Attended'],
          ['INV-002', 'Gogozoom', '05/10/2020', 'Attended'],
          ['INV-003', 'Nam-zim', '05/10/2020', 'Missed']]


style = ttk.Style()
style.configure("Treeview",
                foreground="skyblue"
                )

tv = ttk.Treeview(root, columns=(1, 2, 3, 4), show="headings", height="5")
tv.pack()

tv.heading(1, text="Course ID")
tv.heading(2, text="Tutor Name")
tv.heading(3, text="Course Date")
tv.heading(4, text="Status")

for i in arrays:
    tv.insert('', 'end', values=i)


def tampilan_button():
    return Button(root, text="click here", command=my_click,
                  fg="black", bg="skyblue").pack()


def my_click():
    my_label = Label(root, text="hello").pack()


my_button = Button(root, text="click here", command=my_click,
                   fg="black", bg="skyblue").pack()


root.mainloop()
