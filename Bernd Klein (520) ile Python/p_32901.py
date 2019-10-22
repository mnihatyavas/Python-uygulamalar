#coding:iso-8859-9 Türkçe
# p_32901.py: Numpy ile doğrusal birleştirme örneği.

import numpy as np

x = np.array ([ [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0] ])
y = ( [-3.65, 1.55, 3.14, 2.72])
doğrusalBirleştirme = np.linalg.solve (x, y)
print ("x Numpy dizisi:\n", x, x.shape,
    "\n\ny listesi: ", y,
    "\n\nDoğrusal birleştirme dizisi: ", doğrusalBirleştirme, doğrusalBirleştirme.shape, sep="")
print ("-"*60)
#--------------------------------------------------------------------------------------------------------

x = np.array ([ [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0] ])
db = np.linalg.solve (x, y)
print ("\nx Numpy dizisi:\n", x, x.shape,
    "\n\ny listesi: ", y,
    "\n\nDoğrusal birleştirme dizisi: ", db, db.shape, sep="")



"""Çıktı:
>python p_32901.py
x Numpy dizisi:
[[0 0 0 1]
 [0 0 1 0]
 [0 1 0 0]
 [1 0 0 0]](4, 4)

y listesi: [-3.65, 1.55, 3.14, 2.72]

Doğrusal birleştirme dizisi: [ 2.72  3.14  1.55 -3.65](4,)
------------------------------------------------------------

x Numpy dizisi:
[[0 1 1 1]
 [1 0 1 1]
 [1 1 0 1]
 [1 1 1 0]](4, 4)

y listesi: [-3.65, 1.55, 3.14, 2.72]

Doğrusal birleştirme dizisi: [ 4.90333333 -0.29666667 -1.88666667 -1.46666667](4,)
"""