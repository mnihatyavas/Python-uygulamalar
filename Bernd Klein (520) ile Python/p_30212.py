# coding:iso-8859-9 Türkçe
# p_30212.py: numpy.identity ve numpy.eye ile kayannoktalı veya tamsayı birler matrisi örneği.

import numpy as np

print ("np.identity(4) birler matrisi:\n", np.identity (4), sep="") # dtype=float (varsayılı)...
print ("\nnp.identity(3,dtype=int):\n", np.identity (3, dtype=int), sep="")
print ("-"*40)
#-----------------------------------------------------------------------------------------------

print ("\nnp.eye(5,8) 5x8 birler matrisi:\n", np.eye (5, 8), sep="") # dtype=float (varsayılı)...
print ("\nnp.eye(5,8,k=1,dtype=int) 5x8 birler matrisi:\n", np.eye (5, 8, k=1, dtype=int), sep="")
print ("\nnp.eye(5,8,k=3,dtype=int) 5x8 birler matrisi:\n", np.eye (5, 8, k=3, dtype=int), sep="")
print ("\nnp.eye(5,8,k=-1,dtype=int) 5x8 birler matrisi:\n", np.eye (5, 8, k=-1, dtype=int), sep="")
print ("\nnp.eye(5,8,k=-4,dtype=int) 5x8 birler matrisi:\n", np.eye (5, 8, k=-4, dtype=int), sep="")



"""Çıktı:
>python p_30212.py
np.identity(4) birler matrisi:
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]

np.identity(3,dtype=int):
[[1 0 0]
 [0 1 0]
 [0 0 1]]
----------------------------------------

np.eye(5,8,dtype=int) 5x8 birler matrisi:
[[1. 0. 0. 0. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0. 0. 0. 0.]
 [0. 0. 1. 0. 0. 0. 0. 0.]
 [0. 0. 0. 1. 0. 0. 0. 0.]
 [0. 0. 0. 0. 1. 0. 0. 0.]]

np.eye(5,8,k=1,dtype=int) 5x8 birler matrisi:
[[0 1 0 0 0 0 0 0]
 [0 0 1 0 0 0 0 0]
 [0 0 0 1 0 0 0 0]
 [0 0 0 0 1 0 0 0]
 [0 0 0 0 0 1 0 0]]

np.eye(5,8,k=3,dtype=int) 5x8 birler matrisi:
[[0 0 0 1 0 0 0 0]
 [0 0 0 0 1 0 0 0]
 [0 0 0 0 0 1 0 0]
 [0 0 0 0 0 0 1 0]
 [0 0 0 0 0 0 0 1]]

np.eye(5,8,k=-1,dtype=int) 5x8 birler matrisi:
[[0 0 0 0 0 0 0 0]
 [1 0 0 0 0 0 0 0]
 [0 1 0 0 0 0 0 0]
 [0 0 1 0 0 0 0 0]
 [0 0 0 1 0 0 0 0]]

np.eye(5,8,k=-4,dtype=int) 5x8 birler matrisi:
[[0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [1 0 0 0 0 0 0 0]]
"""