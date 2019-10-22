# coding:iso-8859-9 T�rk�e
# p_31603.py: �oklu �ubuklu ve �oklu �ekilli grafikler �rne�i.

import numpy as np
import matplotlib.pyplot as mp
from p_315 import Renk

X = [1, 2, 3, 4, 6]
Y = [1, 4, 9, 16, 10]

ayr�k�ubuklar = mp.bar (X, Y)
ayr�k�ubuklar [0].set_color ('Tomato') # Varsay�l� mavi...
ayr�k�ubuklar [-1].set_color (Renk.renk())

mp.show()
#---------------------------------------------------------------------------------------------------

mp.style.use ("dark_background")
�ekil = mp.figure()
alt�ekil = �ekil.add_subplot (111)
alt�ekil.bar (X, Y)
yavrular = alt�ekil.get_children()
yavrular [3].set_color ('g')

mp.show()
#---------------------------------------------------------------------------------------------------

�ekil = mp.figure (figsize=(10,5))
�ekil.set_facecolor (Renk.renk())

alt�ekil1 = �ekil.add_subplot (121)
alt�ekil1.set_facecolor (Renk.renk())
�ubuklar1 = alt�ekil1.bar (X, Y)
for �ubuk in �ubuklar1: �ubuk.set_color (Renk.renk())

alt�ekil2 = �ekil.add_subplot (122)
alt�ekil2.set_facecolor (Renk.renk())
�ubuklar2 = alt�ekil2.bar (X, Y)
for �ubuk in �ubuklar2: �ubuk.set_color (Renk.renk())

mp.show()
