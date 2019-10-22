# coding:iso-8859-9 Türkçe
# p_30507.py: Bir matrisi numpy.tile(M,(s,k)) ile s-satır ve k-kolonlu şekle tuğlalama örneği.

import numpy as np

a = np.array ([1.23])
a1 = np.tile (a, 5) # veya (5,): sütunu çoğaltır!..

print ("a dizisi: ", a, "==>", a.shape,
    "\n\nnp.tile(a,5) tuğlalama dizisi:\n", a1, "==>", a1.shape, sep="")
print ("-"*30)
#--------------------------------------------------------------------------------------------------

X = np.array ([1, 2, 3])
X1 = np.tile (X, (3, 1) )

print ("\nX dizisi: ", X, "==>", X.shape,
    "\n\nnp.tile(X,(3,1)) tuğlalama matrisi:\n", X1, "==>", X1.shape, sep="")
print ("-"*30)
#--------------------------------------------------------------------------------------------------

X2 = np.array ([
    [1, 2],
    [3, 4] ])

X3 = np.tile (X2, (3,4) )

print ("\nX2 matrisi:\n", X2, "==>", X2.shape,
    "\n\nnp.tile(X2,(3,4)) tuğlalama matrisi:\n", X3, "==>", X2.shape, "*(3,4)=", X3.shape, sep="")
print ("-"*30)
#--------------------------------------------------------------------------------------------------

x = np.array ([
    [1, 2],
    [3, 4] ])

x1 = np.tile (x, 2)
x2 = np.tile (x, (2, 1))
x3 = np.tile (x, (3, 2))

print ("\nx matrisi:\n", x, "==>", x.shape,
    "\n\nnp.tile(x,2) sütun tuğlalama matrisi:\n", x1, "==>", x1.shape,
    "\n\nnp.tile(x,(2,1)) satır tuğlalama matrisi:\n", x2, "==>", x2.shape,
    "\n\nnp.tile(x,(3,2)) satır ve sütun tuğlalama matrisi:\n", x3, x3.shape, sep="")



"""Çıktı:
>python p_30507.py
a dizisi: [1.23]==>(1,)

np.tile(a,5) tuğlalama dizisi:
[1.23 1.23 1.23 1.23 1.23]==>(5,)
------------------------------

X dizisi: [1 2 3]==>(3,)

np.tile(X,(3,1)) tuğlalama matrisi:
[[1 2 3]
 [1 2 3]
 [1 2 3]]==>(3, 3)
------------------------------

X2 matrisi:
[[1 2]
 [3 4]]==>(2, 2)

np.tile(X2,(3,4)) tuğlalama matrisi:
[[1 2 1 2 1 2 1 2]
 [3 4 3 4 3 4 3 4]
 [1 2 1 2 1 2 1 2]
 [3 4 3 4 3 4 3 4]
 [1 2 1 2 1 2 1 2]
 [3 4 3 4 3 4 3 4]]==>(2, 2)*(3,4)=(6, 8)
------------------------------

x matrisi:
[[1 2]
 [3 4]]==>(2, 2)

np.tile(x,2) sütun tuğlalama matrisi:
[[1 2 1 2]
 [3 4 3 4]]==>(2, 4)

np.tile(x,(2,1)) satır tuğlalama matrisi:
[[1 2]
 [3 4]
 [1 2]
 [3 4]]==>(4, 2)

np.tile(x,(3,2)) satır ve sütun tuğlalama matrisi:
[[1 2 1 2]
 [3 4 3 4]
 [1 2 1 2]
 [3 4 3 4]
 [1 2 1 2]
 [3 4 3 4]](6, 4)
"""