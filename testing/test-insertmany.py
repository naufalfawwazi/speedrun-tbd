from importlib import util as iutil

lib1 = iutil.spec_from_file_location(
    "connectDB", "C:/xampp/htdocs/collaborations/speedrun-tbd/functions/connectDB.py")

connectDB = iutil.module_from_spec(lib1)
lib1.loader.exec_module(connectDB)

# test connection successful
connectDB.connection("localhost", "root", "root", "db_tokomainan")

# test insertmany
