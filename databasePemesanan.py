import mysql.connector

class PemesananDB:
	def __init__(self):
		self.conn = mysql.connector.connect(user='root', password='Gaussian021001', host='127.0.0.1', database='Pemesanan')
		self.cursor = self.conn.cursor()

	def insertToDatabase(self, orderID, muridID, tutorID, courseID, waktuMengajar, nominal, statusPembayaran):
		self.dbPemesanan = """
		INSERT INTO Test
		VALUES(%s, %s, %s, %s, %s, %s, %s)
		"""
		self.dataPemesanan = (orderID, muridID, tutorID, courseID, waktuMengajar, nominal, statusPembayaran)

		try:
			# Eksekusi command SQL
			self.cursor.execute(self.dbPemesanan, self.dataPemesanan)
			# Commit ke database
			self.conn.commit()
		except:
			# Rollback kalau ada error
			self.conn.rollback()

	def closeDatabase(self):
		self.conn.close()
