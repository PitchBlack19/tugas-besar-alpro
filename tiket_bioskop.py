def anggota():
    print("\t PROJEK AKHIR ALGORITMA DAN PEMROGRAMAN")
    print("\t       institut teknologi telkom surabaya")
    print("----------------------------------------------------")
    print("1. Cellion Ascent Savredy\t\t1102210006")
    print("2. Firman Ahmad Maulana\t\t1102210008")
    print("----------------------------------------------------")
    print("tekan [enter] untuk melanjutkan Aplikasi ")
    input ()
    namafilm ()

def namafilm():
    import os
    os.system("CLS")
    print ("\n")
    print ("=================================================")
    print ("\tSELAMAT DATANG PARA PENONTON")
    print ("\t\t BIOSKOP XXj")
    print ("-------------------------------------------------")
def menu():
    print("Tekan (enter) untuk melanjutkan aplikasi ")
    input()
    namafilm ()
 
def namafilm ():
    import os
    os.system("CLS")
    print("\n")
    print("====================================================")
    print("SELAMAT DATANG DI APLIKASI PEMESANAN TIKET BIOSKOP")
    print("\t\t BIOSKOP XXj")
    print("----------------------------------------------------")
    print("|| Kode\t\t      Judul\t\tHarga ||")
    print("----------------------------------------------------")
    print("|| JVE \tJakarta Vs Evreybody       \t60000 ||")
    print("|| KKN \tKKN di Desa Penari         \t45000 ||")
    print("|| DRN \tDear Nathan Thank You Salma\t45000 ||")
    print("|| R3W \tRanah 3 Warna              \t50000 ||")
    print("|| MSG \tMy Sassy Girl              \t50000 ||")
    print("|| TTT \tTeka-Teki Tika             \t55000 ||")
    print("|| KKR \tKukira Kau Rumah           \t65000 ||")
    print("----------------------------------------------------")
    print("||\t\t   KODE KURSI   \t      ||")
    print("----------------------------------------------------")
    print("||     A1      A2      A3      A4      A5     ||")
    print("||     B1      B2      B3      B4      B5     ||")
    print("||     C1      C2      C3      C4      C5     ||")
    print("||     D1      D2      D3      D4      D5     ||")
    print("||     E1      E2      E3      E4      E5     ||")
    print("||     F1      F2      F3      F4      F5     ||")
    print("----------------------------------------------------")
    print("||\t\t   WAKTU   \t\t      ||")
    print("||\t\t   10.00-12.00  \t      ||")
    print("||\t\t   13.00-15.00  \t      ||")
    print("||\t\t   16.00-18.00  \t      ||")
    print("||\t\t   19.00-21.00  \t      ||")
    print("===================================================\n\n")
    print("\t-----Silahkan Buat Pesanan-----\n")
def tiket():
    with open("tiket.txt","w+")as file:
        file = open ("tiket.txt", "w")
        n =int(input("Masukkan banyak tiket yang dipesan :"))
        for i in range(1,n+1):
            print("\n Tiket ke-",i)
            kode = str(input("Masukkan kode film \t\t:"))
            kursi = str(input("Masukkan kode kursi \t\t:"))
            waktu = str(input("Masukkan waktu menonton \t\t:"))
            Judul = kode
            harga = kode

            if kode == "JVE" or kode == "jve":
                Judul = "Jakarta vs Everybody"
                harga = 60000
            elif kode == "KKN" or kode == "kkn":
                Judul = "KKN di Desa Penari "
                harga = 45000
            elif kode == "DRN" or kode == "drn":
                Judul = "Dear Nathan Thank You Salma"
                harga = 45000
            elif kode == "R3W" or kode == "r3w":
                Judul = "Ranah 3 Warna"
                harga = 50000
            elif kode == "MSG" or kode == "msg":
                Judul = "My Sally Girl"
                harga = 50000 
            elif kode == "TTT" or kode == "ttt":
                Judul = "Teka-Teki Tika"
                harga = 55000
            elif kode == "KKR" or kode == "kkr":
                Judul = "Kukira Kau Rumah"
                harga = 65000 
            else:
                print("\nMohon maaf film tidak tersedia")
                break

            while True :
                Jawab = input("apakah anda ingin mengubah pemesanan? (Y/N)\t\t:")
                if Jawab == "Y":
                    ubah = str(input("masukkan kode film \t\t:"))
                    kursi = str(input("Masukkan kode kursi \t\t:"))
                    waktu = str(input("Masukkan waktu menonton \t\t:"))
                    Judul = kode
                    harga = kode
                    if ubah == "JVE" or ubah == "jve":
                        Judul = "Jakarta vs Everybody"
                        harga = 60000
                    elif ubah == "KKN" or ubah == "kkn":
                        Judul = "KKN di Desa Penari "
                        harga = 45000
                    elif ubah == "DRN" or ubah == "drn":
                        Judul = "Dear Nathan Thank You Salma"
                        harga = 45000
                    elif ubah == "R3W" or ubah == "r3w":
                        Judul = "Ranah 3 Warna"
                        harga = 50000
                    elif ubah == "MSG" or ubah == "msg":
                        Judul = "My Sally Girl"
                        harga = 50000
                    elif ubah == "TTT" or ubah == "ttt":
                        Judul = "Teka-Teki Tika"
                        harga = 55000
                    elif ubah == "KKR" or ubah == "kkr":
                        Judul = "Kukira Kau Rumah"
                        harga = 65000
                    else:
                        print('\nfilm tidak tersedia\n')
                        continue
                if Jawab == "N":
                    break  

            bayar = input("Masukkan jumlah uang pembayaran \t:")
            total = int(bayar)-int(harga)
            
            if total < 0:
                print("\n PEMBAYARAN YANG ANDA LAKUKAN BELUM CUKUP, HARAP PERIKSA KEMBALI")
                print("------------------------------------------------------------------")
                bayar = int(input("Masukkan jumlah pembayaran\t"))
                total = int(bayar)- int(harga)
            teks = '''==================================================== 
\t TIKET BIOSKOP
----------------------------------------------------    
Tiket ke \t: {}
Judul Film \t: {}
Kode kursi \t: {}
Jam \t\t: {}
Harga \t\t: {}
----------------------------------------------------
Cost \t\t: {}
Kembalian \t: {}
====================================================
'''.format(i,Judul,kursi,waktu,harga,bayar,total)
            file= open ("tiket.txt", "a+")
            file.write(teks)
            file.close()
    
    print("\ntekan (enter) untuk mencetak tiket")
    input ()
    if kode == "JVE" or kode == "jve":
        cetak()
    elif kode == "KKN" or kode == "kkn":
        cetak()
    elif kode == "DRN" or kode == "drn":
        cetak()
    elif kode == "R3W" or kode == "r3w":
        cetak ()
    elif kode == "MSG" or kode == "msg":
        cetak()
    elif kode == "TTT" or kode == "ttt":
        cetak ()
    elif kode == "KKR" or kode == "kkr":
        cetak() 
    else:
        salah()



def cetak() :
    import os 
    os.system("CLS")
    print("\n")
    print("====================================================")
    print("\t\t     BIOSKOP XXj")
    print("\t\t     CETAK TIKET")
    print("     Tiket telah dicetak, silahkan diambil pada file txt")
    print("\t       Terima kasih telah memesan tiket")
    print("\t           Selamat menonton")
    print("====================================================")

def salah() :
    import os 
    os.system("CLS")
    print("\n")
    print("====================================================")
    print("\t\t     BIOSKOP XXj")
    print("\t\t     TIKET TIDAK DAPAT DICETAK")
    print("     Diharapkan untuk memasukan pemesanan dengan benar")
    print("\t    Agar tiket dapat dicetak")
    print("\t   Mohon maaf atas ketidaknyamanannya")
    print("====================================================")

anggota()
menu()
namafilm()
tiket()
           