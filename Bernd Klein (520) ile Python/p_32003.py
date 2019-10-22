# coding:iso-8859-9 T�rk�e
# p_32003.py: S�zl�kten pandas serisi yapma ve fonksiyon uygulama �rne�i.

import pandas as pd
import numpy as np

s�zl�k = {"Elma":20, "Portakal":33, "Kiraz":52, "Armut":10, "�eftali":19, "Muz":12}
seri = pd.Series (s�zl�k)

print ("S�zl�kten direk yarat�lan pandas serisi:\n", seri, sep="")
print ("\nnp.sin(seri):\n", np.sin (seri), sep="")
print ("\nseri.apply(np.sin):\n", seri.apply (np.sin), sep="")
print ("\nStoklar 50 alt� ise 10 art�r:\n", seri.apply (lambda x: x if x > 50 else x + 10), sep="")



"""��kt�:
>python p_32003.py
S�zl�kten direk yarat�lan pandas serisi:
Elma        20
Portakal    33
Kiraz       52
Armut       10
�eftali     19
Muz         12
dtype: int64

np.sin(seri):
Elma        0.912945
Portakal    0.999912
Kiraz       0.986628
Armut      -0.544021
�eftali     0.149877
Muz        -0.536573
dtype: float64

seri.apply(np.sin):
Elma        0.912945
Portakal    0.999912
Kiraz       0.986628
Armut      -0.544021
�eftali     0.149877
Muz        -0.536573
dtype: float64

Stoklar 50 alt� ise 10 art�r:
Elma        30
Portakal    43
Kiraz       52
Armut       20
�eftali     29
Muz         22
dtype: int64
"""