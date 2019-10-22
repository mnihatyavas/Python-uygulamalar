# coding:iso-8859-9 T�rk�e
# p_30501.py: �ok boyutlu matrisin flatten() ile C/F/A d�zenli tek boyutluya �evrilmesi �rne�i.

import numpy as np

A = np.array ([
    [[ 0,  1],   [ 2,  3],   [ 4,  5],    [ 6,  7]],
    [[ 8,  9],   [10, 11], [12, 13], [14, 15]],
    [[16, 17], [18, 19], [20, 21], [22, 23]] ]) # A(3,4,2))

print ("A(3,4,2) 3 boyutlu matris:\n", A, "==>", A.shape, sep="")

yayg�nA = A.flatten()
print ("\nYayg�nla�t�r�lan A(24,) 0 boyutlu dizi: ", yayg�nA, "==>", yayg�nA.shape, sep="")
print ("C++ sat�r d�zenli yayg�nA:", A.flatten (order="C") ) # Varsay�l�...
print ("Fortran s�tun d�zenli yayg�nA:", A.flatten (order="F") )
print ("A �nceki C/F d�zenli yayg�nA:", A.flatten (order="A") )


"""��kt�:
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

Yayg�nla�t�r�lan A(24,) 0 boyutlu dizi: [ 0  1  2  3  4  5  6  7  8  9 10 11 1213 14 15 16 17 18 19 20 21 22 23]==>(24,)
C++ sat�r d�zenli yayg�nA: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
Fortran s�tun d�zenli yayg�nA: [ 0  8 16  2 10 18  4 12 20  6 14 22  1  9 17  311 19  5 13 21  7 15 23]
A �nceki C/F d�zenli yayg�nA: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
"""