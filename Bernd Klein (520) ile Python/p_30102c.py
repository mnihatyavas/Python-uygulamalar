# coding:iso-8859-9 Türkçe
# p_30102c.py: Bir numpy float16 tipli dizisinin elemansız, herbir eleman ve eleman referans ebatları örneği.

from sys import getsizeof as ebat
import numpy as np

# float16/32/64 ve int8/16/32/64 olarak tahsis edilecek bellek ebatı kullanıcı tarafından belirlenebilir...
# Varsayılan int64 ve float64'dür...

selsiyüsListesi = np.array ([20.1, 0, 21.9e10, -22.5, -22.7e-10, -0, 1, 21.2e100, -20.9e-100, 2], np.float16)
elemanSayısı = len (selsiyüsListesi)

boşListeEbatı = ebat (selsiyüsListesi)   # []
listeElemanNesneleriEbatı = elemanSayısı * ebat (selsiyüsListesi[0]) # 20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.1
toplamEbat = boşListeEbatı + listeElemanNesneleriEbatı

print ("Numpy modül dizisi ve elemanlarının ebatlarını (np.float16) inceleyelim\n", "-"*71, sep="")
print ("Elemansız liste ebatı:", boşListeEbatı)
print ("Tüm eleman nesneleri ebatı:", listeElemanNesneleriEbatı)
print("Toplam elemanlı liste ebatı:", toplamEbat)

eleman = 0
print ("\nTek tek elemanların ebatları:")
for i in range (elemanSayısı):
    eleman +=ebat (selsiyüsListesi[i])
    print (selsiyüsListesi[i], "-->", ebat (selsiyüsListesi[i]) , sep="", end=", ")
print ("\n\nTüm elemanların gerçek toplam ebatı:", eleman)

selsiyüsListesi = np.array ([])
print ("\nElemansız yaratılan boş liste ebatı:", ebat (selsiyüsListesi))
print ("Herbir elemana referans için harcanan ebat:", int ((boşListeEbatı - ebat (selsiyüsListesi)) / elemanSayısı), "byte")



"""Çıktı:
>python p_30102c.py
Numpy modül dizisi ve elemanlarının ebatlarını (np.float16) inceleyelim
-----------------------------------------------------------------------
Elemansız liste ebatı: 68
Tüm eleman nesneleri ebatı: 140
Toplam elemanlı liste ebatı: 208

Tek tek elemanların ebatları:
20.1-->14, 0.0-->14, inf-->14, -22.5-->14, -0.0-->14, 0.0-->14, 1.0-->14, inf-->14, -0.0-->14, 2.0-->14,

Tüm elemanların gerçek toplam ebatı: 140

Elemansız yaratılan boş liste ebatı: 48
Herbir elemana referans için harcanan ebat: 2 byte
"""