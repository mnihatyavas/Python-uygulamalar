# coding:iso-8859-9 T�rk�e
# p_21001.py: x^4-4x^2+3x polinomun (-3,4) aras� 100 noktalamal� grafik resmi �rne�i.

def p (x): return x**4 - 4*x**2 + 3*x

print ("p(x) = x^4 - 4x^2 + 3x polinomun 4 farkl� x de�eriyle sonucu:\n(x, p(x)) =")
for x in [-1, 0, 2, 3.4]: print (x, p (x) )


import numpy as np
import matplotlib.pyplot as mp

mp.style.use ("dark_background")
X = np.linspace (-3, 4, 100, endpoint=True) # x:(-3->4), 100:[-3->4] aras� grafik noktalama say�s�...
F = p (X)
mp.plot (X, F)
mp.show()



"""��kt�:
>python p_21001.py
p(x) = x^4 - 4x^2 + 3x polinomun 4 farkl� x de�eriyle sonucu:
(x, p(x)) =
-1 -6
0 0
2 6
3.4 97.59359999999998
"""