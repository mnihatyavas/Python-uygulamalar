# coding:iso-8859-9 Türkçe
# p_31703.py: Seviyeli renk dolgulu eşhatlı haritalama grafiği örneği.

import numpy as np
import matplotlib.pyplot as mp
from p_315 import Renk

x = np.linspace (-3.0, 3.0, 100)
y = np.linspace (-3.0, 3.0, 100)
X, Y = np.meshgrid (x, y)
Z = np.sqrt (X ** 2 + Y ** 2 )
renkler = [Renk.renk() for _ in range (len (Z)) ]
seviyeler = [0.0, 0.2, 0.5, 0.9, 1.4, 2, 2.7, 3.5, 4.4]

mp.style.use ("dark_background")
mp.figure()
kontur = mp.contour (X, Y, Z, seviyeler, colors=renkler)
mp.clabel (kontur, colors = "k", fmt = '%2.1f', fontsize=12)
dolguluKontur = mp.contourf (X, Y, Z, seviyeler, colors=renkler)
mp.colorbar (dolguluKontur)
mp.title ('Seviyeli Listeler Zifirzeminli Grafik', color=Renk.renk())
mp.xlabel ('x (sm)', color=Renk.renk())
mp.ylabel ('y (sm)', color=Renk.renk())

mp.show()
#---------------------------------------------------------------------------------------------------------

şekil = mp.figure()
şekil.set_facecolor (Renk.renk())
altşekil = şekil.add_subplot()
altşekil.set_facecolor (Renk.renk())

kontur = mp.contour (X, Y, Z, seviyeler, colors=renkler)
mp.clabel (kontur, colors = "black", fmt = '%2.1f', fontsize=12)
dolguluKontur = mp.contourf (X, Y, Z, seviyeler, colors=renkler)
mp.colorbar (dolguluKontur)
mp.title ('Seviyeli Listeler Renkzeminli Grafik', color=Renk.renk())
mp.xlabel ('x (sm)', color=Renk.renk())
mp.ylabel ('y (sm)', color=Renk.renk())

mp.show()
