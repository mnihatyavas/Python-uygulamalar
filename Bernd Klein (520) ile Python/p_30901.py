# coding:iso-8859-9 Türkçe
# p_30901.py: Numpy dizi elemanlarını Boolean True/False'e çevirme örneği.

import numpy as np

A = np.array ([4, 7, 3, 4, 2, 8])
print ("A dizisi: ", A, "\nTek-tek elemanları == 4? ", A == 4, sep="")
print ("Tek-tek elemanları < 5?", (A < 5) )
print ("-"*50)
#---------------------------------------------------------------------------------------------

B = np.array ([
    [42, 56, 89, 65],
    [99, 88, 42, 12],
    [55, 42, 17, 18] ])

print ("\nB dizisi:\n", B, "\n\nTek-tek elemanları >= 42?\n", B >= 42, sep="")
print ("-"*50)
#---------------------------------------------------------------------------------------------

A = np.array ([
[12, 13, 14, 12, 16, 14, 11, 10,  9],
[11, 14, 12, 15, 15, 16, 10, 12, 11],
[10, 12, 12, 15, 14, 16, 10, 12, 12],
[ 9, 11, 16, 15, 14, 16, 15, 12, 10],
[12, 11, 16, 14, 10, 12, 16, 12, 13],
[10, 15, 16, 14, 14, 14, 16, 15, 12],
[13, 17, 14, 10, 14, 11, 14, 15, 10],
[10, 16, 12, 14, 11, 12, 14, 18, 11],
[10, 19, 12, 14, 11, 12, 14, 18, 10],
[14, 22, 17, 19, 16, 17, 18, 17, 13],
[10, 16, 12, 14, 11, 12, 14, 18, 11],
[10, 16, 12, 14, 11, 12, 14, 18, 11],
[10, 19, 12, 14, 11, 12, 14, 18, 10],
[14, 22, 12, 14, 11, 12, 14, 17, 13],
[10, 16, 12, 14, 11, 12, 14, 18, 11] ])

B = A < 15

print ("\nA dizisi:\n", A, "\n\nTek-tek elemanları < 15?\n", B, sep="")

C = B.astype (np.int) # veya (np.float)...

print ("\nTüm True=1, False=0 yaparsak, ortaya 0'larla gizli A harfi imajı çıkar:\n", C)



"""Çıktı:
>python p_30901.py
A dizisi: [4 7 3 4 2 8]
Tek-tek elemanları == 4? [ True False False  True False False]
Tek-tek elemanları < 5? [ True False  True  True  True False]
--------------------------------------------------

B dizisi:
[[42 56 89 65]
 [99 88 42 12]
 [55 42 17 18]]

Tek-tek elemanları >= 42?
[[ True  True  True  True]
 [ True  True  True False]
 [ True  True False False]]
--------------------------------------------------

A dizisi:
[[12 13 14 12 16 14 11 10  9]
 [11 14 12 15 15 16 10 12 11]
 [10 12 12 15 14 16 10 12 12]
 [ 9 11 16 15 14 16 15 12 10]
 [12 11 16 14 10 12 16 12 13]
 [10 15 16 14 14 14 16 15 12]
 [13 17 14 10 14 11 14 15 10]
 [10 16 12 14 11 12 14 18 11]
 [10 19 12 14 11 12 14 18 10]
 [14 22 17 19 16 17 18 17 13]
 [10 16 12 14 11 12 14 18 11]
 [10 16 12 14 11 12 14 18 11]
 [10 19 12 14 11 12 14 18 10]
 [14 22 12 14 11 12 14 17 13]
 [10 16 12 14 11 12 14 18 11]]

Tek-tek elemanları < 15?
[[ True  True  True  True False  True  True  True  True]
 [ True  True  True False False False  True  True  True]
 [ True  True  True False  True False  True  True  True]
 [ True  True False False  True False False  True  True]
 [ True  True False  True  True  True False  True  True]
 [ True False False  True  True  True False False  True]
 [ True False  True  True  True  True  True False  True]
 [ True False  True  True  True  True  True False  True]
 [ True False  True  True  True  True  True False  True]
 [ True False False False False False False False  True]
 [ True False  True  True  True  True  True False  True]
 [ True False  True  True  True  True  True False  True]
 [ True False  True  True  True  True  True False  True]
 [ True False  True  True  True  True  True False  True]
 [ True False  True  True  True  True  True False  True]]

Tüm True=1, False=0 yaparsak, ortaya 0'larla gizli A harfi imajı çıkar:
 [[1 1 1 1 0 1 1 1 1]
 [1 1 1 0 0 0 1 1 1]
 [1 1 1 0 1 0 1 1 1]
 [1 1 0 0 1 0 0 1 1]
 [1 1 0 1 1 1 0 1 1]
 [1 0 0 1 1 1 0 0 1]
 [1 0 1 1 1 1 1 0 1]
 [1 0 1 1 1 1 1 0 1]
 [1 0 1 1 1 1 1 0 1]
 [1 0 0 0 0 0 0 0 1]
 [1 0 1 1 1 1 1 0 1]
 [1 0 1 1 1 1 1 0 1]
 [1 0 1 1 1 1 1 0 1]
 [1 0 1 1 1 1 1 0 1]
 [1 0 1 1 1 1 1 0 1]]
"""