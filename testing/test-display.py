from importlib import util as iutil

lib1 = iutil.spec_from_file_location(
    "connectDB", "speedrun-tbd\\functions\\connectDB.py")
lib2 = iutil.spec_from_file_location(
    "insertMany", "speedrun-tbd\\functions\\display.py")

connectDB = iutil.module_from_spec(lib1)
displayData = iutil.module_from_spec(lib2)

lib1.loader.exec_module(connectDB)
lib2.loader.exec_module(displayData)

# test connection successful
connect = connectDB.connection("localhost", "root", "root", "db_tokomainan")

sqlPembeli = '''
    SELECT *
    FROM tbl_pembeli;
    '''

sqlProduk = '''
    SELECT *
    FROM tbl_produk;
    '''

results = displayData.read_query(connect, sqlProduk)

for result in results:
    print(result)
