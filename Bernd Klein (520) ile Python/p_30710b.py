# coding:iso-8859-9 Türkçe
# p_30710b.py: Jeneratör üreteçle ağırlık nisbetinde tesadüfi sıfır ve bir üretme örneği.

import random

def tesadüfiBirSıfır (a):
    while True:
        x = random.random()
        yield 1 if x < a else 0

def üret (tesadüfiÜreteç, n):
    for i in range (n): yield next (tesadüfiÜreteç)

try: kere = abs (int (input ("Kaç adet tesadüfi sayı üretsin [1 000 000]? ")))
except: kere = 1000000

try: ağırlık = abs (eval (input ("[0->1] ağırlığı kaç olsun [0.50]? ")))
except: ağırlık = 0.5
if ağırlık > 1: ağırlık = 0.5

print ("\nSonuç: %", (ağırlık * 1000) / 10, " ağırlıklı ", kere, " adet 0/1'in ortalaması: %", (sum (_ for _ in üret (tesadüfiBirSıfır (ağırlık), kere)) / kere) * 1000 / 10, sep="")



"""Çıktı:
>python p_30710b.py
Kaç adet tesadüfi sayı üretsin [1 000 000]? 100
[0->1] ağırlığı kaç olsun [0.50]? 0.85

Sonuç: %85.0 ağırlıklı 100 adet 0/1'in ortalaması: %87.0

>python p_30710b.py  ** TEKRAR **
Kaç adet tesadüfi sayı üretsin [1 000 000]? 10000
[0->1] ağırlığı kaç olsun [0.50]? 0.257

Sonuç: %25.7 ağırlıklı 10000 adet 0/1'in ortalaması: %25.779999999999994

>python p_30710b.py  ** TEKRAR **
Kaç adet tesadüfi sayı üretsin [1 000 000]?
[0->1] ağırlığı kaç olsun [0.50]?

Sonuç: %50.0 ağırlıklı 1000000 adet 0/1'in ortalaması: %50.0561
"""