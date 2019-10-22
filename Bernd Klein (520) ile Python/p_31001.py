# coding:iso-8859-9 T�rk�e
# p_31001.py: Numpy matris t�m aritmetik i�lemleri �rne�i.

import numpy as np

x = np.array ([1, 5, 2])
y = np.array ([7, 4, 1]) # x ve y'nin eleman say�lar� ayn� olmal�d�r...

print ("x dizisi: ", x, "\ny dizisi: ", y, sep="")
print ("\n(x + y) =", (x + y))
print ("(x - y) =", (x - y))
print ("(x * y) =", (x * y))
print ("(x / y) =", (x / y))
print ("(x ** y) =", (x ** y))
print ("(x % y) =", (x % y))



"""��kt�:
>python p_31001.py
x dizisi: [1 5 2]
y dizisi: [7 4 1]

(x + y) = [8 9 3]
(x - y) = [-6  1  1]
(x * y) = [ 7 20  2]
(x / y) = [0.14285714 1.25       2.        ]
(x ** y) = [  1 625   2]
(x % y) = [1 1 0]
"""