# coding:iso-8859-9 T�rk�e
# p_30507.py: Bir matrisi numpy.tile(M,(s,k)) ile s-sat�r ve k-kolonlu �ekle tu�lalama �rne�i.

import numpy as np

a = np.array ([1.23])
a1 = np.tile (a, 5) # veya (5,): s�tunu �o�alt�r!..

print ("a dizisi: ", a, "==>", a.shape,
    "\n\nnp.tile(a,5) tu�lalama dizisi:\n", a1, "==>", a1.shape, sep="")
print ("-"*30)
#--------------------------------------------------------------------------------------------------

X = np.array ([1, 2, 3])
X1 = np.tile (X, (3, 1) )

print ("\nX dizisi: ", X, "==>", X.shape,
    "\n\nnp.tile(X,(3,1)) tu�lalama matrisi:\n", X1, "==>", X1.shape, sep="")
print ("-"*30)
#--------------------------------------------------------------------------------------------------

X2 = np.array ([
    [1, 2],
    [3, 4] ])

X3 = np.tile (X2, (3,4) )

print ("\nX2 matrisi:\n", X2, "==>", X2.shape,
    "\n\nnp.tile(X2,(3,4)) tu�lalama matrisi:\n", X3, "==>", X2.shape, "*(3,4)=", X3.shape, sep="")
print ("-"*30)
#--------------------------------------------------------------------------------------------------

x = np.array ([
    [1, 2],
    [3, 4] ])

x1 = np.tile (x, 2)
x2 = np.tile (x, (2, 1))
x3 = np.tile (x, (3, 2))

print ("\nx matrisi:\n", x, "==>", x.shape,
    "\n\nnp.tile(x,2) s�tun tu�lalama matrisi:\n", x1, "==>", x1.shape,
    "\n\nnp.tile(x,(2,1)) sat�r tu�lalama matrisi:\n", x2, "==>", x2.shape,
    "\n\nnp.tile(x,(3,2)) sat�r ve s�tun tu�lalama matrisi:\n", x3, x3.shape, sep="")



"""��kt�:
>python p_30507.py
a dizisi: [1.23]==>(1,)

np.tile(a,5) tu�lalama dizisi:
[1.23 1.23 1.23 1.23 1.23]==>(5,)
------------------------------

X dizisi: [1 2 3]==>(3,)

np.tile(X,(3,1)) tu�lalama matrisi:
[[1 2 3]
 [1 2 3]
 [1 2 3]]==>(3, 3)
------------------------------

X2 matrisi:
[[1 2]
 [3 4]]==>(2, 2)

np.tile(X2,(3,4)) tu�lalama matrisi:
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

np.tile(x,2) s�tun tu�lalama matrisi:
[[1 2 1 2]
 [3 4 3 4]]==>(2, 4)

np.tile(x,(2,1)) sat�r tu�lalama matrisi:
[[1 2]
 [3 4]
 [1 2]
 [3 4]]==>(4, 2)

np.tile(x,(3,2)) sat�r ve s�tun tu�lalama matrisi:
[[1 2 1 2]
 [3 4 3 4]
 [1 2 1 2]
 [3 4 3 4]
 [1 2 1 2]
 [3 4 3 4]](6, 4)
"""