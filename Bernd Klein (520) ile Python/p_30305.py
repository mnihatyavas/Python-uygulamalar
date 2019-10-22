# coding:iso-8859-9 T�rk�e
# p_30305.py: 3 verili t�pleyi SS:dd:ss zaman tipine d�n��t�ren dtype �rne�i.

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

print ("Zamanlar�n ard���k listesi:\n", zamanlar, sep="")

print ("\nZamanlar�n alt-alta listesi:\n", "-"*30, sep="")
for i in range (len (zamanlar)): print (zamanlar [i])

print ("\nZamanlar�n bi�imli listesi:\n", "-"*27, "\nSt Dk Sn\n", "-"*8, sep="")
for i in range (len (zamanlar)): print ("{:02d}:{:02d}:{:02d}" .format (zamanlar [i] [0], zamanlar [i] [1], zamanlar [i] [2]) )

print ("\n�lk zamanlar eleman�:", zamanlar [0])
print ("Son zamanlar eleman�:", zamanlar [-1])

zamanlar [0] = (11, 33, 5) # �lk zaman� 5 dakika geri alal�m...
#zamanlar[len(zamanlar)] = (13, 1, 0) # Son zaman� 1 dakika ilerletip ekleyelim...
print ("5 dk geri al�nan ilk zamanlar eleman�:", zamanlar [0])



"""��kt�:
>python p_30305.py
Zamanlar�n ard���k listesi:
[(11, 38,  5) (14, 56,  0) ( 3,  9,  1) (23, 59, 59) ( 0,  0,  0)
 (12, 59, 59) (13,  0,  0)]

Zamanlar�n alt-alta listesi:
------------------------------
(11, 38, 5)
(14, 56, 0)
(3, 9, 1)
(23, 59, 59)
(0, 0, 0)
(12, 59, 59)
(13, 0, 0)

Zamanlar�n bi�imli listesi:
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

�lk zamanlar eleman�: (11, 38, 5)
Son zamanlar eleman�: (13, 0, 0)
5 dk geri al�nan ilk zamanlar eleman�: (11, 33, 5)
"""