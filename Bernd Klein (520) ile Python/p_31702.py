# coding:iso-8859-9 T�rk�e
# p_31702.py: Izgara kesi�im e�hatlar renk dolgulu haritalama grafi�i �rne�i.

import numpy as np
import matplotlib.pyplot as mp
from p_315 import Renk

x = np.linspace (-3.0, 3.0, 100)
y = np.linspace (-3.0, 3.0, 100)
X, Y = np.meshgrid (x, y)
Z = np.sqrt (X**2 + Y**2)

mp.style.use ("dark_background")
kontur = mp.contourf (X, Y, Z)
mp.colorbar (kontur)
mp.clabel (kontur, inline=False, fontsize=10, colors="w")
mp.title ('Renkdolgulu E�hatlar Zifir Grafi�i')
mp.xlabel ('x (sm)')
mp.ylabel ('y (sm)')

mp.show()
#---------------------------------------------------------------------------------------------------------

�ekil = mp.figure()
�ekil.set_facecolor (Renk.renk())

e�hatlar = �ekil.add_subplot()
e�hatlar.set_facecolor (Renk.renk())
kontur = mp.contourf (X, Y, Z)
mp.colorbar (kontur)
mp.clabel (kontur, inline=False, fontsize=10, colors="w")
mp.title ('Varsay�l� Renkdolgulu E�hatlar Grafi�i', color=Renk.renk())
mp.xlabel ('x (sm)', color=Renk.renk())
mp.ylabel ('y (sm)', color=Renk.renk())

mp.show()
#---------------------------------------------------------------------------------------------------------

�ekil = mp.figure()
�ekil.set_facecolor (Renk.renk())

e�hatlar = �ekil.add_subplot()
e�hatlar.set_facecolor (Renk.renk())

kontur = mp.contourf (X, Y, Z)
renkler = ("0.15", Renk.renk(), Renk.renk(), "Cyan", "Brown", "Tan", Renk.renk())
mp.clabel (kontur, colors = renkler, fmt = '%2.1f', fontsize=12)
kontur = mp.contourf (X, Y, Z, colors=renkler)
mp.colorbar (kontur)
mp.title ('Se�ili Renkdolgulu E�hatlar Grafi�i', color=Renk.renk())
mp.xlabel ('x (sm)', color=Renk.renk())
mp.ylabel ('y (sm)', color=Renk.renk())

mp.show()
