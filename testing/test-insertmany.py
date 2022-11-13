from importlib import util as iutil

lib1 = iutil.spec_from_file_location(
    "connectDB", "D:/Programming/BisaAI/speedrun-tbd/functions/connectDB.py")
lib2 = iutil.spec_from_file_location(
    "insertMany", "D:/Programming/BisaAI/speedrun-tbd/functions/insertMany.py")

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

sqlProduk = '''
    INSERT INTO tbl_produk ( namaProduk, harga) 
    VALUES ( %s, %s)
    '''

valPembeli = [
    ('Naufal', 'Tlogosari Raya', '0812345678'),
    ('Jimmy', 'Pedurungan Timur', '0814327682')
]

valProduk = [
    ('Woody ToyStory', 60000),
    ('Dr.Strange2', 82000)
]


insertMany.insertMany(connect, sqlProduk, valProduk)
