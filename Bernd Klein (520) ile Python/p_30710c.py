# coding:iso-8859-9 Türkçe
# p_30710c.py: Jeneratör üreteçle tesadüfilerin ağırlığını yüzde ellileme örneği.

import random

def tesadüfiBirSıfır (a):
    while True:
        x = random.random()
        yield 1 if x < a else 0

def üret (tesadüfiÜreteç, n):
    for i in range (n): yield next (tesadüfiÜreteç)

def yüzdeEllici (birSıfırlar):
    while True:
        bit1 = next (birSıfırlar)
        bit2 = next (birSıfırlar)
        if bit1 + bit2 == 1:
            bit3 = next (birSıfırlar)
            yield 1 if bit2 + bit3 == 1 else 0
        
def yüzdeEllici2 (birSıfırlar):
    bit1 = next (birSıfırlar)
    bit2 = next (birSıfırlar)
    bit3 = next (birSıfırlar)
    while True:
        if bit1 + bit2 == 1: yield 1 if bit2 + bit3 == 1 else 0
        bit1, bit2, bit3 = bit2, bit3, next (birSıfırlar)


try: kere = abs (int (input ("Kaç adet tesadüfi sayı üretsin [100 000]? ")))
except: kere = 100000

try: ağırlık = abs (eval (input ("[0->1] ağırlığı kaç olsun [0.85]? ")))
except: ağırlık = 0.85
if ağırlık > 1: ağırlık = 0.85

print ("\nSonuç-1: orijinal %", (ağırlık * 1000) / 10, " ağırlıklı ", kere, " adet 0/1'in ortalaması: %", int ((sum (x for x in üret (yüzdeEllici (tesadüfiBirSıfır (ağırlık)), kere)) / kere) * 10000000) / 100000.0, sep="")
print ("Sonuç-2: orijinal %", (ağırlık * 1000) / 10, " ağırlıklı ", kere, " adet 0/1'in ortalaması: %", int ((sum (x for x in üret (yüzdeEllici (tesadüfiBirSıfır (ağırlık)), kere)) / kere) * 10000000) / 100000.0, sep="")



"""Çıktı:
>python p_30710c.py
Kaç adet tesadüfi sayı üretsin [100 000]?
[0->1] ağırlığı kaç olsun [0.85]?

Sonuç-1: orijinal %85.0 ağırlıklı 100000 adet 0/1'in ortalaması: %49.869
Sonuç-2: orijinal %85.0 ağırlıklı 100000 adet 0/1'in ortalaması: %50.043

>python p_30710c.py  ** TEKRAR **
Kaç adet tesadüfi sayı üretsin [100 000]? 10000
[0->1] ağırlığı kaç olsun [0.85]? 0.25

Sonuç-1: orijinal %25.0 ağırlıklı 10000 adet 0/1'in ortalaması: %49.08399
Sonuç-2: orijinal %25.0 ağırlıklı 10000 adet 0/1'in ortalaması: %50.0
"""