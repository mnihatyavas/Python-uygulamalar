# -*- coding: iso-8859-9 -*-
# Türkçe karakterlerinin tanıtımı

import sys

dosyaAdı = input("Veri eklenecek/yaratılacak dosya adı: ")

try:
    # Dosya sistemini açalım...
    dosya = open (dosyaAdı, "a")
except IOError:
    print ("[", dosyaAdı, "] dosyasına yazma problemi var!")
    sys.exit()

dosyaVerisi = input ("Veri girin [çık:son]: ")
while dosyaVerisi != "çık":
    if dosyaVerisi == "çık":
        break
    dosya.write (dosyaVerisi)
    dosya.write ("\n") # Bir alt satıra geçer...
    dosyaVerisi = input ("Veri girin [çık:son]: ")

dosya.close()
print()

dosyaAdı = input ("İçeriği okunacak dosya adı: ")
if len (dosyaAdı) == 0:
    print ("Dosya adını girmeden Enter'ırladın!")
    sys.exit()

try:
    dosya = open (dosyaAdı, "r")
except IOError:
    print ("Dosya okuma hatası oluştu!")
    sys.exit()
dosyaVerisi = dosya.read() # Tüm dosya içeriğini okur...
dosya.close()

print (dosyaVerisi)