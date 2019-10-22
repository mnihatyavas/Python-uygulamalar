# coding:iso-8859-9 T�rk�e
# p_31505.py: 4x2 matrisle toplam 6 alt�ekil �retme �rne�i.

import matplotlib.pyplot as mp
from p_315 import Renk

X = [  (4,2,1), (4,2,2), (4,2,3), (4,2,5), (4,2,(4,6)), (4,1,4)]
for s, k, n in X: mp.subplot (s, k, n)
mp.tight_layout()
mp.show()
#----------------------------------------------------------------------------------------------------

mp.style.use ("dark_background")
mp.subplots_adjust (bottom=0.025, left=0.025, top = 0.975, right=0.975)
for s, k, n in X:
    mp.subplot (s, k, n).set_facecolor (Renk.renk())
    mp.xticks([])
    mp.yticks([])
mp.show()
#----------------------------------------------------------------------------------------------------

�ekil = mp.figure (figsize=(4,3))
�ekil.set_facecolor (Renk.renk())
mp.subplots_adjust (bottom=0.05, left=0.05, top = 0.95, right=0.95)
for s, k, n in X:
    alt�ekil = �ekil.add_subplot (s, k, n)
    alt�ekil.set_facecolor (Renk.renk())
    alt�ekil.set_xticks([])
    alt�ekil.set_yticks([])
mp.show()


