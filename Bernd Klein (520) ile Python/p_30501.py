# coding:iso-8859-9 Türkçe
# p_30501.py: Çok boyutlu matrisin flatten() ile C/F/A düzenli tek boyutluya çevrilmesi örneği.

import numpy as np

A = np.array ([
    [[ 0,  1],   [ 2,  3],   [ 4,  5],    [ 6,  7]],
    [[ 8,  9],   [10, 11], [12, 13], [14, 15]],
    [[16, 17], [18, 19], [20, 21], [22, 23]] ]) # A(3,4,2))

print ("A(3,4,2) 3 boyutlu matris:\n", A, "==>", A.shape, sep="")

yaygınA = A.flatten()
print ("\nYaygınlaştırılan A(24,) 0 boyutlu dizi: ", yaygınA, "==>", yaygınA.shape, sep="")
print ("C++ satır düzenli yaygınA:", A.flatten (order="C") ) # Varsayılı...
print ("Fortran sütun düzenli yaygınA:", A.flatten (order="F") )
print ("A önceki C/F düzenli yaygınA:", A.flatten (order="A") )


"""Çıktı:
>python p_30501.py
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

Yaygınlaştırılan A(24,) 0 boyutlu dizi: [ 0  1  2  3  4  5  6  7  8  9 10 11 1213 14 15 16 17 18 19 20 21 22 23]==>(24,)
C++ satır düzenli yaygınA: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
Fortran sütun düzenli yaygınA: [ 0  8 16  2 10 18  4 12 20  6 14 22  1  9 17  311 19  5 13 21  7 15 23]
A önceki C/F düzenli yaygınA: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
"""