from importlib import util as iutil

lib1 = iutil.spec_from_file_location(
    "connectDB", "C:/xampp/htdocs/collaborations/speedrun-tbd/functions/connectDB.py")
lib2 = iutil.spec_from_file_location(
    "insertMany", "C:/xampp/htdocs/collaborations/speedrun-tbd/functions/insertMany.py")

connectDB = iutil.module_from_spec(lib1)
insertMany = iutil.module_from_spec(lib2)

lib1.loader.exec_module(connectDB)
lib2.loader.exec_module(insertMany)

# test connection successful
connect = connectDB.connection("localhost", "root", "root", "db_tokomainan")

# test insertmany pembeli
sqlPembeli = '''
    INSERT INTO tbl_pembeli ( namaPembeli, alamat, hp) 
    VALUES ( %s, %s, %s)
    '''

valPembeli = [
    ('Naufal', 'Tlogosari Raya', '0812345678'),
    ('Jimmy', 'Pedurungan Timur', '0814327682')
]

insertMany.insertMany(connect, sqlPembeli, valPembeli)
