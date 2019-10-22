# coding:iso-8859-9 Türkçe
# p_30409b.py: Sayısal matris işlemlerinde kısa satır veya kolonun yayılması örneği.

import numpy as np

A = np.array ([
    [11, 12, 13],
    [21, 22, 23],
    [31, 32, 33] ])

B = np.array ([1, 2, 3])
B1 = B[:, np.newaxis]
B2 = np.array ([[1, 2, 3], ] * 3)
B3 = B2.transpose()

Z = A * B[:, np.newaxis]

print ("A:\n", A, "\n\nB: ", B, "\n\nB1=B[:,np.newaxis]:\n", B1, "\n\nB2=np.array([[1,2,3],]*3):\n", B2, "\n\nB3=B2.transpose():\n", B3, sep="")
print ("\n'A*B[:,np.newaxis]' otomatik B kolonvari=B3 yayılım uyumlu bire-bir çarpım:\n", (A * B[:, np.newaxis]), sep="")



"""Çıktı:
>python p_30409b.py
A:
[[11 12 13]
 [21 22 23]
 [31 32 33]]

B: [1 2 3]

B1=B[:,np.newaxis]:
[[1]
 [2]
 [3]]

B2=np.array([[1,2,3],]*3):
[[1 2 3]
 [1 2 3]
 [1 2 3]]

B3=B2.transpose():
[[1 1 1]
 [2 2 2]
 [3 3 3]]

'A*B[:,np.newaxis]' otomatik B kolonvari=B3 yayılım uyumlu bire-bir çarpım:
[[11 12 13]
 [42 44 46]
 [93 96 99]]
"""