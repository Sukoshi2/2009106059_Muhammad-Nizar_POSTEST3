# -*- coding: utf-8 -*-
"""percabangans.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ieSWs9WBw1AsZzDw7oVjiE-kNnpTz-8g
"""

print(" Selamat datang di Shiro TAKO ")
print(" Silahkan pilih menu varian ")
print("         ==== MENU ====")
print("1. Takoyaki isi cumi-cumi  PER PCSRp.2000")
print("2. Takoyaki isi gurita     PER PCSRp.2500")
print("         ==== MENU ====")
total1 = 0
total2 = 0
total_semua = 0
jenis1 = ""
jenis2 = ""

stop = False
while(not stop):
  pesanan = int(input("Masukan nomor varian yang ingin di beli : "))
  if (pesanan == 1):
    pcs = int(input("Masukan berapa jumlah yang ingin di beli : "))
    if (pcs <= 45):
      total1 = pcs * 2000
      print("harga sebelum diskon yaitu Rp.", total1)
      if pcs > 10:
        print("anda mendapatkan diskon sebesar 10% ")
        diskon = 10/100 * total1
        print("total diskon yaitu Rp.", diskon)
        setelah_diskon = total1 - diskon
        print("yang harus dibayar Rp.", setelah_diskon)
      else:
        print("saat ini diskon hanya di atas 10 pembelian")
    else:
      print("Maaf, Pesanan terlalu banyak")
  elif (pesanan == 2):
    pcs = int(input("Masukan berapa jumlah yang ingin di beli :"))
    if (pcs <= 40):
      total2 = pcs * 2500
      print("harga sebelum diskon yaitu Rp.", total2)
      if pcs > 8:
        print("anda mendapatkan diskon sebesar 8% ")
        diskon = 8/100 * total2
        print("total diskon yaitu Rp.", diskon)
        setelah_diskon = total2 - diskon
        print("yang harus dibayar Rp.", setelah_diskon)
      else:
        print("saat ini diskon hanya di atas 8 pembelian")
    else:
      print("Maaf, Pesanan terlalu banyak")   

  else :    
    while True:
        print("=====Menu saat ini Tidak Tersedia=====")
        break
    pesanan = int(input("Masukan nomor varian yang ingin di beli : "))
    if (pesanan == 1):
      pcs = int(input("Masukan berapa jumlah yang ingin di beli : "))
      if (pcs <= 45):
        total1 = pcs * 2000
        print("harga sebelum diskon yaitu Rp.", total1)
        if pcs > 10:
          print("anda mendapatkan diskon sebesar 10% ")
          diskon = 10/100 - total1
          print("total diskon yaitu Rp.", diskon)
          setelah_diskon = total1 - diskon
          print("yang harus dibayar Rp.", setelah_diskon)
        else:
          print("saat ini diskon hanya di atas 10 pembelian")
      else:
        print("Maaf, Pesanan terlalu banyak")
    elif (pesanan == 2):
      pcs = int(input("Masukan berapa jumlah yang ingin di beli :"))
      if (pcs <= 40):
        total2 = pcs * 2500
        print("harga sebelum diskon yaitu Rp.", total2)
        if pcs > 8:
          print("anda mendapatkan diskon sebesar 8% ")
          diskon = 8/100 * total2
          print("total diskon yaitu yaitu Rp.", diskon)
          setelah_diskon = total2 - diskon
          print("yang harus dibayar Rp.", setelah_diskon)
        else:
          print("saat ini diskon hanya di atas 8 pembelian")
      else:
        print("Maaf, Pesanan terlalu banyak")
  ulang = input("Ada yang mau di beli lagi?")
  if (ulang == "tidak"):
      stop = True


print("======== Terimakasih! =========")
print("=====Selamat datang Kembali====")