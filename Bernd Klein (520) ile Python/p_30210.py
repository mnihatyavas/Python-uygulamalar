# coding:iso-8859-9 Türkçe
# p_30210.py: numpy.ones/birler, zeros/sıfırlar, _like/gibi ve empty/kayannoktalısıfırlar örneği.

import numpy as np

K = np.ones ((2, 3)) # 2x3 boyutlu 1'ler tüplesinden numpy dizisi...
print ("Varsayılı kayannoktalı 1'ler dizisi np.ones((2,3)):\n", K, sep="")
T = np.ones ((3, 4), dtype=int)
print ("\nnp.ones((3,4),dtype=int) ile tamsayılı 1'ler dizisi:\n", T, sep="")

S = np.zeros ((2, 4))
print ("\nnp.zeros((2,4)) ile 0'lar dizisi:\n", S, sep="")

X = np.array ([2, 5, 18, 14, 4])
print ("\nnp.array([2, 5, 18, 14, 4]) dizisi:", X)
B = np.ones_like (X)
print ("np.ones_like(X) ile aynı dizinin 1'lisi:", B)
Z = np.zeros_like (X)
print ("np.zeros_like (X) ile aynı dizinin 0'lısı:", Z)

E = np.empty ((2, 4))
print ("\nVarsayılı kayannoktalı boş'lar dizisi np.empty((2,4)):\n", E, sep="")



"""Çıktı:
>python p_30210.py
Varsayılı kayannoktalı 1'ler dizisi np.ones((2,3)):
[[1. 1. 1.]
 [1. 1. 1.]]

np.ones((3,4),dtype=int) ile tamsayılı 1'ler dizisi:
[[1 1 1 1]
 [1 1 1 1]
 [1 1 1 1]]

np.zeros((2,4)) ile 0'lar dizisi:
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]]

np.array([2, 5, 18, 14, 4]) dizisi: [ 2  5 18 14  4]
np.ones_like(X) ile aynı dizinin 1'lisi: [1 1 1 1 1]
np.zeros_like (X) ile aynı dizinin 0'lısı: [0 0 0 0 0]

Varsayılı kayannoktalı boş'lar dizisi np.empty((2,4)):
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]]
"""