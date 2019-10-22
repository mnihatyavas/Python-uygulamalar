# coding:iso-8859-9 T�rk�e
# p_31502.py: �ekle farkl� fonksiyonlu 4 alt�ekil ekleme �rne�i.

import numpy as np
from numpy import e, pi, sin, exp, cos
import matplotlib.pyplot as mp

def f (t): return exp (-t) * cos (2 * pi * t)
def ft (t): return -2 * pi * exp (-t) * sin (2 * pi * t) - e**(-t) * cos (2 * pi * t) # T�rev...
def g (t): return sin (t) * cos (1 / (t) )

mp.style.use ("dark_background")
�ekil = mp.figure (figsize=(6, 4)) # (en, boy)...

t = np.arange (-5.0, 1.0, 0.1)
alt�ekil1 = �ekil.add_subplot (221)
alt�ekil1.set_facecolor ("Gold")
alt�ekil1.set_title ('y=f(t)=e(-t)*cos(2*pi*t)')
alt�ekil1.plot (t, f (t) )

alt�ekil2 = �ekil.add_subplot (222)
alt�ekil2.set_facecolor ("Blue")
alt�ekil2.set_title ('y=df(t)=-2*pi*exp(-t)*sin(2*pi*t)\n-e**(-t)*cos(2*pi*t) t�rev')
alt�ekil2.plot (t, ft (t), color="y")

t = np.arange (-3.0, 2.0, 0.02)
alt�ekil3 = �ekil.add_subplot (223)
alt�ekil3.set_facecolor ("Pink")
alt�ekil3.set_title ('y=g(t)=sin(t)*cos(1/(t+0.1))')
alt�ekil3.plot (t, g (t), color="g")

t = np.arange (-0.2, 0.2, 0.001)
alt�ekil4 = �ekil.add_subplot (224)
alt�ekil4.set_facecolor ("Green")
alt�ekil4.set_title ("y=g(t) detay zoom'u")
alt�ekil4.set_xticks ([-0.2, -0.1, 0, 0.1, 0.2])
alt�ekil4.set_yticks ([-0.15, -0.1, 0, 0.1, 0.15])
alt�ekil4.plot (t, g (t), color="r")

mp.tight_layout()
mp.show()
