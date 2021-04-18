from datetime import datetime
import tkinter as tk
from tkinter.ttk import *

class Pemesanan(tk.Frame):
	def __init__(self, master=None, orderID=1234567890, muridID=1234567890, tutorID=1234567890, courseID=1234567890, waktuMengajar=datetime.now(), nominal=0, statusPembayaran=False):
		super().__init__(master)
		self.master = master

		self.orderID = orderID
		self.muridID = muridID
		self.tutorID = tutorID
		self.courseID = courseID
		self.waktuMengajar = waktuMengajar
		self.nominal = nominal
		self.statusPembayaran = statusPembayaran
		
		master.title("Form Pembayaran")
		master.geometry("500x500")
		self.pack()
		self.inputForm()

	def modifyStatusPembayaran(self, newstatus):
		self.statusPembayaran = newstatus

	def getStatusPembayaran(self):
		return self.statusPembayaran

	def getNominal(self):
		return self.nominal

	def inputForm(self):
		self.heading = tk.Label(self, text = "Form Pembayaran", bg = "grey", fg = "black", width = 500, height = 3)
		self.heading.pack()

		self.fields = ("Order ID", "Murid ID", "Tutor ID", "Course ID", "Waktu Mengajar", "Nominal")

		# Style().configure("OrderID", padding=5, relief="flat")
		for field in self.fields:
			self.row = Frame(self)
			self.label1 = tk.Label(self.row, width=25, text=field, anchor='w')
			self.label2 = tk.Label(self.row, width=25, text=0, anchor='e')
			self.row.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
			self.label1.pack(side=tk.LEFT)
			self.label2.pack(side=tk.RIGHT)
			# self.murid_id = tk.Label(self, width=25, text = "Murid ID", anchor='w')
			# self.order_id.pack(side=tk.LEFT)

		self.bank = ("Mandiri", "BCA", "BRI", "BNI", "CIMB Niaga")

		self.variable = tk.StringVar(self)
		self.variable.set("Pilih Bank")
		# menuFrame = Frame(self)
		self.ddmenu = tk.OptionMenu(self, self.variable, *self.bank)
		self.ddmenu.pack()

		def showDesc(*args):
			self.desc = """
			1. Silakan transfer nominal pembayaran melalui ATM, Internet Banking, Mobile Banking, atau SMS Banking\n
			2. Masukkan Nominal Pembayaran yang sesuai dengan form pembayaran ditambah kode unik, yaitu "011"\n
			Contoh : Nominal Pembayaran : Rp100.000,00\n
			Jumlah yang harus ditransfer : 100011\n
			3. Sertakan juga Berita Transfer yang tertera pada form pembayaran\n
			4. Klik "Konfirmasi Bayar"\n
			"""
			self.lbl = Frame(self)
			self.descLabel = tk.Label(self.lbl, text=self.desc, justify=tk.CENTER)
			self.lbl.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
			self.descLabel.pack()

		# self.descLabel = tk.Label(self, text=self.desc)
		self.variable.trace('w', showDesc)
		# self.descLabel.pack()

	# def sendForm():
	# 	pass

window = tk.Tk()
app = Pemesanan(master=window)
app.mainloop()
