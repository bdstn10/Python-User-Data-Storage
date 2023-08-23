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

# Membuat method untuk mengecek apakah suatu variable berupa null atau whitespace
def isVarNotNullOrSpace(var):
    return (var.__len__() >= 1 and not var.isspace())

def verifikasiUbahDataPengguna():
    os.system("clear")
    print("Masukkan Id Pengguna Yang Ingin diUbah Datanya")
    idToUpdate = input("Id: ")
    
    # Pengecekan agar Id benar-benar diisi dan berupa angka
    if (idToUpdate.__len__() < 1) or not idToUpdate.isnumeric():
        print("Mohon Masukkan Id Pengguna Dengan Benar!")
        
        input("\nEnter Untuk Kembali... ")
        verifikasiUbahDataPengguna()
    
    try:
        with connect(
            host="localhost",
            user="root",
            password="",
            database="testing_python_mysql"
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(f"select * from tb_data_pengguna where id={idToUpdate}")
                dataUser =  cursor.fetchall()
                
                # Pengecekan untuk memastikan data yang hendak diubah terdapat di sistem
                if cursor.rowcount < 1:
                    print("Maaf, data yang anda minta tidak terdapat di sistem!")
                    input("\nEnter To Continue... ")
                    penyimpananData()
                
                # os.system("clear")
                print("Apakah data berikut yang ingin anda ubah: ")    
                
                for data in dataUser:
                    print(f"\nId: {data[0]}")
                    print(f"Nama: {data[1]}")
                    print(f"Umur: {data[2]}")
                    print(f"Alamat: {data[3]}")
                
                konfirmasiAksi = input("\ny/(Yes), n/(No), b/(Back)? ")
                
                match konfirmasiAksi:
                    case 'y':
                        os.system("clear")
                        dataToUpdate = list(dataUser[0])
                        print("Masukkan Data Baru Untuk diUpdate Ke Pengguna Yang Bersangkutan: ")
                        namaBaru = input("Nama: ")
                        umurBaru = input("Umur: ")
                        alamatBaru = input("Alamat: ")
    
                        if isVarNotNullOrSpace(namaBaru) and not namaBaru.isalpha():
                            print("Mohon isi nama hanya dengan huruf alphabet!")
                            input("\nEnter To Continue... ")
                            penyimpananData()
                        if isVarNotNullOrSpace(umurBaru) and not umurBaru.isnumeric():
                            print("Mohon isi umur hanya dengan angka saja!")
                            input("\nEnter To Continue... ")
                            penyimpananData()
                        
                        dataToUpdate[1] = namaBaru if isVarNotNullOrSpace(namaBaru) else dataToUpdate[1]
                        dataToUpdate[2] = umurBaru if isVarNotNullOrSpace(umurBaru) else dataToUpdate[2]
                        dataToUpdate[3] = alamatBaru if isVarNotNullOrSpace(alamatBaru) else dataToUpdate[3]
                        
                        cursor.execute(f"UPDATE tb_data_pengguna SET nama='{dataToUpdate[1]}', umur='{dataToUpdate[2]}', alamat='{dataToUpdate[3]}' WHERE id={idToUpdate}")
                        connection.commit()
                        
                        if cursor.rowcount > 0:
                            print("Berhasil Mengupdate Data User!")
                            input("\nEnter To Continue... ")
                            penyimpananData()
                    case 'n':
                        verifikasiUbahDataPengguna()
                    case 'b':
                        penyimpananData()
                    case _:
                        salahInputHandle(penyimpananData)
                
    except Error as e:
        print(e)

def hapusDataPengguna():
    os.system("clear")
    print("Masukkan Id Pengguna Yang Ingin diHapus Datanya")
    idToDelete = input("Id: ")
    
    if (idToDelete.__len__() < 1) or not idToDelete.isnumeric():
        print("Mohon Masukkan Id Pengguna Dengan Benar!")
        
        input("\nEnter Untuk Kembali... ")
        hapusDataPengguna()
    
    try:
        with connect(
            host="localhost",
            user="root",
            password="",
            database="testing_python_mysql"
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(f"select * from tb_data_pengguna where id={idToDelete}")
                dataUser =  cursor.fetchall()
                
                # Pengecekan untuk memastikan data yang hendak diubah terdapat di sistem
                if cursor.rowcount < 1:
                    print("Maaf, data yang anda minta tidak terdapat di sistem!")
                    input("\nEnter To Continue... ")
                    penyimpananData()
                
                # os.system("clear")
                print("Apakah data berikut yang ingin anda hapus: ")    
                
                for data in dataUser:
                    print(f"\nId: {data[0]}")
                    print(f"Nama: {data[1]}")
                    print(f"Umur: {data[2]}")
                    print(f"Alamat: {data[3]}")
                
                konfirmasiAksi = input("\ny/(Yes), n/(No), b/(Back)? ")
                
                match konfirmasiAksi:
                    case 'y':
                        os.system("clear")
                        
                        cursor.execute(f"DELETE FROM tb_data_pengguna where id='{idToDelete}'")
                        connection.commit()
                        
                        if cursor.rowcount > 0:
                            print("Berhasil Menghapus Data User!")
                            input("\nEnter To Continue... ")
                            penyimpananData()
                    case 'n':
                        hapusDataPengguna()
                    case 'b':
                        penyimpananData()
                    case _:
                        salahInputHandle(penyimpananData)
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
3. Ubah Data Pengguna
4. Hapus Data Pengguna
5. Kembali ke Menu Utama
"""
        )
    option = input("Pilihan: ")
    match option: 
        case '1':
            lihatDataPengguna()
        case '2':
            simpanDataPengguna()
        case '3':
            verifikasiUbahDataPengguna()
        case '4':
            hapusDataPengguna()
        case '5':
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