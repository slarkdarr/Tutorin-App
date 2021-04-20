import sqlite3

conn = sqlite3.connect('Tutorin.db')

c = conn.cursor()

# c.execute("DROP TABLE JadwalTutor")

# c.execute("DROP TABLE DetailCourse")

#create database JadwalTutor
# c.execute("""CREATE TABLE JadwalTutor (
#             tutorID INTEGER,
#             courseID INTEGER,
#             hari text,
#             jamMulai INTEGER,
#             durasi INTEGER,
#             deskripsi text
# )""")



# #create database DetailCourse
# c.execute("""CREATE TABLE DetailCourse (
#             namaMapel text,
#             jenjang text,
#             tingkat INTEGER
# )""")

#insert data pada detailcourse

# course = [
#             ('Biologi','SMA','1'),('Biologi','SMA','2'),('Biologi','SMA','3'),
#             ('Biologi','SMP','1'),('Biologi','SMP','2'),('Biologi','SMP','3'),
#             ('Matematika','SMA','1'),('Matematika','SMA','2'),('Matematika','SMA','3'),
#             ('Matematika','SMP','1'),('Matematika','SMP','2'),('Matematika','SMP','3'),
#             ('Fisika','SMA','1'),('Fisika','SMA','2'),('Fisika','SMA','3'),
#             ('Fisika','SMP','1'),('Fisika','SMP','2'),('Fisika','SMP','3'),
#             ('Kimia','SMA','1'),('Kimia','SMA','2'),('Kimia','SMA','3'),
#             ('Kimia','SMP','1'),('Kimia','SMP','2'),('Kimia','SMP','3'),
#             ('Ekonomi','SMA','1'),('Ekonomi','SMA','2'),('Ekonomi','SMA','3'),
#             ('Ekonomi','SMP','1'),('Ekonomi','SMP','2'),('Ekonomi','SMP','3'),
#             ('Sosiologi','SMA','1'),('Sosiologi','SMA','2'),('Sosiologi','SMA','3'),
#             ('Sosiologi','SMP','1'),('Sosiologi','SMP','2'),('Sosiologi','SMP','3'),
#             ('Geografi','SMA','1'),('Geografi','SMA','2'),('Geografi','SMA','3'),
#             ('Geografi','SMP','1'),('Geografi','SMP','2'),('Geografi','SMP','3'),
#             ('Bahasa Inggris','SMA','1'),('Bahasa Inggris','SMA','2'),('Bahasa Inggris','SMA','3'),
#             ('Bahasa Inggris','SMP','1'),('Bahasa Inggris','SMP','2'),('Bahasa Inggris','SMP','3'),
#             ('Bahasa Indonesia','SMA','1'),('Bahasa Indonesia','SMA','2'),('Bahasa Indonesia','SMA','3'),
#             ('Bahasa Indonesia','SMP','1'),('Bahasa Indonesia','SMP','2'),('Bahasa Indonesia','SMP','3'),
#             ('Sejarah','SMA','1'),('Sejarah','SMA','2'),('Sejarah','SMA','3'),
#             ('Sejarah','SMP','1'),('Sejarah','SMP','2'),('Sejarah','SMP','3')
#         ]
# c.executemany("INSERT INTO DetailCourse VALUES (?,?,?)", course)

#manampilkan isi deatilcourse
# c.execute("SELECT rowid, * FROM DetailCourse")
# c.execute("SELECT rowid, * FROM DetailCourse WHERE namaMapel = (?) AND jenjang = (?)",('Sejarah','SMA',))
# items = c.fetchall()
# for x in items:
#     print(x)

# c.execute("DELETE FROM JadwalTutor WHERE jamMulai = 0")

# #manampilkan isi jadwal
# c.execute("SELECT * FROM JadwalTutor")
c.execute("SELECT rowid, * FROM JadwalTutor WHERE tutorID = (?) AND hari = (?)",(12,'Senin',))
items = c.fetchall()
for x in items:
    print(x)

conn.commit()

conn.close()