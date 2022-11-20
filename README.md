# speedrun-tbd

# Toko Mainan Uhuy

## GUIDE:

`pip install mysql-connector-python`
` pip install termcolor`

## Folder Structure:

    .
    │   ├── app
    │   |   ├── main.py
    │   ├── functions
    │   |   ├── connectDB.py
    │   |   ├── delete.py
    │   |   ├── display.py
    │   |   ├── insertMany.py
    │   |   ├── update.py
    │   ├── .gitignore
    │   ├── db_tokomainan.sql

## Database Design's Structure

    db_tokomainan
    .
    │   ├── tbl_produk
    │   |   ├── idProduk    [INT PRIMARY KEY AUTO INCREMENT NOT NULL]
    │   |   ├── namaProduk  [VARCHAR(100) NOT NULL]
    │   |   ├── harga       [INT UNSIGNED NOT NULL]
    │   ├── tbl_pemesanan
    │   |   ├── idPemesanan [INT PRIMARY KEY AUTO INCREMENT NOT NULL]
    │   |   ├── idProduk    [INT NOT NULL]
    │   |   ├── idPembeli   [INT NOT NULL]
    │   |   ├── namaProduk  [VARCHAR(100) NOT NULL]
    │   |   ├── namaPembeli [VARCHAR(255) NOT NULL]
    │   |   ├── total       [INT UNSIGNED NOT NULL]
    │   |   ├── tanggal     [VARCHAR(10) NOT NULL]
    │   ├── tbl_pembeli
    │   |   ├── idPembeli   [INT PRIMARY KEY AUTO INCREMENT NOT NULL]
    │   |   ├── namaPembeli [VARCHAR(255) NOT NULL]
    │   |   ├── alamat      [TEXT NOT NULL]
    │   |   ├── hp          [VARCHAR(16) NOT NULL]

### Credit: github.com/naufalfawwazi/speedrun-tbd