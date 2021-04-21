import tkinter as tk
from tkinter import messagebox
import csv
import sqlite3
from tkinter.ttk import Combobox
import mysql.connector as mysql

from akunModule import AkunMurid, AkunTutor, UpdateAkun

app = AkunTutor("dwi")
app.run()
