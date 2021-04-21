import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
import sqlite3
from tkinter.ttk import Combobox
import mysql.connector as mysql 
from tkinter import *
# import sys
# import os

# if os.environ.get('DISPLAY','') == '':
#     print('no display found. Using :0.0')
#     os.environ.__setitem__('DISPLAY', ':0.0')

from jadwalTutor import * 
from searchTutor import *
from pemesanan import *
from home import *
from loginModule import *

def raise_frame(fname):
    fname.tkraise()

HEIGHT = 670
WIDTH = 800

main = tk.Tk()

#create canvas
canvas = tk.Canvas(main, height = HEIGHT, width = WIDTH)
canvas.pack()

#
frame3 = tk.Frame(main, bg = '#80c1ff', bd = 2)
frame3.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)


# #==============frame3===================

labelf1 = tk.Label(frame3, text="Tutorin Application", bg = '#80c1ff', font=50)
labelf1.place(relx=0.4, rely=0)
# fungsi antara
def loginAntara(): 
    isLogin = login()
    print(isLogin)
buttonf1 = tk.Button(frame3, text="Login", bd=2, command=loginAntara)
buttonf1.place(relx=0.75, rely=0.1)
# if isLogin : 
#     lambda:raise_frame(frame4)
buttonf2 = tk.Button(frame3, text="Register Murid", bd=2, command=registerM)
buttonf2.place(relx=0.5, rely=0.1)


buttonf3 = tk.Button(frame3, text="Register Tutor", bd=2, command=registerT)
buttonf3.place(relx=0.25, rely=0.1)

raise_frame(frame3)
main.mainloop()