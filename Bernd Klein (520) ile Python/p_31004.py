# coding:iso-8859-9 T�rk�e
# p_31004.py: Numpy matrissel �arp�ml� al��veri� �rne�i.

import numpy as np

# 4 m��terinin herbirinin A, B, C mallar�ndan sat�n ald�klar� gramajlar...
m��teriler = np.array ([
    [100, 175, 210],
    [90, 160, 150],
    [200, 50, 100],
    [120, 0, 310] ])

# A, B ve C mallar�n�n 100 gram�n�n TL fiyatlar�...
fiyatlar = np.array ([2.98, 3.90, 1.99])

tutarlarTL = np.dot (m��teriler / 1000, fiyatlar * 10) # TL fiyatlar�...
# gr->kg i�in m��teriler/1000 ve 100gr->1kg i�in de fiyatlar*10 al�nmal�...

print ("M��terilerin gram cinsinden sat�n ald�klar� A, B ve C mal miktarlar� dizisi:\n",
    m��teriler, " ==>�ekli: ", m��teriler.shape, sep="")
print ("\nA, B ve C mallar�n�n 100 gram TL fiyatlar� dizisi:\n", fiyatlar,
    " ==>�ekli: ", fiyatlar.shape, sep="")
print ("\nHerbir m��terinin sat�n ald�klar�n�n (matrissel �arp�m) TL tutarlar�:\n",
    tutarlarTL, " ==>�ekli: ", tutarlarTL.shape, sep="")
print ("\nAl��veri� genel toplam�:", int (tutarlarTL.sum() * 100) / 100, "TL")



"""��kt�:
>python p_31004.py
M��terilerin gram cinsinden sat�n ald�klar� A, B ve C mal miktarlar� dizisi:
[[100 175 210]
 [ 90 160 150]
 [200  50 100]
 [120   0 310]] ==>�ekli: (4, 3)

A, B ve C mallar�n�n 100 gram TL fiyatlar� dizisi:
[2.98 3.9  1.99] ==>�ekli: (3,) = (3, 1)

Herbir m��terinin sat�n ald�klar�n�n (matrissel �arp�m) TL tutarlar�:
[13.984 11.907  9.9    9.745] ==>�ekli: (4,) = (4, 1) transpose()

Al��veri� genel toplam�: 45.53 TL
"""