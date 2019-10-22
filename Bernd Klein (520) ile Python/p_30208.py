# coding:iso-8859-9 Türkçe
# p_30208.py: numpy.array ile 2 boyutluda atlama [::m, ::n], 3 boyutluda ara dilim [n1:n2, m1:m2, :] örneği.

import numpy as np

X = np.arange (28).reshape (4, 7) # reshape, tek boyutlu X'i 4x7 boyutluya yeniden şekillendirir...
print ("Dizi X:\n", X, "\nŞekli: ", X.shape, "\nSatır-sütun 2-3 atlayarak X[::2, ::3]:\n", X[::2, ::3],
    "\nSütun 3'er atlayarak X[::, ::3]:\n", X[::, ::3], sep="")

A = np.array ([ # 3 boyutlu diziyle atlamalı dilimleme...
    [[45, 10, 1], [45, 11, 2], [45, 12, 3]],
    [[46, 13, 4], [46, 14, 5], [46, 15, 6]],
    [[47, 16, 7], [47, 17, 8], [47, 18, 9]] ])
print ("\nDizi A:\n", A, "\nŞekli: ", A.shape, "\nA[1:3, 0:2, :] dilimi:\n", A[1:3, 0:2], sep="")



"""Çıktı:
>python p_30208.py
Dizi X:
[[ 0  1  2  3  4  5  6]
 [ 7  8  9 10 11 12 13]
 [14 15 16 17 18 19 20]
 [21 22 23 24 25 26 27]]
Şekli: (4, 7)
Satır-sütun 2-3 atlayarak X[::2, ::3]:
[[ 0  3  6]
 [14 17 20]]
Sütun 3'er atlayarak X[::, ::3]:
[[ 0  3  6]
 [ 7 10 13]
 [14 17 20]
 [21 24 27]]

Dizi A:
[[[45 10  1]
  [45 11  2]
  [45 12  3]]

 [[46 13  4]
  [46 14  5]
  [46 15  6]]

 [[47 16  7]
  [47 17  8]
  [47 18  9]]]
Şekli: (3, 3, 3)
A[1:3, 0:2, :] dilimi:
[[[46 13  4]
  [46 14  5]]

 [[47 16  7]
  [47 17  8]]]
"""