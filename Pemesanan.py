class Pemesanan:
	def __init__(self, orderID = 1234567890, muridID = 1234567890, tutorID = 1234567890, courseID = 1234567890, waktuMengajar = datetime.datetime.now(), nominal = 0, statusPembayaran = False):
		self.orderID = orderID
		self.muridID = muridID
		self.tutorID = tutorID
		self.courseID = courseID
		self.waktuMengajar = waktuMengajar
		self.nominal = nominal
		self.statusPembayaran = statusPembayaran

	def modifyStatusPembayaran(newstatus):
		self.statusPembayaran = newstatus

	def getStatusPembayaran():
		return self.statusPembayaran

	def getNominal():
		return self.nominal

	def inputForm():
		pass

	def sendForm():
		pass
