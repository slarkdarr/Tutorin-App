from tkinter import *
import os
from loginModule import Login, RegisterMurid, RegisterTutor



class MainWindow:
    def __init__(self):
        self.app = Tk()
        self.app.title("Tutorin")
        self.app.geometry('300x250')
        self.label = Label(self.app, text='Welcome To Tutorin')
        self.label.place(x=95, y=40)
        self.login = Button(self.app, text="Login", pady=5, padx=30, command=login)
        self.login.place(x=100, y=100)
        self.registerT = Button(self.app, text="Register as Murid", pady=5, padx=20, command=registerM)
        self.registerT.place(x=70, y=150)
        self.registerM = Button(self.app, text="Register as Tutor", pady=5, padx=20, command=registerT)
        self.registerM.place(x=70, y=200)

    def run(self):
        self.app.mainloop()
        
def login():
    loginTk = Login()
    loginTk.run()
    
def registerT():
    registerTk = RegisterTutor()
    registerTk.run()

def registerM():
    registerTk = RegisterMurid()
    registerTk.run()

