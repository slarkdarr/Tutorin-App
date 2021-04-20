from datetime import datetime
import tkinter as tk
import tkinter.messagebox
from databasePemesanan import *
from tkinter.ttk import *

class Pemesanan(tk.Frame):
	def __init__(self, master=None, orderID=12345678, muridID=12345678, tutorID=12345678, courseID=12345678, waktuMengajar=datetime.now(), nominal=0, statusPembayaran=False):
		# If master is none
		super().__init__(master)
		self.master = master

		# Initialize attributes for Pemesanan
		self.orderID = orderID
		self.muridID = muridID
		self.tutorID = tutorID
		self.courseID = courseID
		self.waktuMengajar = waktuMengajar
		self.nominal = nominal
		self.statusPembayaran = statusPembayaran

		# List of attributes value
		self.listOfPemesanan = [self.orderID, self.muridID, self.tutorID, self.courseID, self.waktuMengajar, self.nominal, self.statusPembayaran]

		# Gives windows title and size
		master.title("Form Pembayaran")
		master.geometry("800x670")
		self.pack()
		self.inputForm()

	def modifyStatusPembayaran(self, newstatus):
		self.statusPembayaran = newstatus

	def getStatusPembayaran(self):
		return self.statusPembayaran

	def getNominal(self):
		return self.nominal

	def inputForm(self):
		# Windows Title
		self.heading = tk.Label(self, text = "Form Pembayaran", bg = "grey", fg = "black", width = 500, height = 3)
		self.heading.pack()

		self.fields = ("Order ID", "Murid ID", "Tutor ID", "Course ID", "Waktu Mengajar", "Nominal")

		# Print form template
		i = 0
		for field in self.fields:
			self.row = Frame(self)
			self.label1 = tk.Label(self.row, width=25, text=field, anchor='w', justify='center')
			self.label2 = tk.Label(self.row, width=25, text=self.listOfPemesanan[i], anchor='e', justify='center')
			self.row.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
			self.label1.pack(side=tk.LEFT)
			self.label2.pack(side=tk.RIGHT)
			i += 1

		self.bank = ("Mandiri", "BCA", "BRI", "BNI", "CIMB Niaga")

		# Initialize bank option
		self.variable = tk.StringVar(self)
		self.variable.set("Pilih Bank")

		# Create option menu
		self.ddmenu = tk.OptionMenu(self, self.variable, *self.bank)
		self.ddmenu.pack()

		# Initialize label for option menu's description
		self.lbl = Frame(self)
		self.descLabel = tk.Label(self.lbl)

		# Show description when user chooses any option on Option Menu
		def showDesc(*args):
			self.desc = f"""
				1. Silakan transfer nominal pembayaran melalui ATM, Internet Banking, Mobile Banking, atau SMS Banking\n
				2. Masukkan Nominal Pembayaran yang sesuai dengan form pembayaran ditambah kode unik, yaitu "011"\n
				Nominal Pembayaran Anda : Rp{self.nominal:,}.00\n
				Jumlah yang harus ditransfer : Rp{self.nominal+11:,}.00\n
				3. Sertakan juga Berita Transfer yang tertera pada form pembayaran\n
				4. Klik "Konfirmasi Bayar"\n
				"""
			self.descLabel.destroy()
			# self.lbl.place(x=100, y=100)
			self.lbl.pack(side=tk.BOTTOM, padx=0, pady=0)
			self.descLabel = tk.Label(self.lbl, text=self.desc)
			self.descLabel.pack()

		self.variable.trace('w', showDesc)

		self.submit()

	# Submit button
	def submit(self):
		def submitCallBack():
			tkinter.messagebox.showinfo("Ordered", "Pemesanan telah diterima")
			self.sendForm()
		def cancelCallBack():
			tkinter.messagebox.showinfo("Canceled", "Pemesanan telah dibatalkan")
			quit()

		self.btnFrame = Frame(self)
		self.submitBtn = Button(self.btnFrame, text="Order", command=submitCallBack)
		self.cancelBtn = Button(self.btnFrame, text="Cancel", command=cancelCallBack)

		self.btnFrame.pack(side=tk.BOTTOM, padx=10, pady=10)
		self.submitBtn.pack(side=tk.LEFT, padx=10, pady=5)
		self.cancelBtn.pack(side=tk.RIGHT, padx=10, pady=5)

	# Function to send form to the database
	def sendForm(self):
		self.pemesananDB = PemesananDB()
		self.pemesananDB.insertToDatabase(self.orderID, self.muridID, self.tutorID, self.courseID, self.waktuMengajar, self.nominal, self.statusPembayaran)
		self.pemesananDB.closeDatabase()

# Main Function (To make the form and its GUI)
def makeForm():
	window = tk.Tk()
	app = Pemesanan(master=window)
	app.modifyStatusPembayaran(True)
	app.mainloop()

makeForm()
