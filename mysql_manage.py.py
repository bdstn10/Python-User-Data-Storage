import os
from mysql.connector import connect, Error


def lihatDataPengguna():
    os.system("clear")
    print("Daftar Data Pengguna di Sistem Kami:")
    try:
        with connect(
            host="localhost",
            user="root",
            password="",
            database="testing_python_mysql"
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute("select * from tb_data_pengguna")
                for i in cursor:
                    print(i)
    except Error as e:
        print(e)

def penyimpananData():
    os.system("clear")
    print("="*5, "Tool Penyimpanan Data",5*"=")
    print("Case: Data Identitas Pengguna")
    print(
"""
Masukkan Pilihan Berikut Untuk Melanjutkan:
1. Lihat Data Pengguna Terdaftar
2. Masukkan Data Pengguna
3. Kembali ke Menu Utama
"""
        )
    option = input("Pilihan: ")
    match option:
        case '1':
            lihatDataPengguna()
        case '2':
            pass
        case '3':
            main()
        case _:
            salahInputHandle(penyimpananData)

def salahInputHandle(back):
    print("\nMohon Maaf Pilihan Anda Tidak Tersedia\n")
    input("Tekan Enter Untuk Kembali! ")
    back()

def main():
    os.system("clear")
    print("===== Selamat Datang di Kumpulan Tool Management =====")
    print(
"""
Silahkan Masukkan Angka Dari Option Berikut Untuk Melanjutkan:
1. Tool Penyimpanan Data
2. Exit From Tool
"""        
        )
    
    option = input("Pilihan: ")
    match option:
        case '1':
            penyimpananData()
        case '2':
            print("Selamat Tinggal Orang Baikk:)")
            return
        case _:
            salahInputHandle(main)
if __name__ == '__main__':
    main()