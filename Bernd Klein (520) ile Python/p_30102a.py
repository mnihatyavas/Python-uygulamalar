# coding:iso-8859-9 Türkçe
# p_30102a.py: Bir listenin elemansız, herbir eleman ve eleman referans ebatları örneği.

from sys import getsizeof as ebat

selsiyüsListesi = [20.1, 0, 21.9e10, -22.5, -22.7e-10, -0, 1, 21.2e100, -20.9e-100, 2]
elemanSayısı = len (selsiyüsListesi)

boşListeEbatı = ebat (selsiyüsListesi)   # []
listeElemanNesneleriEbatı = elemanSayısı * ebat (selsiyüsListesi [0]) # 20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.1
toplamEbat = boşListeEbatı + listeElemanNesneleriEbatı

print ("Normal bir python listesi ve elemanlarının ebatlarını inceleyelim\n", "-"*65, sep="")
print ("Elemansız liste ebatı:", boşListeEbatı)
print ("Tüm eleman nesneleri ebatı:", listeElemanNesneleriEbatı)
print("Toplam elemanlı liste ebatı:", toplamEbat)

eleman = 0
print ("\nTek tek elemanların ebatları:")
for i in range (elemanSayısı):
    eleman +=ebat (selsiyüsListesi [i])
    print (selsiyüsListesi [i], "-->", ebat (selsiyüsListesi [i]) , sep="", end=", ")
print ("\n\nTüm elemanların gerçek toplam ebatı:", eleman)

selsiyüsListesi = []
print ("\nElemansız yaratılan boş liste ebatı:", ebat (selsiyüsListesi))
print ("Herbir elemana referans için harcanan ebat:", int ((boşListeEbatı - ebat (selsiyüsListesi)) / elemanSayısı), "byte")



"""Çıktı:
>python p_30102a.py
Normal bir python listesi ve elemanlarının ebatlarını inceleyelim
-----------------------------------------------------------------
Elemansız liste ebatı: 76
Tüm eleman nesneleri ebatı: 160
Toplam elemanlı liste ebatı: 236

Tek tek elemanların ebatları:
20.1-->16, 0-->12, 219000000000.0-->16, -22.5-->16, -2.27e-09-->16, 0-->12, 1-->14, 2.12e+101-->16, -2.09e-99-->16, 2-->14,

Tüm elemanların gerçek toplam ebatı: 148

Elemansız yaratılan boş liste ebatı: 36
Herbir elemana referans için harcanan ebat: 4 byte
"""