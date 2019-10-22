# coding:iso-8859-9 Türkçe
# p_30502.py: 3 boyutlu (3,4,2) şekilli matrisin varsayılı, C-satır, F-sütun, hafızada A ve K düzende sökülmesi örneği. 

import numpy as np

A = np.array ([
    [[ 0,  1],   [ 2,  3],   [ 4,  5],    [ 6,  7]],
    [[ 8,  9],   [10, 11], [12, 13], [14, 15]],
    [[16, 17], [18, 19], [20, 21], [22, 23]] ]) # A(3,4,2))

print ("A(3,4,2) 3 boyutlu matris:\n", A, "==>", A.shape, sep="")

sökükA = A.ravel()
print ("\nSökülen A(24,) 0 boyutlu dizi: ", sökükA, "==>", sökükA.shape, sep="")
print ("C++ satır düzenli sökükA:", A.ravel (order="C") ) # Varsayılı...
print ("Fortran sütun düzenli sökükA:", A.ravel (order="F") )
print ("A hafızada F değilse C düzenli sökükA:", A.ravel (order="A") )
print ("K hafızadaki C/F düzenli sökükA:", A.ravel (order="K") )



"""Çıktı:
>python p_30502.py
A(3,4,2) 3 boyutlu matris:
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

Sökülen A(24,) 0 boyutlu dizi: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 1516 17 18 19 20 21 22 23]==>(24,)
C++ satır düzenli sökükA: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
Fortran sütun düzenli sökükA: [ 0  8 16  2 10 18  4 12 20  6 14 22  1  9 17  3 11 19  5 13 21  7 15 23]
A hafızada F değilse C düzenli sökükA: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
K hafızadaki C/F düzenli sökükA: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
"""