# coding:iso-8859-9 T�rk�e
# p_30206.py: numpy.array ile tek boyutlu D[0]-D[-1] ve iki boyutlu D[0][0]-D[-1][-1] dizi ilk ve son elemanlar� �rne�i.

import numpy as np

F = np.array ([1, 1, 2, 3, 5, 8, 13, 21])
print ("Dizi: ", F, "\n�lk eleman�: ", F[0], "\nSon eleman�: ", F[-1], "\n�ekli: ", F.shape, sep="")

A = np.array ([
    [3.4, 8.7, 9.9],
    [1.1, -7.8, -0.7],
    [4.1, 12.3, 4.8] ])
print ("\nDizi:\n", A, "\n�lk eleman�: ", A[0][0], "\nSon eleman�: ", A[-1][-1], "\n�ekli: ", A.shape, sep="")



"""��kt�:
>python p_30206.py
Dizi: [ 1  1  2  3  5  8 13 21]
�lk eleman�: 1
Son eleman�: 21
�ekli: (8,)

Dizi:
[[ 3.4  8.7  9.9]
 [ 1.1 -7.8 -0.7]
 [ 4.1 12.3  4.8]]
�lk eleman�: 3.4
Son eleman�: 4.8
�ekli: (3, 3)
"""