# coding:iso-8859-9 Türkçe
# p_31704.py: Sevgi sembolü kalbin topografik grafiği örneği.

import numpy as np
import matplotlib.pyplot as mp
from p_315 import Renk

x, y = np.ogrid [-1:1:100j, -1:1.56:100j]
mp.style.use ("dark_background")
mp.contour (
    x.ravel(),
    y.ravel(),
    x**2 + (y - ((x**2)**(1.0 / 3)))**2,
    [1],
    colors='red')
#mp.axis ('equal') # on/açık, off/kapalı...
mp.title ('Sevgi Sembolü Kalp Grafiği')

mp.show()
#---------------------------------------------------------------------------------------------------

y, x = np.ogrid [-1:2:100j, -1:1:100j]

şekil = mp.figure()
şekil.set_facecolor (Renk.renk())

altşekil = şekil.add_subplot()
altşekil.set_facecolor (Renk.renk())

mp.contour (
    x.ravel(),
    y.ravel(),
    x**2 + (y - ((x**2)**(1.0 / 3)))**2,
    [1],
    colors=Renk.renk() )

mp.axis ('equal')
mp.title ('Sevgi Sembolü Kalp Grafiği', color=Renk.renk())

mp.show()
