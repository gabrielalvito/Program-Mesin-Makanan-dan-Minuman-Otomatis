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
