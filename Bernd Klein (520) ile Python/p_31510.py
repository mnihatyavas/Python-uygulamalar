# coding:iso-8859-9 T�rk�e
# p_31510.py: Eksenlerle ana �ekil i�inde alt�ekil �rne�i.

import numpy as np
import matplotlib.pyplot as mp
from p_315 import Renk

�ekil = mp.figure()
X = [1, 2, 3, 4, 5, 6, 7]
Y = [1, 3, 4, 2, 5, 8, 6]
eksenler1 = �ekil.add_axes ([0.1, 0.1, 0.85, 0.85]) # Ana eksenli �ekil...
eksenler1.set_xlabel ('x = yatay eksen')
eksenler1.set_ylabel ('y = dikey eksen')
eksenler1.set_title ('Ana eksen ba�l���')
eksenler1.plot (X, Y, 'r')

sol, alt, en, boy = 0.2, 0.57, 0.4, 0.3
eksenler2 = �ekil.add_axes ([sol,alt, en,boy]) # �� eksenli �ekil...
eksenler2.set_xlabel ('y=yatay eksen')
eksenler2.set_ylabel ('x=dikey eksen')
eksenler2.set_title ('�� eksen ba�l���');
eksenler2.plot (Y, X, 'y')

mp.show()
#-----------------------------------------------------------------------------------------------------

mp.style.use ("dark_background")
�ekil = mp.figure()
X = [1, 2, 3, 4, 5, 6, 7]
Y = [1, 3, 4, 2, 5, 8, 6]
eksenler1 = �ekil.add_axes ([0.1, 0.1, 0.85, 0.85]) # Ana eksenli �ekil...
eksenler1.set_xlabel ('x = yatay eksen')
eksenler1.set_ylabel ('y = dikey eksen')
eksenler1.set_title ('Ana eksen ba�l���')
eksenler1.plot (X, Y, 'r')

sol, alt, en, boy = 0.2, 0.57, 0.4, 0.3
eksenler2 = �ekil.add_axes ([sol,alt, en,boy]) # �� eksenli �ekil...
eksenler2.set_xlabel ('y=yatay eksen')
eksenler2.set_ylabel ('x=dikey eksen')
eksenler2.set_title ('�� eksen ba�l���');
eksenler2.plot (Y, X, 'y')

mp.show()
#-----------------------------------------------------------------------------------------------------

�ekil = mp.figure()
�ekil.set_facecolor (Renk.renk())
X = [1, 2, 3, 4, 5, 6, 7]
Y = [1, 3, 4, 2, 5, 8, 6]
eksenler1 = �ekil.add_axes ([0.1, 0.1, 0.85, 0.85]) # Ana eksenli �ekil...
eksenler1.set_xlabel ('x = yatay eksen')
eksenler1.set_ylabel ('y = dikey eksen')
eksenler1.set_title ('Ana eksen ba�l���')
eksenler1.set_facecolor (Renk.renk())
eksenler1.plot (X, Y, '--o', color=Renk.renk())

sol, alt, en, boy = 0.2, 0.58, 0.4, 0.3
eksenler2 = �ekil.add_axes ([sol,alt, en,boy]) # �� eksenli �ekil...
eksenler2.set_xlabel ('y=yatay eksen')
eksenler2.set_ylabel ('x=dikey eksen')
eksenler2.set_title ('�� eksen ba�l���');
eksenler2.set_facecolor (Renk.renk())
eksenler2.plot (Y, X, '--o', color=Renk.renk())

mp.show()