# coding:iso-8859-9 T�rk�e
# p_30102c.py: Bir numpy float16 tipli dizisinin elemans�z, herbir eleman ve eleman referans ebatlar� �rne�i.

from sys import getsizeof as ebat
import numpy as np

# float16/32/64 ve int8/16/32/64 olarak tahsis edilecek bellek ebat� kullan�c� taraf�ndan belirlenebilir...
# Varsay�lan int64 ve float64'd�r...

selsiy�sListesi = np.array ([20.1, 0, 21.9e10, -22.5, -22.7e-10, -0, 1, 21.2e100, -20.9e-100, 2], np.float16)
elemanSay�s� = len (selsiy�sListesi)

bo�ListeEbat� = ebat (selsiy�sListesi)   # []
listeElemanNesneleriEbat� = elemanSay�s� * ebat (selsiy�sListesi[0]) # 20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.1
toplamEbat = bo�ListeEbat� + listeElemanNesneleriEbat�

print ("Numpy mod�l dizisi ve elemanlar�n�n ebatlar�n� (np.float16) inceleyelim\n", "-"*71, sep="")
print ("Elemans�z liste ebat�:", bo�ListeEbat�)
print ("T�m eleman nesneleri ebat�:", listeElemanNesneleriEbat�)
print("Toplam elemanl� liste ebat�:", toplamEbat)

eleman = 0
print ("\nTek tek elemanlar�n ebatlar�:")
for i in range (elemanSay�s�):
    eleman +=ebat (selsiy�sListesi[i])
    print (selsiy�sListesi[i], "-->", ebat (selsiy�sListesi[i]) , sep="", end=", ")
print ("\n\nT�m elemanlar�n ger�ek toplam ebat�:", eleman)

selsiy�sListesi = np.array ([])
print ("\nElemans�z yarat�lan bo� liste ebat�:", ebat (selsiy�sListesi))
print ("Herbir elemana referans i�in harcanan ebat:", int ((bo�ListeEbat� - ebat (selsiy�sListesi)) / elemanSay�s�), "byte")



"""��kt�:
>python p_30102c.py
Numpy mod�l dizisi ve elemanlar�n�n ebatlar�n� (np.float16) inceleyelim
-----------------------------------------------------------------------
Elemans�z liste ebat�: 68
T�m eleman nesneleri ebat�: 140
Toplam elemanl� liste ebat�: 208

Tek tek elemanlar�n ebatlar�:
20.1-->14, 0.0-->14, inf-->14, -22.5-->14, -0.0-->14, 0.0-->14, 1.0-->14, inf-->14, -0.0-->14, 2.0-->14,

T�m elemanlar�n ger�ek toplam ebat�: 140

Elemans�z yarat�lan bo� liste ebat�: 48
Herbir elemana referans i�in harcanan ebat: 2 byte
"""