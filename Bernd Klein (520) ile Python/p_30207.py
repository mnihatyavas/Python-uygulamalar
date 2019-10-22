# coding:iso-8859-9 T�rk�e
# p_30207.py: numpy.array ile 2 boyutlu dizi [sat�r,kolon]'lar�n t�m� [:], ters t�m� [::-1], �ncesi [:s] ve sonras� [k:] �rne�i.

import numpy as np

S = np.array ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print ("Dizi S: ", S, "\n�ekli: ", S.shape, "\nS[2:5] dilimi: ", S[2:5],
    "\nBa�tan S[:4] dilimi: ", S[:4], "\nSondan S[6:] dilimi: ", S[6:],
    "\nT�m S[:] dilimi: ", S[:], "\nTersten t�m S[::-1] dilimi: ", S[::-1], sep="")

A = np.array([
[11, 12, 13, 14, 15],
[21, 22, 23, 24, 25],
[31, 32, 33, 34, 35],
[41, 42, 43, 44, 45],
[51, 52, 53, 54, 55]])
print ("\nDizi A:\n", A, "\n�ekli: ", A.shape, "\nSa� �stten A[:3, 2:] dilimi:\n", A[:3, 2:],
    "\nOrtadan A[1:4, 1:4] dilimi:\n", A[1:4, 1:4], "\nAlttan soniki A[3:, :] dilimi:\n", A[3:, :],
    "\nSon kolon A[:, 4:] dilimi:\n", A[:, 4:], sep="")



"""��kt�:
>python p_30207.py
Dizi S: [0 1 2 3 4 5 6 7 8 9]
�ekli: (10,)
S[2:5] dilimi: [2 3 4]
Ba�tan S[:4] dilimi: [0 1 2 3]
Sondan S[6:] dilimi: [6 7 8 9]
T�m S[:] dilimi: [0 1 2 3 4 5 6 7 8 9]
Tersten t�m S[::-1] dilimi: [9 8 7 6 5 4 3 2 1 0]

Dizi A:
[[11 12 13 14 15]
 [21 22 23 24 25]
 [31 32 33 34 35]
 [41 42 43 44 45]
 [51 52 53 54 55]]
�ekli: (5, 5)
Sa� �stten A[:3, 2:] dilimi:
[[13 14 15]
 [23 24 25]
 [33 34 35]]
Ortadan A[1:4, 1:4] dilimi:
[[22 23 24]
 [32 33 34]
 [42 43 44]]
Alttan �st A[3:, :] dilimi:
[[41 42 43 44 45]
 [51 52 53 54 55]]
Son kolon A[:, 4:] dilimi:
[[15]
 [25]
 [35]
 [45]
 [55]]
"""