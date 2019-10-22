# coding:iso-8859-9 T�rk�e
# p_30503.py: S�f�r boyutlu (24,) �ekilli matrisi 3 boyutlu (3,4,2) �ekilli varsay�l� C-d�zene �evirme �rne�i.

import numpy as np

X = np.array (range(24) )
Y = X.reshape ((3,4,2)) # order:C/F/A, varsay�l�:C

print ("Yarat�lan X(24,) 0 boyutlu dizi: ", X, "==>", X.shape, sep="")
print ("\nC++ sat�r d�zenli Y(3,4,2) �ekillenen X:\n", Y, "==>", Y.shape, sep="" )



"""��kt�:
>python p_30503.py
Yarat�lan X(24,) 0 boyutlu dizi: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]==>(24,)

C++ sat�r d�zenli Y(3,4,2) �ekillenen X:
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