# coding:iso-8859-9 Türkçe
# p_30409a.py: Skalar/sayısal çarpma ve toplamada küçük matrisin büyüğe otomatik yayılması örneği.

import numpy as np

A = np.array ([
    [11, 12, 13],
    [21, 22, 23],
    [31, 32, 33] ])

B = np.array ([1, 2, 3])

b = np.array ([
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3] ])

# A ve B dizileri farklıysa, Numpy işlemleri büyüğe uyumluluk yayılımıyla gerçekleştirir...

print ("A ve B dizileri:\n", A, "\n\n", B, sep="")
print ("\n'A*B' bire-bir çarpım:\n", (A * B), sep="")
print ("\n'A+B' bire-bir toplam:\n", (A + B), sep="")

print ("\nBüyük A'ya otomatikmen uyumlu yayılan B dizisi:\n", b, sep="")



"""Çıktı:
>python p_30409a.py
A ve B dizileri:
[[11 12 13]
 [21 22 23]
 [31 32 33]]

[1 2 3]

'A*B' bire-bir çarpım:
[[11 24 39]
 [21 44 69]
 [31 64 99]]

'A+B' bire-bir toplam:
[[12 14 16]
 [22 24 26]
 [32 34 36]]

Büyük A'ya otomatikmen uyumlu yayılan B dizisi:
[[1 2 3]
 [1 2 3]
 [1 2 3]]
"""