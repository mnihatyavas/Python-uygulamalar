# coding:iso-8859-9 Türkçe
# p_30409d.py: Satır matrisinin numpy.concatenate'le çok boyutlu matrise uyarlanması örneği.

import numpy as np

A = np.array ([
    [11, 12, 13],
    [21, 22, 23],
    [31, 32, 33] ])

B = np.array ([1, 2, 3])
B1 = B[np.newaxis, :]
B2 = np.concatenate ((B1, B1, B1))

print ("A(3,3) matrisi:\n", A, "==>", A.shape, "\n\nB(3,) dizisi: ", B, "==>", B.shape,
    "\n\nB1(1,3) matrisi:\n", B1, "==>", B1.shape,
    "\n\nÜçlü 'concatenate' ekleme sonucu B2(3,3) matrisi:\n", B2, "==>", B2.shape, sep="")
print ("\nMatris bire-bir çarpma (A*B2):\n", (A * B2),
    "\n\nMatris bire-bir toplama (A+B2):\n", (A + B2), sep="")


"""Çıktı:
>python p_30409d.py
A(3,3) matrisi:
[[11 12 13]
 [21 22 23]
 [31 32 33]]==>(3, 3)

B(3,) dizisi: [1 2 3]==>(3,)

B1(1,3) matrisi:
[[1 2 3]]==>(1, 3)

Üçlü 'concatenate' ekleme sonucu B2(3,3) matrisi:
[[1 2 3]
 [1 2 3]
 [1 2 3]]==>(3, 3)

Matris bire-bir çarpma (A*B2):
[[11 24 39]
 [21 44 69]
 [31 64 99]]

Matris bire-bir toplama (A+B2):
[[12 14 16]
 [22 24 26]
 [32 34 36]]
"""