# coding:iso-8859-9 Türkçe
# p_31702.py: Izgara kesişim eşhatlar renk dolgulu haritalama grafiği örneği.

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
mp.title ('Renkdolgulu Eşhatlar Zifir Grafiği')
mp.xlabel ('x (sm)')
mp.ylabel ('y (sm)')

mp.show()
#---------------------------------------------------------------------------------------------------------

şekil = mp.figure()
şekil.set_facecolor (Renk.renk())

eşhatlar = şekil.add_subplot()
eşhatlar.set_facecolor (Renk.renk())
kontur = mp.contourf (X, Y, Z)
mp.colorbar (kontur)
mp.clabel (kontur, inline=False, fontsize=10, colors="w")
mp.title ('Varsayılı Renkdolgulu Eşhatlar Grafiği', color=Renk.renk())
mp.xlabel ('x (sm)', color=Renk.renk())
mp.ylabel ('y (sm)', color=Renk.renk())

mp.show()
#---------------------------------------------------------------------------------------------------------

şekil = mp.figure()
şekil.set_facecolor (Renk.renk())

eşhatlar = şekil.add_subplot()
eşhatlar.set_facecolor (Renk.renk())

kontur = mp.contourf (X, Y, Z)
renkler = ("0.15", Renk.renk(), Renk.renk(), "Cyan", "Brown", "Tan", Renk.renk())
mp.clabel (kontur, colors = renkler, fmt = '%2.1f', fontsize=12)
kontur = mp.contourf (X, Y, Z, colors=renkler)
mp.colorbar (kontur)
mp.title ('Seçili Renkdolgulu Eşhatlar Grafiği', color=Renk.renk())
mp.xlabel ('x (sm)', color=Renk.renk())
mp.ylabel ('y (sm)', color=Renk.renk())

mp.show()
