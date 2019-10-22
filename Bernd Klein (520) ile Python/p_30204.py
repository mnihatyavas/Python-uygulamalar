# coding:iso-8859-9 T�rk�e
# p_30204.py: numpy.array ile 0-1-2-3 boyut ve ()-(5,)-(1,5)-(3,4)-(6,3)-(3,2,4) �ekil �rne�i.

import numpy as np

N = np.array (-2.8)
print ("Dizi:\n", N, sep="")
print ("Boyutu:", N.ndim)
print ("�ekli:", np.shape (N) )

T1 = np.array ([3.4, 0, 9.9, 1, -2.8])
print ("\nDizi:\n", T1, sep="")
print ("Boyutu:", T1.ndim)
print ("�ekli:", np.shape (T1) )

T2 = np.array ([[3.4, 0, 9.9, 1, -2.8]])
print ("\nDizi:\n", T2, sep="")
print ("Boyutu:", T2.ndim)
print ("�ekli:", np.shape (T2) )

A = np.array ([
    [3.4, 0, 9.9, 1],
    [1.1, -7.8, -0.7, 7.5],
    [4.1, 12, 4.8, -2] ])
print ("\nDizi:\n", A, sep="")
print ("Boyutu:", A.ndim)
print ("�ekli:", np.shape (A) )

B = np.array ([
    [67, 63, 87],
    [77, 69, 59],
    [85, 87, 99],
    [79, 72, 71],
    [63, 89, 93],
    [68, 92, 78] ])
print ("\nDizi:\n", B, sep="")
print ("Boyutu:", B.ndim)
print ("�ekli:", np.shape (B) )

C = np.array ([
    [[111, 112, 113,114], [121, 122, 123, 124]],
    [[211, 212, 213, 214], [221, 222, 223, 224]],
    [[311, 312, 313, 314], [321, 322, 323, 324]] ])
print ("\nDizi:\n", C, sep="")
print ("Boyutu:", C.ndim)
print ("�ekli:", np.shape (C) )
print ("�ekli:", C.shape) # ayn� sonu�...



"""��kt�:
>python p_30204.py
Dizi:
-2.8
Boyutu: 0
�ekli: ()

Dizi:
[ 3.4  0.   9.9  1.  -2.8]
Boyutu: 1
�ekli: (5,)

Dizi:
[[ 3.4  0.   9.9  1.  -2.8]]
Boyutu: 2
�ekli: (1, 5)

Dizi:
[[ 3.4  0.   9.9  1. ]
 [ 1.1 -7.8 -0.7  7.5]
 [ 4.1 12.   4.8 -2. ]]
Boyutu: 2
�ekli: (3, 4)

Dizi:
[[67 63 87]
 [77 69 59]
 [85 87 99]
 [79 72 71]
 [63 89 93]
 [68 92 78]]
Boyutu: 2
�ekli: (6, 3)

Dizi:
[[[111 112 113 114]
  [121 122 123 124]]

 [[211 212 213 214]
  [221 222 223 224]]

 [[311 312 313 314]
  [321 322 323 324]]]
Boyutu: 3
�ekli: (3, 2, 4)
�ekli: (3, 2, 4)
"""