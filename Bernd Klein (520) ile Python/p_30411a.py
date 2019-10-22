# coding:iso-8859-9 Türkçe
# p_30411a.py: Sayısal çarpımda (1,3,4) matrisin otomatik (3,3,4) matrise yayılması örneği.

import numpy as np

A = np.array ([
    [[3, 4, 7, 2], [5, 0, -1, 1] , [2, 1, 5, -2]],
    [[1, 0, -1, 1], [8, 2, 4, 0], [5, 2, 1, 1]],
    [[2, 1, 3, 0], [1, 9, 4, 2], [5, -2, 4, -2]] ]) # A(3,3,4) 3 boyutlu matris..

B = np.array ([ [[3, 4, 7, 1], [1, 0, -1, 2], [1, 2, 3, 0]] ]) # B(1,3,4) matrisi...
B1 = np.array ([
     [[3, 4, 7, 1], [1, 0, -1, 2], [1, 2, 3, 0]],
     [[3, 4, 7, 1], [1, 0, -1, 2], [1, 2, 3, 0]],
     [[3, 4, 7, 1], [1, 0, -1, 2], [1, 2, 3, 0]] ]) # B1(3,3,4) matrisi...

print ("A(3,3,4) matrisi:\n", A, "==>", A.shape, "\n\nB(1,3,4) matrisi:\n", B, "==>", B.shape, sep="")

print ("\n(A*B) bire-bir çarpım yayılımla A'nın her 3 satırdaki 3 dizinin içerik 4 elemanı için de tekrarlı geçerlidir:\n", (A * B), sep="")

print ("\nnp.array_equal(A*B,A*B1):?", np.array_equal (A*B, A*B1) )



"""Çıktı:
>python p_30411a.py
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

B(1,3,4) matrisi:
[[[ 3  4  7  1]
  [ 1  0 -1  2]
  [ 1  2  3  0]]]==>(1, 3, 4)

(A*B) bire-bir çarpım yayılımla A'nın her 3 satırdaki 3 dizinin içerik 4 elemanı için de tekrarlı geçerlidir:
[[[ 9 16 49  2]
  [ 5  0  1  2]
  [ 2  2 15  0]]

 [[ 3  0 -7  1]
  [ 8  0 -4  0]
  [ 5  4  3  0]]

 [[ 6  4 21  0]
  [ 1  0 -4  4]
  [ 5 -4 12  0]]]

np.array_equal (A*B, A*B1):? True
"""