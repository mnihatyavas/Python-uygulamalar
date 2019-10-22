# coding:iso-8859-9 Türkçe

para = 2000

def paraEkle():
    global para # Yoksa HATA: "UnboundLocalError: local variable 'para' referenced before assignment"
    para += 100

print (para)
paraEkle()
print (para)

import math

içerik = dir (math)
print ("\nmath modül isimleri:", içerik)
