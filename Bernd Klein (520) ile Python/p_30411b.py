# coding:iso-8859-9 Türkçe
# p_30411b.py: Sayısal çarpımda (3,4) matrisin (3,3,4) matrise yayılması örneği.

import numpy as np

A = np.array ([
    [[3, 4, 7, 2], [5, 0, -1, 1] , [2, 1, 5, -2]],
    [[1, 0, -1, 1], [8, 2, 4, 0], [5, 2, 1, 1]],
    [[2, 1, 3, 0], [1, 9, 4, 2], [5, -2, 4, -2]] ]) # A(3,3,4) 3 boyutlu matris..

B = np.array ([1, 2, 3]); print ("B diziden matrise:\n", B.shape, sep="") # B(3,)
B = B[np.newaxis, :]; print (B.shape) # B(1, 3)
B = np.concatenate ((B, B, B, B)).transpose(); print (B.shape) # B(3, 3)

print ("\nA(3,3,4) matrisi:\n", A, "==>", A.shape, "\n\nB(3,4) matrisi:\n", B, "==>", B.shape, sep="")
print ("\n(A*B) bire-bir çarpım yayılımla A'nın her 3 satırdaki 3 dizinin içerik 4 elemanı için de tekrarlı geçerlidir:\n", (A * B), sep="")



"""Çıktı:
>python p_30411b.py
B diziden matrise:
(3,)
(1, 3)
(3, 4)

A(3,3,4) matrisi:
[[[ 3  4  7  2]
  [ 5  0 -1  1]
  [ 2  1  5 -2]]

 [[ 1  0 -1  1]
  [ 8  2  4  0]
  [ 5  2  1  1]]

 [[ 2  1  3  0]
  [ 1  9  4  2]
  [ 5 -2  4 -2]]]==>(3, 3, 4)

B(3,4) matrisi:
[[1 1 1 1]
 [2 2 2 2]
 [3 3 3 3]]==>(3, 4)

(A*B) bire-bir çarpım yayılımla A'nın her 3 satırdaki 3 dizinin içerik 4 elemanı
 için de tekrarlı geçerlidir:
[[[ 3  4  7  2]
  [10  0 -2  2]
  [ 6  3 15 -6]]

 [[ 1  0 -1  1]
  [16  4  8  0]
  [15  6  3  3]]

 [[ 2  1  3  0]
  [ 2 18  8  4]
  [15 -6 12 -6]]]
"""