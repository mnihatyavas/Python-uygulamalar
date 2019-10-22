# coding:iso-8859-9 Türkçe
# p_31502.py: Şekle farklı fonksiyonlu 4 altşekil ekleme örneği.

import numpy as np
from numpy import e, pi, sin, exp, cos
import matplotlib.pyplot as mp

def f (t): return exp (-t) * cos (2 * pi * t)
def ft (t): return -2 * pi * exp (-t) * sin (2 * pi * t) - e**(-t) * cos (2 * pi * t) # Türev...
def g (t): return sin (t) * cos (1 / (t) )

mp.style.use ("dark_background")
şekil = mp.figure (figsize=(6, 4)) # (en, boy)...

t = np.arange (-5.0, 1.0, 0.1)
altşekil1 = şekil.add_subplot (221)
altşekil1.set_facecolor ("Gold")
altşekil1.set_title ('y=f(t)=e(-t)*cos(2*pi*t)')
altşekil1.plot (t, f (t) )

altşekil2 = şekil.add_subplot (222)
altşekil2.set_facecolor ("Blue")
altşekil2.set_title ('y=df(t)=-2*pi*exp(-t)*sin(2*pi*t)\n-e**(-t)*cos(2*pi*t) türev')
altşekil2.plot (t, ft (t), color="y")

t = np.arange (-3.0, 2.0, 0.02)
altşekil3 = şekil.add_subplot (223)
altşekil3.set_facecolor ("Pink")
altşekil3.set_title ('y=g(t)=sin(t)*cos(1/(t+0.1))')
altşekil3.plot (t, g (t), color="g")

t = np.arange (-0.2, 0.2, 0.001)
altşekil4 = şekil.add_subplot (224)
altşekil4.set_facecolor ("Green")
altşekil4.set_title ("y=g(t) detay zoom'u")
altşekil4.set_xticks ([-0.2, -0.1, 0, 0.1, 0.2])
altşekil4.set_yticks ([-0.15, -0.1, 0, 0.1, 0.15])
altşekil4.plot (t, g (t), color="r")

mp.tight_layout()
mp.show()
