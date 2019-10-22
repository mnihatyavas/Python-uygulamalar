# coding:iso-8859-9 Türkçe
# p_21001.py: x^4-4x^2+3x polinomun (-3,4) arası 100 noktalamalı grafik resmi örneği.

def p (x): return x**4 - 4*x**2 + 3*x

print ("p(x) = x^4 - 4x^2 + 3x polinomun 4 farklı x değeriyle sonucu:\n(x, p(x)) =")
for x in [-1, 0, 2, 3.4]: print (x, p (x) )


import numpy as np
import matplotlib.pyplot as mp

mp.style.use ("dark_background")
X = np.linspace (-3, 4, 100, endpoint=True) # x:(-3->4), 100:[-3->4] arası grafik noktalama sayısı...
F = p (X)
mp.plot (X, F)
mp.show()



"""Çıktı:
>python p_21001.py
p(x) = x^4 - 4x^2 + 3x polinomun 4 farklı x değeriyle sonucu:
(x, p(x)) =
-1 -6
0 0
2 6
3.4 97.59359999999998
"""