# PROGRAM MESIN MAKANAN DAN MINUMAN
def menampilkanjenis():
    print("==================================================")
    print("Program Mesin Penjual Makanan dan Minuman Otomatis")
    print("==================================================")
    print("1. Makanan Ringan")
    print("2. Minuman Dingin")
    print("0. Keluar")
  
    pilih = str(input("Masukkan Pilihan : "))
  
    if(pilih == "1"):
      makananringan()
    elif(pilih == "2"):
     minumandingin()
    elif(pilih =="0"):
      Membeli_lagi()

#MAKANAN RINGAN
def makananringan():
    mr = ["1. Chitato", "2. Maitos", "3. Qtela", "4. Taro", "5. Jetz", "6.Pilus", "7. SilverQueen", "8. Cadbury"]
    print("Pilih Makanan")
    print(mr[0])
    print(mr[1])
    print(mr[2])
    print(mr[3])
    print(mr[4])
    print(mr[5])
    print(mr[6])
    print(mr[7])
    print("0. Keluar")
    print("===========================")
    
    pilih = str(input("Masukkan Pilihan     : "))
      

    if (pilih == "1"):
        Chitato()
    elif (pilih == "2"):
        Maitos()
    elif (pilih == "3"):
        Qtela()
    elif (pilih == "4"):
        Taro()
    elif (pilih == "5"):
        Jetz()
    elif (pilih == "6"):
        Pilus()
    elif (pilih == "7"):
        SilverQueen()
    elif (pilih == "8"):
        Cadbury()
    elif (pilih == "0"): 
        Membeli_lagi()
    else:
        print("Makanan Tidak Tersedia")
        Kembali_ke_awal() 
    
#MINUMAN DINGIN
def minumandingin():
    md = ["1. Aqua Botol","2. Teh Pucuk","3. Pocari Sweat", "4. Freshtea", "5. Good Day", "6. Nestcafe"]
    print("Pilih Minuman")
    print(md[0])
    print(md[1])
    print(md[2])
    print(md[3])
    print(md[4])
    print(md[5])
    print("0. Keluar")
    print("============================")

    pilih = str(input("Masukkan Pilihan     : "))
    if (pilih == "1"):
        Aqua_Botol()
    elif (pilih == "2"):
        Teh_Pucuk()
    elif (pilih == "3"):
        Pocari_Sweat()
    elif (pilih == "4"):
        Freshtea()
    elif (pilih == "5"):
        Good_Day()
    elif (pilih == "6"):
        Nestcafe()
    elif (pilih == "0"):
        Membeli_lagi()
    else :
        print("Minuman Tidak Tersedia")
        Kembali_ke_awal()
        
# INGIN MEMBELI LAGI
def Membeli_lagi():
    pilih = str(input("Ingin Membeli lagi (1) Ya (2) Tidak : "))
    if (pilih == "1"):
        Kembali_ke_awal()
    elif (pilih == "2"):
        print("Terimakasih Telah Membeli")
        print("===========================")
        input("Tekan Enter untuk keluar")
        exit
        
# KEMBALI KE AWAL
def Kembali_ke_awal():
    input("Tekan Enter untuk kembali...")
    print("")
    menampilkanjenis()

#MAKANAN RINGAN
def Chitato():
    HargaC = 15000
    x = int(input("Masukkan Uang Anda   : "))
    if (x >= HargaC):
        print("Kembalian Anda       = Rp.",x - HargaC)
        print("Pembelian Berhasil")
        print("===========================")
        Membeli_lagi()
    else :
        print("Uang Anda Tidak Cukup")
        Kembali_ke_awal()

def Maitos():
    HargaM = 10000
    x = int(input("Masukkan Uang Anda   : "))
    if (x >= HargaM):
        print("Kembalian Anda       = Rp.",x - HargaM)
        print("Pembelian Berhasil")
        print("===========================")
        Membeli_lagi()
    else :
        print("Uang Anda Tidak Mencukupi")
        Kembali_ke_awal()

def Qtela():
    HargaQ = 8000
    x = int(input("Masukkan Uang Anda   : "))
    if (x >= HargaQ):
        print("Kembalian Anda       = Rp.",x - HargaQ)
        print("Pembelian Berhasil")
        print("===========================")
        Membeli_lagi()
    else :
        print("Uang Anda Tidak Mencukupi")
        Kembali_ke_awal()

def Taro():
    HargaT = 7500
    x = int(input("Masukkan Uang Anda   : "))
    if (x >= HargaT):
        print("Kembalian Anda       = Rp.",x - HargaT)
        print("Pembelian Berhasil")
        print("===========================")
        Membeli_lagi()
    else :
        print("Uang Anda Tidak Mencukupi")
        Kembali_ke_awal()
        
def Jetz():
    HargaJ = 9000
    x = int(input("Masukkan Uang Anda   : "))
    if (x >= HargaJ):
        print("Kembalian Anda       = Rp.",x - HargaJ)
        print("Pembelian Berhasil")
        print("===========================")
        Membeli_lagi()
    else :
        print("Uang Anda Tidak Mencukupi")
        Kembali_ke_awal()

def Pilus():
    HargaP = 4000
    x = int(input("Masukkan Uang Anda   : "))
    if (x >= HargaP):
        print("Kembalian Anda       = Rp.",x - HargaP)
        print("Pembelian Berhasil")
        print("===========================")
        Membeli_lagi()
    else :
        print("Uang Anda Tidak Mencukupi")
        Kembali_ke_awal()

def SilverQueen():
    HargaS = 8000
    x = int(input("Masukkan Uang Anda   : "))
    if (x >= HargaS):
        print("Kembalian Anda       = Rp.",x - HargaS)
        print("Pembelian Berhasil")
        print("===========================")
        Membeli_lagi()
    else :
        print("Uang Anda Tidak Mencukupi")
        Kembali_ke_awal()

def Cadbury():
    HargaC = 6500
    x = int(input("Masukkan Uang Anda   : "))
    if (x >= HargaC):
        print("Kembalian Anda       = Rp.",x - HargaC)
        print("Pembelian Berhasil")
        print("===========================")
        Membeli_lagi()
    else :
        print("Uang Anda Tidak Mencukupi")
        Kembali_ke_awal()
        
#MINUMAN DINGIN
def Aqua_Botol():
    HargaAB = 4000
    x = int(input("Masukkan Uang Anda   : "))
    if (x >= HargaAB):
        print("Kembalian Anda       = Rp.",x - HargaAB)
        print("Pembelian Berhasil")
        print("===========================")
        Membeli_lagi()
    else :
        print("Uang Anda Tidak Mencukupi")
        Kembali_ke_awal()

def Teh_Pucuk():
    HargaTP = 12500
    x = int(input("Masukkan Uang Anda   : "))
    if (x >= HargaTP):
        print("Kembalian Anda       = Rp.",x - HargaTP)
        print("Pembelian Berhasil")
        print("===========================")
        Membeli_lagi()
    else :
        print("Uang Anda Tidak Mencukupi")
        Kembali_ke_awal()

def Pocari_Sweat():
    HargaPS = 12500
    x = int(input("Masukkan Uang Anda   : "))
    if (x >= HargaPS):
        print("Kembalian Anda       = Rp.",x - HargaPS)
        print("Pembelian Berhasil")
        print("===========================")
        Membeli_lagi()
    else :
        print("Uang Anda Tidak Mencukupi")
        Kembali_ke_awal()
        
def Freshtea():
    HargaF = 5000
    x = int(input("Masukkan Uang Anda   : "))
    if (x >= HargaF):
        print("Kembalian Anda       = Rp.",x - HargaF)
        print("Pembelian Berhasil")
        print("===========================")
        Membeli_lagi()
    else :
        print("Uang Anda Tidak Mencukupi")
        Kembali_ke_awal()

def Good_Day():
    HargaGD = 11000
    x = int(input("Masukkan Uang Anda   : "))
    if (x >= HargaGD):
        print("Kembalian Anda       = Rp.",x - HargaGD)
        print("Pembelian Berhasil")
        print("===========================")
        Membeli_lagi()
    else :
        print("Uang Anda Tidak Mencukupi")
        Kembali_ke_awal()

def Nestcafe():
    HargaN = 12500
    x = int(input("Masukkan Uang Anda   : "))
    if (x >= HargaN):
        print("Kembalian Anda       = Rp.",x - HargaN)
        print("Pembelian Berhasil")
        print("===========================")
        Membeli_lagi()
    else :
        print("Uang Anda Tidak Mencukupi")
        Kembali_ke_awal()

menampilkanjenis()
        
        
        
        
        
