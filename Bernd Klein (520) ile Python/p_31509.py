# coding:iso-8859-9 T�rk�e
# p_31509.py: Eksenlerle �ekil ebatlar�n� de�i�tirme �rne�i.

import numpy as np
import matplotlib.pyplot as mp
from p_315 import Renk

mp.figure (figsize=(10, 4))
X = np.arange (0,20)
Y = np.random.randint (1, 20, size=20)
mp.plot (X, Y, "Green")
mp.show()
#-------------------------------------------------------------------------------------------------------

mp.style.use ("dark_background")
�ekil = mp.figure()
X = np.arange (0,20)
Y = np.random.randint (1, 20, size=20)

sol, alt, sa�, �st = 0.15, 0.15, 0.75, 0.75
eksenler = �ekil.add_axes ([sol, alt, sa�, �st])
eksenler.set_xlabel ('X=(Yatay Eksen)')
eksenler.set_ylabel ('Y=(Dikey Eksen)')
eksenler.set_title ('Geli�ig�zel 20 �ak��ma');

eksenler.plot (X, Y, 'r--o')
mp.show ()
#-------------------------------------------------------------------------------------------------------

�ekil = mp.figure()
�ekil.set_facecolor (Renk.renk())

sol, alt, sa�, �st = 0.1, 0.1, 0.8, 0.3
eksenler = �ekil.add_axes ([sol, alt, sa�, �st])
eksenler.set_xlabel ('X=(Yatay Eksen)')
eksenler.set_ylabel ('Y=(Dikey Eksen)')
eksenler.set_title ('Geli�ig�zel 20 �ak��ma');

eksenler.plot (X, Y, 'r--o')
mp.show ()
#-------------------------------------------------------------------------------------------------------

�ekil = mp.figure()
�ekil.set_facecolor (Renk.renk())

sol, alt, sa�, �st = 0.1, 0.1, 0.3, 0.8
eksenler = �ekil.add_axes ([sol, alt, sa�, �st])
eksenler.set_xlabel ('X=(Yatay Eksen)')
eksenler.set_ylabel ('Y=(Dikey Eksen)')
eksenler.set_title ('Geli�ig�zel 20 �ak��ma');

eksenler.set_facecolor (Renk.renk())
eksenler.plot (X, Y, "--o", color=Renk.renk())
mp.show ()




