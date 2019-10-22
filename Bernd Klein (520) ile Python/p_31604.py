# coding:iso-8859-9 T�rk�e
# p_31604.py: �ubuk grafiklerle y�llara da��n�k turist say�s� �rne�i.

import numpy as np
import matplotlib.pyplot as mp
from p_315 import Renk

y�llar = ("2012", "2013", "2014", "2015", "2016", "2017", "2018")
Y = (1241, 50927, 162242, 222093, 296665 / 8 * 12, 65782, 65782 * 4.55)
X = np.arange (len (Y))
�ubukEni = 0.95

�ekil = mp.figure()
�ekil.set_facecolor (Renk.renk())
mp.title ("Y�llara G�re Ku�adas�n� Ziyaret Eden Yabanc� Turist Say�s�", color=Renk.renk())

alt�ekil1 = �ekil.add_subplot (111)
alt�ekil1.set_facecolor (Renk.renk())
mp.xticks (X, y�llar) # alt�ekil.set_xticks y�llar� yans�tmad�...
alt�ekil1.set_xlabel ("Y�llar", color=Renk.renk())
alt�ekil1.set_ylabel ("Ku�adas�'na Turist Say�s�", color=Renk.renk())
alt�ekil1.set_xlim (-0.5, 6.5)
�ubuklar = alt�ekil1.bar (X, Y, �ubukEni,  color=Renk.renk())
for �ubuk in �ubuklar: �ubuk.set_color (Renk.renk())

mp.tight_layout()
mp.show()