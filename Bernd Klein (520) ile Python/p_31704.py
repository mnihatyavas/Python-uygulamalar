# coding:iso-8859-9 T�rk�e
# p_31704.py: Sevgi sembol� kalbin topografik grafi�i �rne�i.

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
#mp.axis ('equal') # on/a��k, off/kapal�...
mp.title ('Sevgi Sembol� Kalp Grafi�i')

mp.show()
#---------------------------------------------------------------------------------------------------

y, x = np.ogrid [-1:2:100j, -1:1:100j]

�ekil = mp.figure()
�ekil.set_facecolor (Renk.renk())

alt�ekil = �ekil.add_subplot()
alt�ekil.set_facecolor (Renk.renk())

mp.contour (
    x.ravel(),
    y.ravel(),
    x**2 + (y - ((x**2)**(1.0 / 3)))**2,
    [1],
    colors=Renk.renk() )

mp.axis ('equal')
mp.title ('Sevgi Sembol� Kalp Grafi�i', color=Renk.renk())

mp.show()
