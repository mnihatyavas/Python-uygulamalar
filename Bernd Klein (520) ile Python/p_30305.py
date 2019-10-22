# coding:iso-8859-9 Türkçe
# p_30305.py: 3 verili tüpleyi SS:dd:ss zaman tipine dönüştüren dtype örneği.

import numpy as np

zamanTipi = np.dtype ([('saat', int), ('dakika', int), ('saniye', int)])
zamanlar = np.array ([
    (11, 38, 5),
    (14, 56, 0),
    (3, 9, 1),
    (23, 59, 59),
    (0, 0, 0),
    (12, 59, 59),
    (13, 0, 0)], dtype=zamanTipi)

print ("Zamanların ardışık listesi:\n", zamanlar, sep="")

print ("\nZamanların alt-alta listesi:\n", "-"*30, sep="")
for i in range (len (zamanlar)): print (zamanlar [i])

print ("\nZamanların biçimli listesi:\n", "-"*27, "\nSt Dk Sn\n", "-"*8, sep="")
for i in range (len (zamanlar)): print ("{:02d}:{:02d}:{:02d}" .format (zamanlar [i] [0], zamanlar [i] [1], zamanlar [i] [2]) )

print ("\nİlk zamanlar elemanı:", zamanlar [0])
print ("Son zamanlar elemanı:", zamanlar [-1])

zamanlar [0] = (11, 33, 5) # İlk zamanı 5 dakika geri alalım...
#zamanlar[len(zamanlar)] = (13, 1, 0) # Son zamanı 1 dakika ilerletip ekleyelim...
print ("5 dk geri alınan ilk zamanlar elemanı:", zamanlar [0])



"""Çıktı:
>python p_30305.py
Zamanların ardışık listesi:
[(11, 38,  5) (14, 56,  0) ( 3,  9,  1) (23, 59, 59) ( 0,  0,  0)
 (12, 59, 59) (13,  0,  0)]

Zamanların alt-alta listesi:
------------------------------
(11, 38, 5)
(14, 56, 0)
(3, 9, 1)
(23, 59, 59)
(0, 0, 0)
(12, 59, 59)
(13, 0, 0)

Zamanların biçimli listesi:
---------------------------
St Dk Sn
--------
11:38:05
14:56:00
03:09:01
23:59:59
00:00:00
12:59:59
13:00:00

İlk zamanlar elemanı: (11, 38, 5)
Son zamanlar elemanı: (13, 0, 0)
5 dk geri alınan ilk zamanlar elemanı: (11, 33, 5)
"""