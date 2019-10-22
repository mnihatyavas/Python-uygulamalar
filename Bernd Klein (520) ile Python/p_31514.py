# coding:iso-8859-9 Türkçe
# p_31514.py: Grafik tabanını ızgaralama örneği.

import numpy as np
import matplotlib.pyplot as mp
from p_315 import Renk

şekil = mp.figure()
def f (t): return np.exp (-t) * np.cos (2 * np.pi * t)
def g (t): return np.sin(t) * np.cos (1 / (t + 1))
t = np.arange (0.0, 7.0, 0.1)

altşekil1 = mp.subplot (211)
altşekil1.grid (color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
altşekil1.set_title ("f(t)=exp(-t)*cos(2*pi*t)")
altşekil1.plot (t, f (t), 'r--.')

altşekil2 = mp.subplot (212)
altşekil2.grid (color='r', alpha=0.9, linestyle='solid', linewidth=0.3)
altşekil2.set_title ("f(t)=sin(t)*cos(1/(t+1))")
altşekil2.plot (t, g (t), 'k-.')

mp.tight_layout()
mp.show()
#------------------------------------------------------------------------------------------------------

mp.style.use ("dark_background")
şekil = mp.figure()
def f (t): return np.exp (-t) * np.cos (2 * np.pi * t)
def g (t): return np.sin(t) * np.cos (1 / (t + 1))
t = np.arange (0.0, 7.0, 0.1)

altşekil1 = mp.subplot (211)
altşekil1.grid (color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
altşekil1.set_title ("f(t)=exp(-t)*cos(2*pi*t)")
altşekil1.plot (t, f (t), 'r--.')

altşekil2 = mp.subplot (212)
altşekil2.grid (color='r', alpha=0.9, linestyle='solid', linewidth=0.3)
altşekil2.set_title ("f(t)=sin(t)*cos(1/(t+1))")
altşekil2.plot (t, g (t), 'w-.')

mp.tight_layout()
mp.show()
#------------------------------------------------------------------------------------------------------

şekil = mp.figure()
şekil.set_facecolor (Renk.renk())
def f (t): return np.exp (-t) * np.cos (2 * np.pi * t)
def g (t): return np.sin(t) * np.cos (1 / (t + 1))
t = np.arange (0.0, 7.0, 0.1)

altşekil1 = mp.subplot (211)
altşekil1.grid (color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
altşekil1.set_title ("f(t)=exp(-t)*cos(2*pi*t)")
altşekil1.set_facecolor (Renk.renk())
altşekil1.plot (t, f (t), 'r--.')

altşekil2 = mp.subplot (212)
altşekil2.grid (color='r', alpha=0.9, linestyle='solid', linewidth=0.3)
altşekil2.set_title ("f(t)=sin(t)*cos(1/(t+1))")
altşekil2.set_facecolor (Renk.renk())
altşekil2.plot (t, g (t), 'k-.')

mp.tight_layout()
mp.show()

#şekil.savefig ("p_31514.pdf", dpi=200)
# Saklama formatları: PNG, JPG, EPS, SVG, PGF ve PDF olabilir...