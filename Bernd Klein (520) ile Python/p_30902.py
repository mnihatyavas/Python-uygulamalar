# coding:iso-8859-9 Türkçe
# p_30902.py: Numpy dizi elemanlarını boolean ve randint'le süzgeçleme örneği.

import numpy as np
from random import randint

A = np.array ([123, 188, 190, 99, 77, 88, 100])
B = np.array ([4, 7, 2, 8, 6, 9, 5])
C = B <= 5
D = A[C]

print ("A dizisi: ", A, "\nB dizisi: ", B,
    "\n(B <= 5) Boolean çevrimi: ", C,
    "\nC'nin True'larının konumlarını A süzgeç endeksi yap: ", D, sep="")
print ("-"*70)
#--------------------------------------------------------------------------------------------------------

print ("\nA dizisinin (0, 2, 3, 1, 6, 1) endeks elemanlarını göster:\n", A[[0, 2, 3, 1, 6, 1]])
print ("\nA dizisinin gelişigüzel 10 elemanını göster:\n", A[[randint (0,6) for i in range (10)]])



"""Çıktı:
>python p_30902.py
A dizisi: [123 188 190  99  77  88 100]
B dizisi: [4 7 2 8 6 9 5]
(B <= 5) Boolean çevrimi: [ True False  True False False False  True]
C'nin True'larının konumlarını A süzgeç endeksi yap: [123 190 100]
----------------------------------------------------------------------

A dizisinin (0, 2, 3, 1, 6, 1) endeks elemanlarını göster:
 [123 190  99 188 100 188]

A dizisinin gelişigüzel 10 elemanını göster:
 [ 77 100  99 188 123 100 188 100 123  99]
"""