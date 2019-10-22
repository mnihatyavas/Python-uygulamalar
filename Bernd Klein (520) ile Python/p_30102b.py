# coding:iso-8859-9 Türkçe
# p_30102b.py: Bir numpy dizisinin elemansız, herbir eleman ve eleman referans ebatları örneği.

from sys import getsizeof as ebat
import numpy as np

selsiyüsListesi = np.array ([20.1, 0, 21.9e10, -22.5, -22.7e-10, -0, 1, 21.2e100, -20.9e-100, 2])
elemanSayısı = len (selsiyüsListesi)

boşListeEbatı = ebat (selsiyüsListesi)   # []
listeElemanNesneleriEbatı = elemanSayısı * ebat (selsiyüsListesi[0]) # 20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.1
toplamEbat = boşListeEbatı + listeElemanNesneleriEbatı

print ("Numpy modül dizisi ve elemanlarının ebatlarını inceleyelim\n", "-"*58, sep="")
print ("Elemansız liste ebatı:", boşListeEbatı)
print ("Tüm eleman nesneleri ebatı:", listeElemanNesneleriEbatı)
print("Toplam elemanlı liste ebatı:", toplamEbat)

eleman = 0
print ("\nTek tek elemanların ebatları:")
for i in range (elemanSayısı):
    eleman +=ebat (selsiyüsListesi [i])
    print (selsiyüsListesi [i], "-->", ebat (selsiyüsListesi [i]) , sep="", end=", ")
print ("\n\nTüm elemanların gerçek toplam ebatı:", eleman)

selsiyüsListesi = np.array ([])
print ("\nElemansız yaratılan boş liste ebatı:", ebat (selsiyüsListesi))
print ("Herbir elemana referans için harcanan ebat:", int ((boşListeEbatı - ebat (selsiyüsListesi)) / elemanSayısı), "byte")



"""Çıktı:
>python p_30102b.py
Numpy modül dizisi ve elemanlarının ebatlarını inceleyelim
----------------------------------------------------------
Elemansız liste ebatı: 128
Tüm eleman nesneleri ebatı: 240
Toplam elemanlı liste ebatı: 368

Tek tek elemanların ebatları:
20.1-->24, 0.0-->24, 219000000000.0-->24, -22.5-->24, -2.27e-09-->24, 0.0-->24, 1.0-->24, 2.12e+101-->24, -2.09e-99-->24, 2.0-->24,

Tüm elemanların gerçek toplam ebatı: 240

Elemansız yaratılan boş liste ebatı: 48
Herbir elemana referans için harcanan ebat: 8 byte
"""