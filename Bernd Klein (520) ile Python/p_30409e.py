# coding:iso-8859-9 T�rk�e
# p_30409e.py: Sat�r matrisinin numpy.tile ile �ok boyutluya eklenmesi �rne�i.

import numpy as np

A = np.array ([
    [11, 12, 13],
    [21, 22, 23],
    [31, 32, 33] ])

B = np.array ([1, 2, 3])
B1 = np.tile (B, (3, 1)) # Sat�r 3 kez, s�tun 1 kez eklenir...

print ("A(3,3) matrisi:\n", A, "==>", A.shape, "\n\nB(3,) dizisi: ", B, "==>", B.shape,
    "\n\n��l� 'tile' sat�r ekleme sonucu B1(3,3) matrisi:\n", B1, "==>", B1.shape, sep="")
print ("\nMatris bire-bir �arpma (A*B1):\n", (A * B1),
    "\n\nMatris bire-bir toplama (A+B1):\n", (A + B1), sep="")



"""��kt�:
>python p_30409e.py
A(3,3) matrisi:
[[11 12 13]
 [21 22 23]
 [31 32 33]]==>(3, 3)

B(3,) dizisi: [1 2 3]==>(3,)

��l� 'tile' sat�r ekleme sonucu B1(3,3) matrisi:
[[1 2 3]
 [1 2 3]
 [1 2 3]]==>(3, 3)

Matris bire-bir �arpma (A*B1):
[[11 24 39]
 [21 44 69]
 [31 64 99]]

Matris bire-bir toplama (A+B1):
[[12 14 16]
 [22 24 26]
 [32 34 36]]

"""