# coding:iso-8859-9 Türkçe
# p_31504.py: 3x2 matrisle toplam 6 altşekil üretme örneği.

import matplotlib.pyplot as mp
from p_315 import Renk

mp.style.use ("dark_background")

X = [ (1,2,1), (3,2,2), (3,2,4), (3,2,6) ]
for satır, sütun, aktifNo in X: mp.subplot (satır, sütun, aktifNo)
mp.tight_layout()
mp.show()
#-------------------------------------------------------------------------------------------------------

şekil = mp.figure (figsize=(6, 4))
for i, j, n in X:
    altşekil = şekil.add_subplot (i, j, n)
    altşekil.set_facecolor (Renk.renk())
mp.tight_layout()
mp.show()

#-------------------------------------------------------------------------------------------------------
şekil = mp.figure (figsize=(6, 4))
şekil.set_facecolor (Renk.renk())
for i, j, n in X:
    altşekil = şekil.add_subplot (i, j, n)
    altşekil.set_facecolor (Renk.renk())
    altşekil.set_xticks ([])
    altşekil.set_yticks ([])
mp.show()
