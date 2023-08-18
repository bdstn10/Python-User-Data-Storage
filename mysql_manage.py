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
                    print(f"\nId: {i[0]}")
                    print(f"Nama: {i[1]}")
                    print(f"Umur: {i[2]}")
                    print(f"Alamat: {i[3]}")
                
                input("\nPress Enter To Continue... ")
                penyimpananData()
    except Error as e:
        print(e)

def simpanDataPengguna():
    os.system("clear") 
    print("Masukkan Data Pengguna Untuk Disimpan")
    nama = input("Nama: ")
    umur = input("Umur: ")
    alamat = input("Alamat: ")
    
    isInputHaveFilled = (nama.__len__() > 0) and (umur.__len__() > 0)  and (alamat.__len__() > 0)
    
    if isInputHaveFilled:
        isNamaAlphabet = nama.isalpha()
        isUmurNum = umur.isnumeric()
    
        if not isNamaAlphabet:
            print("Mohon isi nama hanya dengan huruf alphabet!")
            input("\nEnter To Continue... ")
            penyimpananData()
        if not isUmurNum:
            print("Mohon isi umur hanya dengan angka saja!")
            input("\nEnter To Continue... ")
            penyimpananData()
        
        try:
            with connect(
                host="localhost",
                user="root",
                password="",
                database="testing_python_mysql"
            ) as connection:
                with connection.cursor() as cursor:
                    query = f"INSERT INTO `tb_data_pengguna` VALUES (NULL, '{nama}', '{umur}', '{alamat}')"
                    cursor.execute(query)
                    
                    connection.commit()
                    
                    if(cursor.rowcount > 0):
                        print(f"\nBerhasil menyimpan data user '{nama}' ke database!")
                    else:
                        print("\nGagal menyimpan data user!")
                    
                    input("\nPress Enter To Continue... ")
                    penyimpananData()
        except Error as e:
            print(e)
        
    else:
        print("Mohon lengkapi semua form input yang diminta!")
        input("\nEnter To Continue... ")
        penyimpananData()

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
            simpanDataPengguna()
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
            exit()
        case _:
            salahInputHandle(main)
if __name__ == '__main__':
    main()