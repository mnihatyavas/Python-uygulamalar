# coding:iso-8859-9 "Türkçe"
import os, sys

def fonksiyonum1():
    print ("Bir fonksiyon tanımından herkese selamlar!")

fonksiyonum1()
print()

def fonksiyonum2 (ad):
    print (ad + " Yavaş")

fonksiyonum2 ("Mahmut Nihat")
fonksiyonum2 ("Sevim")
fonksiyonum2 ("Mustafa Nedim")
print()

def fonksiyonum3 (ülke = "Türkiye"): # Varsayılı değer atama...
    print ("Memleketim:" + ülke)

fonksiyonum3 ("Amerika")
fonksiyonum3() # Varsayılı değer görüntülenecek...
fonksiyonum3 ("Almanya")
print()

def fonksiyonum4 (sayı):
    return 5 * pow (sayı, 0.37)

print ("5 * 3^0.37 =", fonksiyonum4 (3))
print ("5 * 5^0.37 =", fonksiyonum4 (5))
print ("5 * 9.7862^0.37 =", fonksiyonum4 (9.7862))
