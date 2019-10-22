# coding:iso-8859-9 Türkçe
# p_30409c.py: Kolon ve sütun matrislerinin sayısal çarpımda birlikte yayılmaları örneği.

import numpy as np

A = np.array ([10, 20, 30])
A1 = A[:, np.newaxis]
A2 = np.array ([[10, 20, 30], ] * 3).transpose()

B = np.array ([1, 2, 3])
B1 = np.array ([[1, 2, 3],]*3)

# A[:, np.newaxis] * B = A2 * B1 gibi oldu...
Z1 = A[:, np.newaxis] * B
Z2 = A2 * B1

print ("A 1x3 dizisi: ", A, "\n\nA[:,np.newaxis] 3x1 kolon matrisi:\n", A1, "\n\nA2=np.array([[10,20,30],]*3).transpose() 3x3 matrisi:\n", A2, sep="")
print ("\nB 1x3 dizisi: ", B, "\n\nB1=np.array([[1,2,3],]*3) 3x3 matrisi:\n", B1, sep="")
print ("\nA[:,np.newaxis]*B otomatik yayılım uyumlu bire-bir çarpımlı 3x3 matrisi:\n", (A[:, np.newaxis] * B), sep="")
print ("\n(A[:,np.newaxis]*B) ile (A2*B1=np.array([[10, 20, 30],]*3).transpose() * np.array([[1,2,3],]*3)) eşit mi?", np.array_equal (Z1, Z2) )



"""Çıktı:
>python p_30409c.py
A 1x3 dizisi: [10 20 30]

A[:,np.newaxis] 3x1 kolon matrisi:
[[10]
 [20]
 [30]]

A2=np.array([[10,20,30],]*3).transpose() 3x3 matrisi:
[[10 10 10]
 [20 20 20]
 [30 30 30]]

B 1x3 dizisi: [1 2 3]

B1=np.array([[1,2,3],]*3) 3x3 matrisi:
[[1 2 3]
 [1 2 3]
 [1 2 3]]

A[:,np.newaxis]*B otomatik yayılım uyumlu bire-bir çarpımlı 3x3 matrisi:
[[10 20 30]
 [20 40 60]
 [30 60 90]]

(A[:,np.newaxis]*B) ile (A2*B1=np.array([[10, 20, 30],]*3).transpose() * np.array([[1,2,3],]*3)) eşit mi? True
"""