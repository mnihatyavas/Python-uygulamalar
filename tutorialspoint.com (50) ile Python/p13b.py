# coding:iso-8859-9 T�rk�e

para = 2000

def paraEkle():
    global para # Yoksa HATA: "UnboundLocalError: local variable 'para' referenced before assignment"
    para += 100

print (para)
paraEkle()
print (para)

import math

i�erik = dir (math)
print ("\nmath mod�l isimleri:", i�erik)
