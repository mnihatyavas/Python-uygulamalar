# coding:iso-8859-9 Türkçe
# p_30207.py: numpy.array ile 2 boyutlu dizi [satır,kolon]'ların tümü [:], ters tümü [::-1], öncesi [:s] ve sonrası [k:] örneği.

import numpy as np

S = np.array ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print ("Dizi S: ", S, "\nŞekli: ", S.shape, "\nS[2:5] dilimi: ", S[2:5],
    "\nBaştan S[:4] dilimi: ", S[:4], "\nSondan S[6:] dilimi: ", S[6:],
    "\nTüm S[:] dilimi: ", S[:], "\nTersten tüm S[::-1] dilimi: ", S[::-1], sep="")

A = np.array([
[11, 12, 13, 14, 15],
[21, 22, 23, 24, 25],
[31, 32, 33, 34, 35],
[41, 42, 43, 44, 45],
[51, 52, 53, 54, 55]])
print ("\nDizi A:\n", A, "\nŞekli: ", A.shape, "\nSağ üstten A[:3, 2:] dilimi:\n", A[:3, 2:],
    "\nOrtadan A[1:4, 1:4] dilimi:\n", A[1:4, 1:4], "\nAlttan soniki A[3:, :] dilimi:\n", A[3:, :],
    "\nSon kolon A[:, 4:] dilimi:\n", A[:, 4:], sep="")



"""Çıktı:
>python p_30207.py
Dizi S: [0 1 2 3 4 5 6 7 8 9]
Şekli: (10,)
S[2:5] dilimi: [2 3 4]
Baştan S[:4] dilimi: [0 1 2 3]
Sondan S[6:] dilimi: [6 7 8 9]
Tüm S[:] dilimi: [0 1 2 3 4 5 6 7 8 9]
Tersten tüm S[::-1] dilimi: [9 8 7 6 5 4 3 2 1 0]

Dizi A:
[[11 12 13 14 15]
 [21 22 23 24 25]
 [31 32 33 34 35]
 [41 42 43 44 45]
 [51 52 53 54 55]]
Şekli: (5, 5)
Sağ üstten A[:3, 2:] dilimi:
[[13 14 15]
 [23 24 25]
 [33 34 35]]
Ortadan A[1:4, 1:4] dilimi:
[[22 23 24]
 [32 33 34]
 [42 43 44]]
Alttan üst A[3:, :] dilimi:
[[41 42 43 44 45]
 [51 52 53 54 55]]
Son kolon A[:, 4:] dilimi:
[[15]
 [25]
 [35]
 [45]
 [55]]
"""