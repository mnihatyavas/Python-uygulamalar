# coding:iso-8859-9 T�rk�e
# p_31504.py: 3x2 matrisle toplam 6 alt�ekil �retme �rne�i.

import matplotlib.pyplot as mp
from p_315 import Renk

mp.style.use ("dark_background")

X = [ (1,2,1), (3,2,2), (3,2,4), (3,2,6) ]
for sat�r, s�tun, aktifNo in X: mp.subplot (sat�r, s�tun, aktifNo)
mp.tight_layout()
mp.show()
#-------------------------------------------------------------------------------------------------------

�ekil = mp.figure (figsize=(6, 4))
for i, j, n in X:
    alt�ekil = �ekil.add_subplot (i, j, n)
    alt�ekil.set_facecolor (Renk.renk())
mp.tight_layout()
mp.show()

#-------------------------------------------------------------------------------------------------------
�ekil = mp.figure (figsize=(6, 4))
�ekil.set_facecolor (Renk.renk())
for i, j, n in X:
    alt�ekil = �ekil.add_subplot (i, j, n)
    alt�ekil.set_facecolor (Renk.renk())
    alt�ekil.set_xticks ([])
    alt�ekil.set_yticks ([])
mp.show()
