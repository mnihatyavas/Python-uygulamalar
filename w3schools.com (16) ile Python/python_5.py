# coding:iso-8859-9 "T�rk�e"
import os, sys

def fonksiyonum1():
    print ("Bir fonksiyon tan�m�ndan herkese selamlar!")

fonksiyonum1()
print()

def fonksiyonum2 (ad):
    print (ad + " Yava�")

fonksiyonum2 ("Mahmut Nihat")
fonksiyonum2 ("Sevim")
fonksiyonum2 ("Mustafa Nedim")
print()

def fonksiyonum3 (�lke = "T�rkiye"): # Varsay�l� de�er atama...
    print ("Memleketim:" + �lke)

fonksiyonum3 ("Amerika")
fonksiyonum3() # Varsay�l� de�er g�r�nt�lenecek...
fonksiyonum3 ("Almanya")
print()

def fonksiyonum4 (say�):
    return 5 * pow (say�, 0.37)

print ("5 * 3^0.37 =", fonksiyonum4 (3))
print ("5 * 5^0.37 =", fonksiyonum4 (5))
print ("5 * 9.7862^0.37 =", fonksiyonum4 (9.7862))
