# coding:iso-8859-9 Türkçe
# p_31603.py: Çoklu çubuklu ve çoklu şekilli grafikler örneği.

import numpy as np
import matplotlib.pyplot as mp
from p_315 import Renk

X = [1, 2, 3, 4, 6]
Y = [1, 4, 9, 16, 10]

ayrıkÇubuklar = mp.bar (X, Y)
ayrıkÇubuklar [0].set_color ('Tomato') # Varsayılı mavi...
ayrıkÇubuklar [-1].set_color (Renk.renk())

mp.show()
#---------------------------------------------------------------------------------------------------

mp.style.use ("dark_background")
şekil = mp.figure()
altşekil = şekil.add_subplot (111)
altşekil.bar (X, Y)
yavrular = altşekil.get_children()
yavrular [3].set_color ('g')

mp.show()
#---------------------------------------------------------------------------------------------------

şekil = mp.figure (figsize=(10,5))
şekil.set_facecolor (Renk.renk())

altşekil1 = şekil.add_subplot (121)
altşekil1.set_facecolor (Renk.renk())
çubuklar1 = altşekil1.bar (X, Y)
for çubuk in çubuklar1: çubuk.set_color (Renk.renk())

altşekil2 = şekil.add_subplot (122)
altşekil2.set_facecolor (Renk.renk())
çubuklar2 = altşekil2.bar (X, Y)
for çubuk in çubuklar2: çubuk.set_color (Renk.renk())

mp.show()
