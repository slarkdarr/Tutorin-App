import mysql.connector

class PemesananDB:
	def __init__(self):
		self.conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='Pemesanan')
		self.cursor = self.conn.cursor()

	# Insert data in the form to database
	def insertToDatabase(self, orderID, muridID, tutorID, tutorName, mataPelajaran, jenjang, tingkat, hari):
		self.dbPemesanan = """
		INSERT INTO Pemesanan
		VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
		"""

		self.dataPemesanan = (orderID, muridID, tutorID, tutorName, mataPelajaran, jenjang, tingkat, hari)

		try:
			# Eksekusi command SQL
			self.cursor.execute(self.dbPemesanan, self.dataPemesanan)
			# Commit ke database
			self.conn.commit()
		except mysql.connector.errors.IntegrityError:
			print("Data can't be duplicate")
			# Rollback kalau ada error
			self.conn.rollback()
		finally:
			print("Data has been added to database")

	# Close the database
	def closeDatabase(self):
		self.conn.close()
		print("MySQL is closed")
