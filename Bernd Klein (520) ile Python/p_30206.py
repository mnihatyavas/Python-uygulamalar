# coding:iso-8859-9 Türkçe
# p_30206.py: numpy.array ile tek boyutlu D[0]-D[-1] ve iki boyutlu D[0][0]-D[-1][-1] dizi ilk ve son elemanları örneği.

import numpy as np

F = np.array ([1, 1, 2, 3, 5, 8, 13, 21])
print ("Dizi: ", F, "\nİlk elemanı: ", F[0], "\nSon elemanı: ", F[-1], "\nŞekli: ", F.shape, sep="")

A = np.array ([
    [3.4, 8.7, 9.9],
    [1.1, -7.8, -0.7],
    [4.1, 12.3, 4.8] ])
print ("\nDizi:\n", A, "\nİlk elemanı: ", A[0][0], "\nSon elemanı: ", A[-1][-1], "\nŞekli: ", A.shape, sep="")



"""Çıktı:
>python p_30206.py
Dizi: [ 1  1  2  3  5  8 13 21]
İlk elemanı: 1
Son elemanı: 21
Şekli: (8,)

Dizi:
[[ 3.4  8.7  9.9]
 [ 1.1 -7.8 -0.7]
 [ 4.1 12.3  4.8]]
İlk elemanı: 3.4
Son elemanı: 4.8
Şekli: (3, 3)
"""