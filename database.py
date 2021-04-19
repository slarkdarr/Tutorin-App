import sqlite3
import bcrypt

class Database:
    '''
    Database Class for sqlite3
    :params conn — sqlite3Connection
    :params curr — cursor
    '''
    def __init__(self):
        try:
            self.conn = sqlite3.connect('test.db')
            print('Succesfully connected to database')
            self.curr = self.conn.cursor()
        except:
            print('Failed')

    def createTable(self):
        '''Method for Creating Table in Database'''
        create_table_user = '''
        CREATE TABLE IF NOT EXISTS user(
        idUser Integer PRIMARY KEY AUTOINCREMENT,
        username TEXT PRIMARY KEY NOT NULL,
        password TEXT NOT NULL,
        nama TEXT NOT NULL,
        kontak TEXT NOT NULL,
        alamat TEXT NOT NULL,
        balance Integer NOT NULL DEFAULT 0,
        flag Integer NOT NULL DEFAULT 0,
        rating Float NOT NULL DEFAULT 0
        );
        '''

        create_table_tutor = '''
        CREATE TABLE IF NOT EXISTS tutor(
        username TEXT PRIMARY KEY NOT NULL,
        jenjang TEXT NOT NULL,
        tarif Integer NOT NULL,
        noKTP TEXT NOT NULL,
        pengalaman TEXT NOT NULL,
        pendidikan TEXT NOT NULL,
        headline TEXT NOT NULL DEFAULT '',
        FOREIGN KEY (username) REFERENCES user(username) ON DELETE CASCADE ON UPDATE CASCADE
        );
        '''

        create_table_bidang = '''
        CREATE TABLE IF NOT EXISTS bidang(
        username TEXT NOT NULL,
        bidang TEXT NOT NULL,
        primary key(username),
        foreign key (username) references user(username) on delete cascade on update cascade    
        );
        '''

        self.curr.execute(create_table_user)
        self.curr.execute(create_table_tutor)
        self.curr.execute(create_table_bidang)
        self.conn.commit()

    def insertData(self, data):
        '''
        Method for Insertig Data in Table in Database
        '''
        insert_data_user = '''
        INSERT INTO user(username, password, nama, kontak, alamat)
        VALUES(?, ?, ?, ?, ?);
        '''
        self.curr.execute(insert_data_user, data)
        self.conn.commit()
    
    def insertDataTutor(self, data):
        '''
        Method for Insertig Data in Table in Database
        '''
        insert_data_tutor = '''
        INSERT INTO tutor(username, jenjang, tarif, noKTP, pengalaman, pendidikan, headline)
        VALUES(?, ?, ?, ?, ?, ?);
        '''
        self.curr.execute(insert_data_tutor, data)
        self.conn.commit()

    def searchData(self, data):
        '''
        Method for Searching Data in Table in Database
        '''
        search_data = '''
        SELECT * FROM user WHERE username = (?);
        '''
        self.curr.execute(search_data, data)
        rows = self.curr.fetchall()
        print(data)
        print(rows)
        if rows == []:
            print("username available")
            return 1
        print('username is not available')
        return 0
        
    def validateData(self, data, inputData):
        '''
        Method for Validating Data Table in Database
        '''
        print(data)
        print(inputData)
        validate_data = '''
        SELECT * FROM user WHERE username = (?);
        '''
        self.curr.execute(validate_data, data)
        row = self.curr.fetchall()
        print(row)
        if row[0][1] == inputData[0]:
            return row[0][2] == inputData[1]