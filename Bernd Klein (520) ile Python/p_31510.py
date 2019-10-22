# coding:iso-8859-9 Türkçe
# p_31510.py: Eksenlerle ana şekil içinde altşekil örneği.

import numpy as np
import matplotlib.pyplot as mp
from p_315 import Renk

şekil = mp.figure()
X = [1, 2, 3, 4, 5, 6, 7]
Y = [1, 3, 4, 2, 5, 8, 6]
eksenler1 = şekil.add_axes ([0.1, 0.1, 0.85, 0.85]) # Ana eksenli şekil...
eksenler1.set_xlabel ('x = yatay eksen')
eksenler1.set_ylabel ('y = dikey eksen')
eksenler1.set_title ('Ana eksen başlığı')
eksenler1.plot (X, Y, 'r')

sol, alt, en, boy = 0.2, 0.57, 0.4, 0.3
eksenler2 = şekil.add_axes ([sol,alt, en,boy]) # İç eksenli şekil...
eksenler2.set_xlabel ('y=yatay eksen')
eksenler2.set_ylabel ('x=dikey eksen')
eksenler2.set_title ('İç eksen başlığı');
eksenler2.plot (Y, X, 'y')

mp.show()
#-----------------------------------------------------------------------------------------------------

mp.style.use ("dark_background")
şekil = mp.figure()
X = [1, 2, 3, 4, 5, 6, 7]
Y = [1, 3, 4, 2, 5, 8, 6]
eksenler1 = şekil.add_axes ([0.1, 0.1, 0.85, 0.85]) # Ana eksenli şekil...
eksenler1.set_xlabel ('x = yatay eksen')
eksenler1.set_ylabel ('y = dikey eksen')
eksenler1.set_title ('Ana eksen başlığı')
eksenler1.plot (X, Y, 'r')

sol, alt, en, boy = 0.2, 0.57, 0.4, 0.3
eksenler2 = şekil.add_axes ([sol,alt, en,boy]) # İç eksenli şekil...
eksenler2.set_xlabel ('y=yatay eksen')
eksenler2.set_ylabel ('x=dikey eksen')
eksenler2.set_title ('İç eksen başlığı');
eksenler2.plot (Y, X, 'y')

mp.show()
#-----------------------------------------------------------------------------------------------------

şekil = mp.figure()
şekil.set_facecolor (Renk.renk())
X = [1, 2, 3, 4, 5, 6, 7]
Y = [1, 3, 4, 2, 5, 8, 6]
eksenler1 = şekil.add_axes ([0.1, 0.1, 0.85, 0.85]) # Ana eksenli şekil...
eksenler1.set_xlabel ('x = yatay eksen')
eksenler1.set_ylabel ('y = dikey eksen')
eksenler1.set_title ('Ana eksen başlığı')
eksenler1.set_facecolor (Renk.renk())
eksenler1.plot (X, Y, '--o', color=Renk.renk())

sol, alt, en, boy = 0.2, 0.58, 0.4, 0.3
eksenler2 = şekil.add_axes ([sol,alt, en,boy]) # İç eksenli şekil...
eksenler2.set_xlabel ('y=yatay eksen')
eksenler2.set_ylabel ('x=dikey eksen')
eksenler2.set_title ('İç eksen başlığı');
eksenler2.set_facecolor (Renk.renk())
eksenler2.plot (Y, X, '--o', color=Renk.renk())

mp.show()