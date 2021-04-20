from datetime import datetime
import tkinter as tk
import tkinter.messagebox
from databasePemesanan import *
from tkinter.ttk import *

class Pemesanan(tk.Frame):
	def __init__(self, master=None, tutorID=12345678, tutorName="XXX", mataPelajaran="XXX", jenjang="XXX", tingkat=0, hari="XXX"):
		super().__init__(master)
		self.master = master

		self.tutorID = tutorID
		self.tutorName = tutorName
		self.mataPelajaran = mataPelajaran	
		self.jenjang = jenjang
		self.tingkat = tingkat
		self.hari = hari

		self.listOfPemesanan = [self.tutorID, self.tutorName, self.mataPelajaran, self.jenjang, self.tingkat, self.hari]

		master.title("Pemesanan")
		master.geometry("800x670")
		self.pack()
		self.inputForm()

	def inputForm(self):
		self.heading = tk.Label(self, text="Detail Pemesanan", bg="grey", fg="black", width=670, height=3)
		self.heading.pack()

		self.fields = ("Tutor ID", "Tutor Name", "Mata Pelajaran", "Jenjang", "Tingkat", "Hari")

		i = 0
		for field in self.fields:
			self.row = Frame(self)
			self.label1 = tk.Label(self.row, width=25, text=field, anchor='w', justify='center')
			self.label2 = tk.Label(self.row, width=25, text=self.listOfPemesanan[i], anchor='e', justify='center')
			self.row.pack(side=tk.TOP, fill=tk.X, padx=10, pady=20)
			self.label1.pack(side=tk.LEFT)
			self.label2.pack(side=tk.RIGHT)
			i += 1

		self.confirm()

	def confirm(self):
		def confirmCallBack():
			try:
				self.sendForm()
				tkinter.messagebox.showinfo("Confirmed", "Pemesanan telah diterima")
			except:
				tkinter.messagebox.showinfo("Error", "Database not found")
		def cancelCallBack():
			tkinter.messagebox.showinfo("Canceled", "Pemesanan telah dibatalkan")
			quit()

		self.btnFrame = Frame(self)
		self.submitBtn = Button(self.btnFrame, text="Confirm", command=confirmCallBack, width=20)
		self.cancelBtn = Button(self.btnFrame, text="Cancel", command=cancelCallBack, width=20)

		self.btnFrame.pack(side=tk.BOTTOM, padx=10, pady=10)
		self.submitBtn.pack(side=tk.LEFT, padx=50, pady=100)
		self.cancelBtn.pack(side=tk.RIGHT, padx=50, pady=100)

	def sendForm(self):
		self.pemesananDB = PemesananDB()
		self.pemesananDB.insertToDatabase(self.tutorID, self.tutorName, self.mataPelajaran, self.jenjang, self.tingkat, self.hari)
		self.pemesananDB.closeDatabase()

# Main Function (To make the form and its GUI)
# For the main program
# Add these parameters later : tutorID, tutorName, mataPelajaran, jenjang, tingkat, hari
def makeForm():
	window = tk.Tk()
	app = Pemesanan(master=window)
	app.mainloop()

# makeForm()
