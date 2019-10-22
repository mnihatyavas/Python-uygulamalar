# coding:iso-8859-9 T�rk�e
# p_30502.py: 3 boyutlu (3,4,2) �ekilli matrisin varsay�l�, C-sat�r, F-s�tun, haf�zada A ve K d�zende s�k�lmesi �rne�i. 

import numpy as np

A = np.array ([
    [[ 0,  1],   [ 2,  3],   [ 4,  5],    [ 6,  7]],
    [[ 8,  9],   [10, 11], [12, 13], [14, 15]],
    [[16, 17], [18, 19], [20, 21], [22, 23]] ]) # A(3,4,2))

print ("A(3,4,2) 3 boyutlu matris:\n", A, "==>", A.shape, sep="")

s�k�kA = A.ravel()
print ("\nS�k�len A(24,) 0 boyutlu dizi: ", s�k�kA, "==>", s�k�kA.shape, sep="")
print ("C++ sat�r d�zenli s�k�kA:", A.ravel (order="C") ) # Varsay�l�...
print ("Fortran s�tun d�zenli s�k�kA:", A.ravel (order="F") )
print ("A haf�zada F de�ilse C d�zenli s�k�kA:", A.ravel (order="A") )
print ("K haf�zadaki C/F d�zenli s�k�kA:", A.ravel (order="K") )



"""��kt�:
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

S�k�len A(24,) 0 boyutlu dizi: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 1516 17 18 19 20 21 22 23]==>(24,)
C++ sat�r d�zenli s�k�kA: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
Fortran s�tun d�zenli s�k�kA: [ 0  8 16  2 10 18  4 12 20  6 14 22  1  9 17  3 11 19  5 13 21  7 15 23]
A haf�zada F de�ilse C d�zenli s�k�kA: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
K haf�zadaki C/F d�zenli s�k�kA: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
"""