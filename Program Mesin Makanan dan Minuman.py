# PROGRAM MESIN MAKANAN DAN MINUMAN
# Menu Utama
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
