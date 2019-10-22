# coding:iso-8859-9 T�rk�e
# p_31514.py: Grafik taban�n� �zgaralama �rne�i.

import numpy as np
import matplotlib.pyplot as mp
from p_315 import Renk

�ekil = mp.figure()
def f (t): return np.exp (-t) * np.cos (2 * np.pi * t)
def g (t): return np.sin(t) * np.cos (1 / (t + 1))
t = np.arange (0.0, 7.0, 0.1)

alt�ekil1 = mp.subplot (211)
alt�ekil1.grid (color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
alt�ekil1.set_title ("f(t)=exp(-t)*cos(2*pi*t)")
alt�ekil1.plot (t, f (t), 'r--.')

alt�ekil2 = mp.subplot (212)
alt�ekil2.grid (color='r', alpha=0.9, linestyle='solid', linewidth=0.3)
alt�ekil2.set_title ("f(t)=sin(t)*cos(1/(t+1))")
alt�ekil2.plot (t, g (t), 'k-.')

mp.tight_layout()
mp.show()
#------------------------------------------------------------------------------------------------------

mp.style.use ("dark_background")
�ekil = mp.figure()
def f (t): return np.exp (-t) * np.cos (2 * np.pi * t)
def g (t): return np.sin(t) * np.cos (1 / (t + 1))
t = np.arange (0.0, 7.0, 0.1)

alt�ekil1 = mp.subplot (211)
alt�ekil1.grid (color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
alt�ekil1.set_title ("f(t)=exp(-t)*cos(2*pi*t)")
alt�ekil1.plot (t, f (t), 'r--.')

alt�ekil2 = mp.subplot (212)
alt�ekil2.grid (color='r', alpha=0.9, linestyle='solid', linewidth=0.3)
alt�ekil2.set_title ("f(t)=sin(t)*cos(1/(t+1))")
alt�ekil2.plot (t, g (t), 'w-.')

mp.tight_layout()
mp.show()
#------------------------------------------------------------------------------------------------------

�ekil = mp.figure()
�ekil.set_facecolor (Renk.renk())
def f (t): return np.exp (-t) * np.cos (2 * np.pi * t)
def g (t): return np.sin(t) * np.cos (1 / (t + 1))
t = np.arange (0.0, 7.0, 0.1)

alt�ekil1 = mp.subplot (211)
alt�ekil1.grid (color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
alt�ekil1.set_title ("f(t)=exp(-t)*cos(2*pi*t)")
alt�ekil1.set_facecolor (Renk.renk())
alt�ekil1.plot (t, f (t), 'r--.')

alt�ekil2 = mp.subplot (212)
alt�ekil2.grid (color='r', alpha=0.9, linestyle='solid', linewidth=0.3)
alt�ekil2.set_title ("f(t)=sin(t)*cos(1/(t+1))")
alt�ekil2.set_facecolor (Renk.renk())
alt�ekil2.plot (t, g (t), 'k-.')

mp.tight_layout()
mp.show()

#�ekil.savefig ("p_31514.pdf", dpi=200)
# Saklama formatlar�: PNG, JPG, EPS, SVG, PGF ve PDF olabilir...