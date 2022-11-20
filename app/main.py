# -*- coding: utf-8 -*-
"""tbd.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lNqu3ViBwWsvP8Nx07YdJAUFd44pnv5O
"""

from importlib import util as iutil
from termcolor import cprint
from datetime import date
import os


path = os.path.realpath(__file__)
dir = os.path.dirname(path)
dir = dir.replace('app', 'functions')
os.chdir(dir)

dir1 = dir + '\\connectDB.py';
lib1 = iutil.spec_from_file_location(
    "connectDB", dir1)

def tampil(sql):
    dir2 = dir + '\\display.py'

    lib2 = iutil.spec_from_file_location(
        "display", dir2)
    connectDB = iutil.module_from_spec(lib1)
    displayData = iutil.module_from_spec(lib2)

    lib1.loader.exec_module(connectDB)
    lib2.loader.exec_module(displayData)

    # test connection successful
    connect = connectDB.connection(
        "localhost", "root", "root", "db_tokomainan")

    results = displayData.read_query(connect, sql)
    return results


def tambah(sql, val):
    dir2 = dir + '\\insertMany.py'

    lib2 = iutil.spec_from_file_location(
        "insertMany", dir2)

    connectDB = iutil.module_from_spec(lib1)
    insertMany = iutil.module_from_spec(lib2)

    lib1.loader.exec_module(connectDB)
    lib2.loader.exec_module(insertMany)

    # test connection successful
    connect = connectDB.connection(
        "localhost", "root", "root", "db_tokomainan")

    insertMany.insertMany(connect, sql, val)


def update(sql, val):
    dir2 = dir + '\\update.py'

    lib2 = iutil.spec_from_file_location(
        "update", dir2)

    connectDB = iutil.module_from_spec(lib1)
    updateData = iutil.module_from_spec(lib2)

    lib1.loader.exec_module(connectDB)
    lib2.loader.exec_module(updateData)

    # test connection successful
    connect = connectDB.connection(
        "localhost", "root", "root", "db_tokomainan")

    updateData.update(connect, sql, val)


def delete(sql, val):
    dir2 = dir + '\\delete.py'

    lib2 = iutil.spec_from_file_location(
        "delete", dir2)

    connectDB = iutil.module_from_spec(lib1)
    deleteData = iutil.module_from_spec(lib2)

    lib1.loader.exec_module(connectDB)
    lib2.loader.exec_module(deleteData)

    # test connection successful
    connect = connectDB.connection(
        "localhost", "root", "root", "db_tokomainan")

    deleteData.delete(connect, sql, val)


def tampilMainan():
    sqlProduk = '''
      SELECT *
      FROM tbl_produk;
      '''
    result = tampil(sqlProduk)
    for res in result:
        print(res)

    return result


def tampilPembeli():
    sqlPembeli = '''
      SELECT *
      FROM tbl_pembeli;
      '''
    result = tampil(sqlPembeli)
    for res in result:
        print(res)

    return result


def tampilPemesanan():
    sqlPemesanan = '''
      SELECT *
      FROM tbl_pemesanan;
      '''
    result = tampil(sqlPemesanan)
    for res in result:
        print(res)

    return result


def tambahMainan():
    namaProduk = input('Nama Mainan: ')
    harga = int(input('Harga Mainan: '))

    sqlProduk = '''
      INSERT INTO tbl_produk ( namaProduk, harga) 
      VALUES ( %s, %s)
      '''

    valProduk = [
        (namaProduk, harga)
    ]

    tambah(sqlProduk, valProduk)


def tambahPelanggan():
    namaPembeli = input('Nama Pembeli: ')
    alamat = input('Alamat Pembeli: ')
    hp = input('No HP Pembeli: ')

    sqlPembeli = '''
      INSERT INTO tbl_pembeli ( namaPembeli, alamat, hp) 
      VALUES ( %s, %s, %s)
      '''

    valPembeli = [
        (namaPembeli, alamat, hp)
    ]

    tambah(sqlPembeli, valPembeli)


def ubahMainan():
    tampilMainan()
    namaProduk = input('Nama Mainan yang ingin diubah: ')
    harga = int(input('Harga baru Mainan: '))
    # update di tbl_produk

    sqlProduk = '''
      UPDATE tbl_produk SET namaProduk=%s, harga=%s
      WHERE namaProduk=%s
      '''

    valProduk = (namaProduk, harga, namaProduk)

    update(sqlProduk, valProduk)


def hapusMainan():
    tampilMainan()
    namaProduk = input('Nama Mainan yang ingin dihapus: ')
    # delete dari tbl_produk

    sqlProduk = '''
      DELETE FROM tbl_produk WHERE namaProduk=%s
      '''

    valProduk = [
        (namaProduk)
    ]

    delete(sqlProduk, valProduk)


def catatPemesanan():
    tampilPembeli()
    idPembeli = int(input('ID Pelanggan yang beli: '))

    tampilMainan()
    idProduk = int(input('ID Mainan yang dibeli: '))

    sqlProduk = f'''
      SELECT *
      FROM tbl_produk WHERE idProduk={idProduk};
      '''

    resultProduk = tampil(sqlProduk)[0]
    # print(resultProduk)
    idProduk, namaProduk, harga = resultProduk

    sqlPembeli = f'''
      SELECT *
      FROM tbl_pembeli WHERE idPembeli={idPembeli};
      '''
    idPembeli, namaPembeli, alamat, hp = tampil(sqlPembeli)[0]

    jumlah = int(input('Jumlah beli: '))
    total = jumlah * harga
    tanggal = date.today()

    # insert ke tbl_pemesanan

    sqlPemesanan = '''
      INSERT INTO tbl_pemesanan 
      ( idProduk, idPembeli, namaProduk, namaPembeli, jumlah, total, tanggal ) 
      VALUES ( %s, %s, %s, %s, %s, %s, %s)
      '''

    valPemesanan = [
        (idProduk, idPembeli, namaProduk, namaPembeli, jumlah, total, tanggal)
    ]

    tambah(sqlPemesanan, valPemesanan)


def main():
    pilih = 0

    while pilih != 9:
        cprint('-= TOKO MAINAN UHUY =-', 'red', 'on_cyan')
        print('1. Lihat Etalase Mainan')
        print('2. Tambah Mainan')
        print('3. Ubah Harga Mainan')
        print('4. Hapus Mainan')
        print('5. Lihat Pelanggan')
        print('6. Tambah Pelanggan')
        print('7. Lihat Data Pemesanan')
        print('8. Catat Pemesanan Mainan')
        print('9. Keluar')

        print()
        pilih = int(input('Pilih Operasi: '))

        if pilih == 1:
            tampilMainan()
        if pilih == 2:
            tambahMainan()
        if pilih == 3:
            ubahMainan()
        if pilih == 4:
            hapusMainan()
        if pilih == 5:
            tampilPembeli()
        if pilih == 6:
            tambahPelanggan()
        if pilih == 7:
            tampilPemesanan()
        if pilih == 8:
            catatPemesanan()
        print()


if __name__ == '__main__':
    main()
