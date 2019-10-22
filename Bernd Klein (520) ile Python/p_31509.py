# coding:iso-8859-9 Türkçe
# p_31509.py: Eksenlerle şekil ebatlarını değiştirme örneği.

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
şekil = mp.figure()
X = np.arange (0,20)
Y = np.random.randint (1, 20, size=20)

sol, alt, sağ, üst = 0.15, 0.15, 0.75, 0.75
eksenler = şekil.add_axes ([sol, alt, sağ, üst])
eksenler.set_xlabel ('X=(Yatay Eksen)')
eksenler.set_ylabel ('Y=(Dikey Eksen)')
eksenler.set_title ('Gelişigüzel 20 Çakışma');

eksenler.plot (X, Y, 'r--o')
mp.show ()
#-------------------------------------------------------------------------------------------------------

şekil = mp.figure()
şekil.set_facecolor (Renk.renk())

sol, alt, sağ, üst = 0.1, 0.1, 0.8, 0.3
eksenler = şekil.add_axes ([sol, alt, sağ, üst])
eksenler.set_xlabel ('X=(Yatay Eksen)')
eksenler.set_ylabel ('Y=(Dikey Eksen)')
eksenler.set_title ('Gelişigüzel 20 Çakışma');

eksenler.plot (X, Y, 'r--o')
mp.show ()
#-------------------------------------------------------------------------------------------------------

şekil = mp.figure()
şekil.set_facecolor (Renk.renk())

sol, alt, sağ, üst = 0.1, 0.1, 0.3, 0.8
eksenler = şekil.add_axes ([sol, alt, sağ, üst])
eksenler.set_xlabel ('X=(Yatay Eksen)')
eksenler.set_ylabel ('Y=(Dikey Eksen)')
eksenler.set_title ('Gelişigüzel 20 Çakışma');

eksenler.set_facecolor (Renk.renk())
eksenler.plot (X, Y, "--o", color=Renk.renk())
mp.show ()




