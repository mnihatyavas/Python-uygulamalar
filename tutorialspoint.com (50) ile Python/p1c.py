# -*- coding: iso-8859-9 -*-
# T�rk�e karakterlerinin tan�t�m�

import sys

dosyaAd� = input("Veri eklenecek/yarat�lacak dosya ad�: ")

try:
    # Dosya sistemini a�al�m...
    dosya = open (dosyaAd�, "a")
except IOError:
    print ("[", dosyaAd�, "] dosyas�na yazma problemi var!")
    sys.exit()

dosyaVerisi = input ("Veri girin [��k:son]: ")
while dosyaVerisi != "��k":
    if dosyaVerisi == "��k":
        break
    dosya.write (dosyaVerisi)
    dosya.write ("\n") # Bir alt sat�ra ge�er...
    dosyaVerisi = input ("Veri girin [��k:son]: ")

dosya.close()
print()

dosyaAd� = input ("��eri�i okunacak dosya ad�: ")
if len (dosyaAd�) == 0:
    print ("Dosya ad�n� girmeden Enter'�rlad�n!")
    sys.exit()

try:
    dosya = open (dosyaAd�, "r")
except IOError:
    print ("Dosya okuma hatas� olu�tu!")
    sys.exit()
dosyaVerisi = dosya.read() # T�m dosya i�eri�ini okur...
dosya.close()

print (dosyaVerisi)