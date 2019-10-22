# coding:iso-8859-9 Türkçe
# p_31004.py: Numpy matrissel çarpımlı alışveriş örneği.

import numpy as np

# 4 müşterinin herbirinin A, B, C mallarından satın aldıkları gramajlar...
müşteriler = np.array ([
    [100, 175, 210],
    [90, 160, 150],
    [200, 50, 100],
    [120, 0, 310] ])

# A, B ve C mallarının 100 gramının TL fiyatları...
fiyatlar = np.array ([2.98, 3.90, 1.99])

tutarlarTL = np.dot (müşteriler / 1000, fiyatlar * 10) # TL fiyatları...
# gr->kg için müşteriler/1000 ve 100gr->1kg için de fiyatlar*10 alınmalı...

print ("Müşterilerin gram cinsinden satın aldıkları A, B ve C mal miktarları dizisi:\n",
    müşteriler, " ==>Şekli: ", müşteriler.shape, sep="")
print ("\nA, B ve C mallarının 100 gram TL fiyatları dizisi:\n", fiyatlar,
    " ==>Şekli: ", fiyatlar.shape, sep="")
print ("\nHerbir müşterinin satın aldıklarının (matrissel çarpım) TL tutarları:\n",
    tutarlarTL, " ==>Şekli: ", tutarlarTL.shape, sep="")
print ("\nAlışveriş genel toplamı:", int (tutarlarTL.sum() * 100) / 100, "TL")



"""Çıktı:
>python p_31004.py
Müşterilerin gram cinsinden satın aldıkları A, B ve C mal miktarları dizisi:
[[100 175 210]
 [ 90 160 150]
 [200  50 100]
 [120   0 310]] ==>Şekli: (4, 3)

A, B ve C mallarının 100 gram TL fiyatları dizisi:
[2.98 3.9  1.99] ==>Şekli: (3,) = (3, 1)

Herbir müşterinin satın aldıklarının (matrissel çarpım) TL tutarları:
[13.984 11.907  9.9    9.745] ==>Şekli: (4,) = (4, 1) transpose()

Alışveriş genel toplamı: 45.53 TL
"""