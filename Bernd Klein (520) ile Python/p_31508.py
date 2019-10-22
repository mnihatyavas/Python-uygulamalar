# coding:iso-8859-9 Türkçe
# p_31508.py: Izgaralar ile çoklu fonksiyonları çizme örneği.

import numpy as np
import matplotlib.pyplot as mp
import matplotlib.gridspec as mg
from p_315 import Renk

mp.style.use ("dark_background")
mp.figure (figsize=(7, 4))
ızgara = mg.GridSpec (3, 3)
X = np.linspace (0, 2 * np.pi, 200, endpoint=True)
F1 = 2.8 * np.cos (X)
F2 = 5 * np.sin (X)
F3 = 0.3 * np.sin (X)

altşekil1 = mp.subplot (ızgara [0, :])
altşekil1.plot (X, F1, 'r-', X, F2)

altşekil2 = mp.subplot (ızgara [1, :-1])
altşekil2.plot (X, F3)

altşekil3 = mp.subplot (ızgara [1:, -1])
altşekil3.plot ([0,1,2,3,4], [0,1,10,100,1000], 'b-')

altşekil4 = mp.subplot (ızgara [-1, 0])
altşekil4.plot ([0,1,2,3,4], [51, 48, 0, 42, 60], 'r-')

altşekil5 = mp.subplot (ızgara [-1, -2])
altşekil5.plot ([0,1,2,3,4], [7.5, 7, 2, 1, 0])

mp.tight_layout()
mp.show()
#-------------------------------------------------------------------------------------------------


şekil = mp.figure (figsize=(7, 4))
şekil.set_facecolor (Renk.renk())
ızgara = mg.GridSpec (3, 3)
X = np.linspace (0, 2 * np.pi, 200, endpoint=True)
F1 = 2.8 * np.cos (X)
F2 = 5 * np.sin (X)
F3 = 0.3 * np.sin (X)

altşekil1 = şekil.add_subplot (ızgara [0, 0:3])
altşekil1.set_facecolor (Renk.renk())
altşekil1.plot (X, F1, 'r-', X, F2, "y-")

altşekil2 = şekil.add_subplot (ızgara [1, 0:2])
altşekil2.set_facecolor (Renk.renk())
altşekil2.plot (X, F3, "g")

altşekil3 = şekil.add_subplot (ızgara [1:3, 2])
altşekil3.set_facecolor (Renk.renk())
altşekil3.plot ([0,1,2,3,4], [0,1,10,100,1000], 'b-')

altşekil4 = şekil.add_subplot (ızgara [2, 0])
altşekil4.set_facecolor (Renk.renk())
altşekil4.plot ([0,1,2,3,4], [51, 48, 0, 42, 60], 'r-')

altşekil5 = şekil.add_subplot (ızgara [2, 1])
altşekil5.set_facecolor (Renk.renk())
altşekil5.plot ([0,1,2,3,4], [7.5, 7, 2, 1, 0], "m")

şekil.tight_layout()
mp.show()
