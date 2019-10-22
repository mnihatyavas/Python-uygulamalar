# coding:iso-8859-9 T�rk�e
# p_30902.py: Numpy dizi elemanlar�n� boolean ve randint'le s�zge�leme �rne�i.

import numpy as np
from random import randint

A = np.array ([123, 188, 190, 99, 77, 88, 100])
B = np.array ([4, 7, 2, 8, 6, 9, 5])
C = B <= 5
D = A[C]

print ("A dizisi: ", A, "\nB dizisi: ", B,
    "\n(B <= 5) Boolean �evrimi: ", C,
    "\nC'nin True'lar�n�n konumlar�n� A s�zge� endeksi yap: ", D, sep="")
print ("-"*70)
#--------------------------------------------------------------------------------------------------------

print ("\nA dizisinin (0, 2, 3, 1, 6, 1) endeks elemanlar�n� g�ster:\n", A[[0, 2, 3, 1, 6, 1]])
print ("\nA dizisinin geli�ig�zel 10 eleman�n� g�ster:\n", A[[randint (0,6) for i in range (10)]])



"""��kt�:
>python p_30902.py
A dizisi: [123 188 190  99  77  88 100]
B dizisi: [4 7 2 8 6 9 5]
(B <= 5) Boolean �evrimi: [ True False  True False False False  True]
C'nin True'lar�n�n konumlar�n� A s�zge� endeksi yap: [123 190 100]
----------------------------------------------------------------------

A dizisinin (0, 2, 3, 1, 6, 1) endeks elemanlar�n� g�ster:
 [123 190  99 188 100 188]

A dizisinin geli�ig�zel 10 eleman�n� g�ster:
 [ 77 100  99 188 123 100 188 100 123  99]
"""