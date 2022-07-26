import os
def anggota():
    print("-"*52)
    print("      PROJEK AKHIR ALGORITMA DAN PEMROGRAMAN")
    print("\tInstitut Teknologi Telkom Surabaya")
    print("-")
    print("1. Cellion Ascent Savredy\t\t  1102210006")
    print("2. Firman Ahmad Maulana\t\t\t  1102210008")
    print("-"*52)
    print("tekan [enter] untuk melanjutkan Aplikasi ")
    input ()
    namafilm ()

def namafilm():
    os.system("CLS")
    print ("\n")
    print ("="*52)
    print ("\tSELAMAT DATANG PARA PENONTON")
    print ("\t\t BIOSKOP XXj")
    print ("-"*52)
def menu():
    print("Tekan (enter) untuk melanjutkan aplikasi ")
    input()
    namafilm ()
 
def namafilm ():
    os.system("CLS")
    print("\n")
    print("="*52)
    print(" SELAMAT DATANG DI APLIKASI PEMESANAN TIKET BIOSKOP ")
    print("                   BIOSKOP XXj                      ")
    print("="*52)
    print("|| Kode              Judul                  Harga ||")
    print("="*52)
    print("|| JVE      Jakarta Vs Evreybody            60000 ||")
    print("|| KKN      KKN di Desa Penari              45000 ||")
    print("|| DRN      Dear Nathan Thank You Salma     45000 ||")
    print("|| R3W      Ranah 3 Warna                   50000 ||")
    print("|| MSG      My Sassy Girl                   50000 ||")
    print("|| TTT      Teka-Teki Tika                  55000 ||")
    print("|| KKR      Kukira Kau Rumah                65000 ||")
    print("="*52)
    print("||                   KODE KURSI                   ||")
    print("="*52)
    print("||       A1      A2      A3      A4      A5       ||")
    print("||       B1      B2      B3      B4      B5       ||")
    print("||       C1      C2      C3      C4      C5       ||")
    print("||       D1      D2      D3      D4      D5       ||")
    print("||       E1      E2      E3      E4      E5       ||")
    print("||       F1      F2      F3      F4      F5       ||")
    print("="*52)
    print("||\t\t      WAKTU   \t\t          ||")
    print("||\t\t   10.00-12.00   \t\t  ||")
    print("||\t\t   13.00-15.00   \t\t  ||")
    print("||\t\t   16.00-18.00   \t\t  ||")
    print("||\t\t   19.00-21.00   \t\t  ||")
    print("="*52)
    print("         -----Silahkan Buat Pesanan-----")
def tiket():
    n =int(input("Masukkan banyak tiket yang dipesan :"))
    for i in range(1,n+1):
            print("\n Tiket ke-",i)
            kode = str(input("Masukkan kode film \t\t:")).upper()
            kursi = str(input("Masukkan kode kursi \t\t:"))
            waktu = str(input("Masukkan waktu menonton \t:"))
            Judul = kode
            harga = kode

            if kode == "JVE":
                Judul = "Jakarta vs Everybody"
                harga = 60000
            elif kode == "KKN":
                Judul = "KKN di Desa Penari "
                harga = 45000
            elif kode == "DRN":
                Judul = "Dear Nathan Thank You Salma"
                harga = 45000
            elif kode == "R3W":
                Judul = "Ranah 3 Warna"
                harga = 50000
            elif kode == "MSG":
                Judul = "My Sally Girl"
                harga = 50000 
            elif kode == "TTT":
                Judul = "Teka-Teki Tika"
                harga = 55000
            elif kode == "KKR":
                Judul = "Kukira Kau Rumah"
                harga = 65000 
            else:
                print("\nMohon maaf film tidak tersedia")
                break


            while True :
                Jawab = input("apakah anda ingin mengubah atau membatalkan pemesanan? (UBAH/BATALKAN/TIDAK)\t\t:").upper()
                if Jawab == "UBAH":
                    ubah = str(input("masukkan kode film \t\t:")).upper()
                    kursi = str(input("Masukkan kode kursi \t\t:"))
                    waktu = str(input("Masukkan waktu menonton \t\t:"))
                    Judul = kode
                    harga = kode

                    if ubah == "JVE":
                        Judul = "Jakarta vs Everybody"
                        harga = 60000
                    elif ubah == "KKN":
                        Judul = "KKN di Desa Penari "
                        harga = 45000
                    elif ubah == "DRN":
                        Judul = "Dear Nathan Thank You Salma"
                        harga = 45000
                    elif ubah == "R3W":
                        Judul = "Ranah 3 Warna"
                        harga = 50000
                    elif ubah == "MSG":
                        Judul = "My Sally Girl"
                        harga = 50000
                    elif ubah == "TTT":
                        Judul = "Teka-Teki Tika"
                        harga = 55000
                    elif ubah == "KKR":
                        Judul = "Kukira Kau Rumah"
                        harga = 65000
                    else:
                        print('\nfilm tidak tersedia\n')
                        continue
                if Jawab == "BATALKAN":
                    print("Pesanan dibatalkan, program akan ditutup")
                    quit()
                if Jawab == "TIDAK":
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
             z = open("tiket.txt", "a")
            z.write('\n')
            z.writelines(teks)
            z.close()
            f = open('tampung.txt', 'a')
            f.write('\n')
            f.writelines(Judul)
            f.write(', ')
            f.writelines(kursi)
            f.write(', ')
            f.writelines(waktu)
            f.write(', ')
            f.writelines(str(harga))
            f.close
            print('''
Apakah anda ingin mengurutkan data tiket?
[1] Jika ingin mengurutkan data
[2] Jika tidak ingin mengurutkan
            ''')
            print('Silahkan Masukan Pilihan : ', end='')
            urutin=str(input())
            if urutin == '1':            
                def urutkan():
                    def sorting(filename):
                        infile = open(filename)
                        words = []
                        for line in infile:
                            temp = line.split('\n')
                            for i in temp:
                                words.append(i)
                        infile.close()
                        words.sort()
                        print('data telah di urutkan')
                        print(words)
                    sorting("tampung.txt")
                urutkan()
    
    print("\ntekan (enter) untuk mencetak tiket")
    input ()
    if kode == "JVE":
        cetak()
    elif kode == "KKN":
        cetak()
    elif kode == "DRN":
        cetak()
    elif kode == "R3W":
        cetak ()
    elif kode == "MSG":
        cetak()
    elif kode == "TTT":
        cetak ()
    elif kode == "KKR":
        cetak() 
    else:
        salah()



def cetak() :
    os.system("CLS")
    print("\n")
    print("="*52)
    print("\t\t     BIOSKOP XXj")
    print("\t\t     CETAK TIKET")
    print("Tiket telah dicetak, silahkan diambil pada file txt")
    print("\t       Terima kasih telah memesan tiket")
    print("\t           Selamat menonton")
    print("="*52)

def salah() :
    os.system("CLS")
    print("\n")
    print("="*52)
    print("\t\t     BIOSKOP XXj")
    print("\t\t     TIKET TIDAK DAPAT DICETAK")
    print("     Diharapkan untuk memasukan pemesanan dengan benar")
    print("\t    Agar tiket dapat dicetak")
    print("\t   Mohon maaf atas ketidaknyamanannya")
    print("="*52)

anggota()
menu()
namafilm()
tiket()
           
