# coding:iso-8859-9 Türkçe
# p_32003.py: Sözlükten pandas serisi yapma ve fonksiyon uygulama örneği.

import pandas as pd
import numpy as np

sözlük = {"Elma":20, "Portakal":33, "Kiraz":52, "Armut":10, "Şeftali":19, "Muz":12}
seri = pd.Series (sözlük)

print ("Sözlükten direk yaratılan pandas serisi:\n", seri, sep="")
print ("\nnp.sin(seri):\n", np.sin (seri), sep="")
print ("\nseri.apply(np.sin):\n", seri.apply (np.sin), sep="")
print ("\nStoklar 50 altı ise 10 artır:\n", seri.apply (lambda x: x if x > 50 else x + 10), sep="")



"""Çıktı:
>python p_32003.py
Sözlükten direk yaratılan pandas serisi:
Elma        20
Portakal    33
Kiraz       52
Armut       10
Şeftali     19
Muz         12
dtype: int64

np.sin(seri):
Elma        0.912945
Portakal    0.999912
Kiraz       0.986628
Armut      -0.544021
Şeftali     0.149877
Muz        -0.536573
dtype: float64

seri.apply(np.sin):
Elma        0.912945
Portakal    0.999912
Kiraz       0.986628
Armut      -0.544021
Şeftali     0.149877
Muz        -0.536573
dtype: float64

Stoklar 50 altı ise 10 artır:
Elma        30
Portakal    43
Kiraz       52
Armut       20
Şeftali     29
Muz         22
dtype: int64
"""