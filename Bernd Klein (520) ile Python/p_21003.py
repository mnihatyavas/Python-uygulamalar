# coding:iso-8859-9 Türkçe
# p_21003.py: Rakamlarla ve grafiklerle 2 ayrı polinom, toplamları ve farkları örneği.

from p_21002 import Polinom
import numpy as np
import matplotlib.pyplot as mp
            
p1 = Polinom (4, 0, -4, 3, 0) # 4x^4 - 4x^2 + 3x
p2 = Polinom (-0.8, 2.3, 0.5, 1, 0.2) # -0.8x^4 + 2.3x^3 + 0.5x^2 + x + 0.2

print ("Polinom p1 ve p2:\n", p1, " ve ", p2, sep="")
print ("x=>p1(x): ", end="")
for i in range (-3, 5): print (i, "=>", p1 (i), sep="", end=", ")
print ("\nx=>p2(x): ", end="")
for i in range (-3, 5): print (i, "=>", p2 (i), sep="", end=", ")

pT = p1 + p2 # Toplam katsayıları tüplesi...
pF = p1 - p2 # Fark katsayıları tüplesi...

print ("\n\nPolinom toplamı ve polinom farkı:\n", pT, " ve ", pF, sep="")
print ("x=>pT(x): ", end="")
for i in range (-3, 5): print (i, "=>", pT (i), sep="", end=", ")
print ("\nx=>pF(x): ", end="")
for i in range (-3, 5): print (i, "=>", pF (i), sep="", end=", ")

X = np.linspace (-3, 4, 100, endpoint=True)
F1 = p1 (X)
F2 = p2 (X)
Ft = pT (X)
Ff = pF (X)

mp.style.use ("dark_background")
mp.plot (X, F1, label="F1")
mp.plot (X, F2, label="F2")
mp.plot (X, Ft, label="Ftoplam")
mp.plot (X, Ff, label="Ffark")
mp.legend()
mp.show()



"""Çıktı:
>python p_21003.py
Polinom p1 ve p2:
Polinom (4, 0, -4, 3, 0) ve Polinom (-0.8, 2.3, 0.5, 1, 0.2)
x=>p1(x): -3=>279, -2=>42, -1=>-3, 0=>0, 1=>3, 2=>54, 3=>297, 4=>972,
x=>p2(x): -3=>-125.19999999999999, -2=>-31.0, -1=>-3.3999999999999995, 0=>0.2, 1=>3.2, 2=>9.799999999999997, 3=>5.0, 4=>-45.400000000000034,

Polinom toplamı ve polinom farkı:
Polinom (0.2, 4, -3.5, 2.3, 3.2) ve Polinom (-0.2, 2, -4.5, -2.3, 4.8)
x=>pT(x): -3=>-126.99999999999999, -2=>-44.199999999999996, -1=>-6.3999999999999995, 0=>3.2, 1=>6.2, 2=>29.0, 3=>102.8, 4=>263.6,
x=>pF(x): -3=>-99.0, -2=>-27.8, -1=>0.39999999999999963, 0=>4.8, 1=>-0.2, 2=>-5.000000000000001, 3=>-4.800000000000001, 4=>0.3999999999999915,
"""