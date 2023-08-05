import sys
import os
from turtle import home
import mysql.connector as conn

def menuSapaan():
    print("""
Hallo Pengguna          
          """)
    input("Enter To Continue! ")
    main()

def penyimpananData():
    mydb = conn.connect(
        host="localhost",
        user="root",
        password="",
        database="testing_python_mysql"
    )

    mycursor = mydb.cursor()
    mycursor.execute("select * from daftar_pengguna")
    # mycursor.execute("insert into daftar_pengguna values ('Budu Setiawan', 18, 'Sleman', 'Backend Programmer')")
    # mycursor.execute("update daftar_pengguna set Pekerjaan='DevOps Engineer' where Nama like '%bud%'")
    # mycursor.execute("delete from daftar_pengguna where Nama like '%bud%'")

    # print("Mysql User List:\n")
    for x in mycursor:
        print(x)
    
    # mydb.commit()
    # print(mycursor.rowcount, "record deleted successfully!")
    
    input("\nEnter To Continue! ")
    main()


def salahInputHandle():
    print("\nMohon Maaf Pilihan Anda Tidak Tersedia\n")
    input("Tekan Enter Untuk Kembali! ")
    main()

def main():
    os.system("clear")
    print(
"""===== Selamat Datang di Kumpulan Tool Management =====

Silahkan Masukkan Angka Dari Option Berikut Untuk Melanjutkan:
1. Tool Sapaan
2. Tool Penyimpanan Data
3. Exit From Tool
"""        
        )
    
    option = input("Pilihan: ")
    match option:
        case '1':
            menuSapaan()
        case '2':
            penyimpananData()
        case '3':
            print("Selamat Tinggal Orang Baikk:)")
            return
        case _:
            salahInputHandle()
if __name__ == '__main__':
    main()