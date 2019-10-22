# coding:iso-8859-9 T�rk�e
# p_21004.py: 2 farkl� polinom ve t�revlerinin rakamsal ve grafiksel sonu�lar� �rne�i.

from p_21002 import Polinom
import numpy as np
import matplotlib.pyplot as mp

p1 = Polinom (4, 0, -4, 3, 0) # 4x^4 - 4x^2 + 3x
p2 = Polinom (-0.8, 2.3, 0.5, 1, 0.2) # -0.8x^4 + 2.3x^3 + 0.5x^2 + x + 0.2
pT�1 = p1.t�rev()
pT�2 = p2.t�rev()

print ("Polinom p1 ve p2:\n", p1, " ve ", p2, sep="")
print ("x=>p1(x): ", end="")
for i in range (-3, 5): print (i, "=>", p1 (i), sep="", end=", ")
print ("\nx=>p2(x): ", end="")
for i in range (-3, 5): print (i, "=>", p2 (i), sep="", end=", ")

print ("\n\nHer iki polinom t�revleri :\n", pT�1, " ve ", pT�2, sep="")
print ("x=>pT�1(x): ", end="")
for i in range (-3, 5): print (i, "=>", pT�1 (i), sep="", end=", ")
print ("\nx=>pT�2(x): ", end="")
for i in range (-3, 5): print (i, "=>", pT�2 (i), sep="", end=", ")

X = np.linspace (-10, 10, 100, endpoint=True)
F1 = p1(X)
F2 = p2(X)
Ft�1 = pT�1 (X)
Ft�2 = pT�2 (X)
mp.style.use ("dark_background")
mp.plot (X, F1, label="F1")
mp.plot (X, F2, label="F2")
mp.plot (X, Ft�1, label="Ft�rev1")
mp.plot (X, Ft�2, label="Ft�rev2")
mp.legend()
mp.show()



"""��kt�:
>python p_21004.py
Polinom p1 ve p2:
Polinom (4, 0, -4, 3, 0) ve Polinom (-0.8, 2.3, 0.5, 1, 0.2)
x=>p1(x): -3=>279, -2=>42, -1=>-3, 0=>0, 1=>3, 2=>54, 3=>297, 4=>972,
x=>p2(x): -3=>-125.19999999999999, -2=>-31.0, -1=>-3.3999999999999995, 0=>0.2, 1=>3.2, 2=>9.799999999999997, 3=>5.0, 4=>-45.400000000000034,

Her iki polinom t�revleri :
Polinom (16, 0, -8, 3) ve Polinom (-3.2, 6.8999999999999995, 1.0, 1)
x=>pT�1(x): -3=>-405, -2=>-109, -1=>-5, 0=>3, 1=>11, 2=>115, 3=>411, 4=>995,
x=>pT�2(x): -3=>146.5, -2=>52.2, -1=>10.1, 0=>1.0, 1=>5.699999999999998, 2=>4.9999999999999964, 3=>-20.30000000000001, 4=>-89.40000000000002,
"""