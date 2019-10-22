# coding:iso-8859-9 Türkçe
# p_30407.py: Numpy.dot(a,b) ve numpy.mat(a)*numpy.mat(b) matris çarpımlarının aynılığı örneği.

import numpy as np

A = np.array ([
    [1, 2, 3],
    [2, 2, 2],
    [3, 3, 3] ])

B = np.array ([
    [3, 2, 1],
    [1, 2, 3],
    [-1, -2, -3] ])

print ("A ile B matrisleri ve şekilleri:\n", A, " ==>", A.shape, "\n", B, " ==>", B.shape, sep="")
print ("\n'A*B' elemanlarının bire-bir çarpımı sonucu:\n", (A * B), sep="")
print ("\n'np.dot(A,B)' matris çarpımı sonucu:\n", np.dot (A, B), sep="")
print ("\n'np.mat(A)*np.mat(B)' matris çarpımı sonucu:\n", (np.mat (A) * np.mat (B)), sep="")



"""Çıktı:
>python p_30407.py
A ile B matrisleri ve şekilleri:
[[1 2 3]
 [2 2 2]
 [3 3 3]] ==>(3, 3)
[[ 3  2  1]
 [ 1  2  3]
 [-1 -2 -3]] ==>(3, 3)

'A*B' elemanlarının bire-bir çarpımı sonucu:
[[ 3  4  3]
 [ 2  4  6]
 [-3 -6 -9]]

'np.dot(A,B)' matris çarpımı sonucu:
[[ 2  0 -2]
 [ 6  4  2]
 [ 9  6  3]]

'np.mat(A)*np.mat(B)' matris çarpımı sonucu:
[[ 2  0 -2]
 [ 6  4  2]
 [ 9  6  3]]
"""