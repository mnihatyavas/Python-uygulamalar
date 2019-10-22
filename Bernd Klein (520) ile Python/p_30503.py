# coding:iso-8859-9 Türkçe
# p_30503.py: Sıfır boyutlu (24,) şekilli matrisi 3 boyutlu (3,4,2) şekilli varsayılı C-düzene çevirme örneği.

import numpy as np

X = np.array (range(24) )
Y = X.reshape ((3,4,2)) # order:C/F/A, varsayılı:C

print ("Yaratılan X(24,) 0 boyutlu dizi: ", X, "==>", X.shape, sep="")
print ("\nC++ satır düzenli Y(3,4,2) şekillenen X:\n", Y, "==>", Y.shape, sep="" )



"""Çıktı:
>python p_30503.py
Yaratılan X(24,) 0 boyutlu dizi: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]==>(24,)

C++ satır düzenli Y(3,4,2) şekillenen X:
[[[ 0  1]
  [ 2  3]
  [ 4  5]
  [ 6  7]]

 [[ 8  9]
  [10 11]
  [12 13]
  [14 15]]

 [[16 17]
  [18 19]
  [20 21]
  [22 23]]]==>(3, 4, 2)
"""