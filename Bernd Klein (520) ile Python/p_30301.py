# coding:iso-8859-9 Türkçe
# p_30301.py: Python liste'nin varsayılı kayannoktalı ve dtype tamsayılı numpy.array(liste)'si örneği.

import numpy as np

i16 = np.dtype (np.int16) # dtype: data type object/veri tipi nesnesi...
print ("np.dtype(np.int16):", i16)

liste = [
    [3.4, 8.7, 9.9], 
    [1.1, -7.8, -0.7],
    [4.1, 12.3, 4.8] ]
print ("Liste:", liste)

A = np.array (liste)
print ("\nVarsayılı veri tipli numpy disizi A:\n", A, sep="")

A = np.array (liste, dtype=i16)
print ("\nint16 veri tipli numpy dizisi A:\n", A, sep="")



"""Çıktı:
>python p_30301.py
np.dtype(np.int16): int16
Liste: [[3.4, 8.7, 9.9], [1.1, -7.8, -0.7], [4.1, 12.3, 4.8]]

Varsayılı veri tipli numpy dizisi A:
[[ 3.4  8.7  9.9]
 [ 1.1 -7.8 -0.7]
 [ 4.1 12.3  4.8]]

int16 veri tipli numpy disizi A:
[[ 3  8  9]
 [ 1 -7  0]
 [ 4 12  4]]
"""