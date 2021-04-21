import pytest
from jadwalTutor import *
from searchTutor import *
    
#test getIntJam
def test_getIntJam():
        assert(getIntJam("08.00 WIB")==8)
        
def test_getIntJam2():
        assert(getIntJam("10.00 WIB")==10)

def test_getIntJam3():
        assert(getIntJam("00.00 WIB")==0)

def test_getID():
        data = [(2, 'Biologi', 'SMA', 2),(3, 'Biologi', 'SMA', 3),(4, 'Biologi', 'SMP', 1),(5, 'Biologi', 'SMP', 2) ,
        (6, 'Biologi', 'SMP', 3),(7, 'Matematika', 'SMA', 1),(8, 'Matematika', 'SMA', 2),(9, 'Matematika', 'SMA', 3),(10, 'Matematika', 'SMP', 1),
        (11, 'Matematika', 'SMP', 2),(12, 'Matematika', 'SMP', 3),(13, 'Fisika', 'SMA', 1),(14, 'Fisika', 'SMA', 2),(15, 'Fisika', 'SMA', 3),
        (16, 'Fisika', 'SMP', 1),(17, 'Fisika', 'SMP', 2),(18, 'Fisika', 'SMP', 3)]
        assert(getID(data,'Biologi',2,'SMA')==2)
        
        
def test_getID22():
        data = [(2, 'Biologi', 'SMA', 2),(3, 'Biologi', 'SMA', 3),(4, 'Biologi', 'SMP', 1),(5, 'Biologi', 'SMP', 2) ,
        (6, 'Biologi', 'SMP', 3),(7, 'Matematika', 'SMA', 1),(8, 'Matematika', 'SMA', 2),(9, 'Matematika', 'SMA', 3),(10, 'Matematika', 'SMP', 1),
        (11, 'Matematika', 'SMP', 2),(12, 'Matematika', 'SMP', 3),(13, 'Fisika', 'SMA', 1),(14, 'Fisika', 'SMA', 2),(15, 'Fisika', 'SMA', 3),
        (16, 'Fisika', 'SMP', 1),(17, 'Fisika', 'SMP', 2),(18, 'Fisika', 'SMP', 3)]
        assert(getID(data,'Matematika',2,'SMA')==8)

def test_getID33():
        data = [(2, 'Biologi', 'SMA', 2),(3, 'Biologi', 'SMA', 3),(4, 'Biologi', 'SMP', 1),(5, 'Biologi', 'SMP', 2) ,
        (6, 'Biologi', 'SMP', 3),(7, 'Matematika', 'SMA', 1),(8, 'Matematika', 'SMA', 2),(9, 'Matematika', 'SMA', 3),(10, 'Matematika', 'SMP', 1),
        (11, 'Matematika', 'SMP', 2),(12, 'Matematika', 'SMP', 3),(13, 'Fisika', 'SMA', 1),(14, 'Fisika', 'SMA', 2),(15, 'Fisika', 'SMA', 3),
        (16, 'Fisika', 'SMP', 1),(17, 'Fisika', 'SMP', 2),(18, 'Fisika', 'SMP', 3)]
        assert(getID(data,'Fisika',2,'SMP')==17)

#test getID2
def test_getId2():
        data = [(2, 'Biologi', 'SMA', 2),(3, 'Biologi', 'SMA', 3),(4, 'Biologi', 'SMP', 1),(5, 'Biologi', 'SMP', 2) ,
        (6, 'Biologi', 'SMP', 3),(7, 'Matematika', 'SMA', 1),(8, 'Matematika', 'SMA', 2),(9, 'Matematika', 'SMA', 3),(10, 'Matematika', 'SMP', 1),
        (11, 'Matematika', 'SMP', 2),(12, 'Matematika', 'SMP', 3),(13, 'Fisika', 'SMA', 1),(14, 'Fisika', 'SMA', 2),(15, 'Fisika', 'SMA', 3),
        (16, 'Fisika', 'SMP', 1),(17, 'Fisika', 'SMP', 2),(18, 'Fisika', 'SMP', 3)]
        data2 = (16, 'Fisika', 'SMP', 1)
        data3 = (7, 'Matematika', 'SMA', 1)
        assert(getID2(data,data2)==16)
        

def test_getId233():
        data = [(2, 'Biologi', 'SMA', 2),(3, 'Biologi', 'SMA', 3),(4, 'Biologi', 'SMP', 1),(5, 'Biologi', 'SMP', 2) ,
        (6, 'Biologi', 'SMP', 3),(7, 'Matematika', 'SMA', 1),(8, 'Matematika', 'SMA', 2),(9, 'Matematika', 'SMA', 3),(10, 'Matematika', 'SMP', 1),
        (11, 'Matematika', 'SMP', 2),(12, 'Matematika', 'SMP', 3),(13, 'Fisika', 'SMA', 1),(14, 'Fisika', 'SMA', 2),(15, 'Fisika', 'SMA', 3),
        (16, 'Fisika', 'SMP', 1),(17, 'Fisika', 'SMP', 2),(18, 'Fisika', 'SMP', 3)]
        assert(getID2(data,data3)==7)

#test saveForm
def test_saveForm():
        assert(checkDatabaseJadwal(12,4,'Senin',8,2,"Tidak Ada")==1)
        

def test_saveForm2():
        assert(checkDatabaseJadwal(11111,12,'Selasa',9,1,"Tidak ada")==0)
