# coding:iso-8859-9 T�rk�e
# p_30102b.py: Bir numpy dizisinin elemans�z, herbir eleman ve eleman referans ebatlar� �rne�i.

from sys import getsizeof as ebat
import numpy as np

selsiy�sListesi = np.array ([20.1, 0, 21.9e10, -22.5, -22.7e-10, -0, 1, 21.2e100, -20.9e-100, 2])
elemanSay�s� = len (selsiy�sListesi)

bo�ListeEbat� = ebat (selsiy�sListesi)   # []
listeElemanNesneleriEbat� = elemanSay�s� * ebat (selsiy�sListesi[0]) # 20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.1
toplamEbat = bo�ListeEbat� + listeElemanNesneleriEbat�

print ("Numpy mod�l dizisi ve elemanlar�n�n ebatlar�n� inceleyelim\n", "-"*58, sep="")
print ("Elemans�z liste ebat�:", bo�ListeEbat�)
print ("T�m eleman nesneleri ebat�:", listeElemanNesneleriEbat�)
print("Toplam elemanl� liste ebat�:", toplamEbat)

eleman = 0
print ("\nTek tek elemanlar�n ebatlar�:")
for i in range (elemanSay�s�):
    eleman +=ebat (selsiy�sListesi [i])
    print (selsiy�sListesi [i], "-->", ebat (selsiy�sListesi [i]) , sep="", end=", ")
print ("\n\nT�m elemanlar�n ger�ek toplam ebat�:", eleman)

selsiy�sListesi = np.array ([])
print ("\nElemans�z yarat�lan bo� liste ebat�:", ebat (selsiy�sListesi))
print ("Herbir elemana referans i�in harcanan ebat:", int ((bo�ListeEbat� - ebat (selsiy�sListesi)) / elemanSay�s�), "byte")



"""��kt�:
>python p_30102b.py
Numpy mod�l dizisi ve elemanlar�n�n ebatlar�n� inceleyelim
----------------------------------------------------------
Elemans�z liste ebat�: 128
T�m eleman nesneleri ebat�: 240
Toplam elemanl� liste ebat�: 368

Tek tek elemanlar�n ebatlar�:
20.1-->24, 0.0-->24, 219000000000.0-->24, -22.5-->24, -2.27e-09-->24, 0.0-->24, 1.0-->24, 2.12e+101-->24, -2.09e-99-->24, 2.0-->24,

T�m elemanlar�n ger�ek toplam ebat�: 240

Elemans�z yarat�lan bo� liste ebat�: 48
Herbir elemana referans i�in harcanan ebat: 8 byte
"""