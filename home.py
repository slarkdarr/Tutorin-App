from tkinter import *
import os
from loginModule import login
from registerModule import register

main_screen = Tk()

def main_account_screen():
    global main_screen
    main_screen.geometry("300x250")
    main_screen.title("Tutorin")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Montserrat", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()