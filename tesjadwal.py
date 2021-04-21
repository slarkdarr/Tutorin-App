from jadwalTutor2 import *

e = jadwalTutor()

#test getIntJam
assert(e.getIntJam("08.00 WIB")==8)
assert(e.getIntJam("10.00 WIB")==10)
assert(e.getIntJam("00.00 WIB")==0)

data = [(2, 'Biologi', 'SMA', 2),(3, 'Biologi', 'SMA', 3),(4, 'Biologi', 'SMP', 1),(5, 'Biologi', 'SMP', 2) ,
        (6, 'Biologi', 'SMP', 3),(7, 'Matematika', 'SMA', 1),(8, 'Matematika', 'SMA', 2),(9, 'Matematika', 'SMA', 3),(10, 'Matematika', 'SMP', 1),
        (11, 'Matematika', 'SMP', 2),(12, 'Matematika', 'SMP', 3),(13, 'Fisika', 'SMA', 1),(14, 'Fisika', 'SMA', 2),(15, 'Fisika', 'SMA', 3),
        (16, 'Fisika', 'SMP', 1),(17, 'Fisika', 'SMP', 2),(18, 'Fisika', 'SMP', 3)]

#test getID
assert(e.getID(data,'Biologi',2,'SMA')==2)
assert(e.getID(data,'Matematika',2,'SMA')==8)
assert(e.getID(data,'Fisika',2,'SMP')==17)

#test getID2
data2 = [(16, 'Fisika', 'SMP', 1)]
data3 = [(7, 'Matematika', 'SMA', 1)]
assert(e.getID2(data,data2)==16)
assert(e.getID2(data,data3)==7)

#test showSchedule

