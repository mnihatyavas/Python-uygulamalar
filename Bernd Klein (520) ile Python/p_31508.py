# coding:iso-8859-9 T�rk�e
# p_31508.py: Izgaralar ile �oklu fonksiyonlar� �izme �rne�i.

import numpy as np
import matplotlib.pyplot as mp
import matplotlib.gridspec as mg
from p_315 import Renk

mp.style.use ("dark_background")
mp.figure (figsize=(7, 4))
�zgara = mg.GridSpec (3, 3)
X = np.linspace (0, 2 * np.pi, 200, endpoint=True)
F1 = 2.8 * np.cos (X)
F2 = 5 * np.sin (X)
F3 = 0.3 * np.sin (X)

alt�ekil1 = mp.subplot (�zgara [0, :])
alt�ekil1.plot (X, F1, 'r-', X, F2)

alt�ekil2 = mp.subplot (�zgara [1, :-1])
alt�ekil2.plot (X, F3)

alt�ekil3 = mp.subplot (�zgara [1:, -1])
alt�ekil3.plot ([0,1,2,3,4], [0,1,10,100,1000], 'b-')

alt�ekil4 = mp.subplot (�zgara [-1, 0])
alt�ekil4.plot ([0,1,2,3,4], [51, 48, 0, 42, 60], 'r-')

alt�ekil5 = mp.subplot (�zgara [-1, -2])
alt�ekil5.plot ([0,1,2,3,4], [7.5, 7, 2, 1, 0])

mp.tight_layout()
mp.show()
#-------------------------------------------------------------------------------------------------


�ekil = mp.figure (figsize=(7, 4))
�ekil.set_facecolor (Renk.renk())
�zgara = mg.GridSpec (3, 3)
X = np.linspace (0, 2 * np.pi, 200, endpoint=True)
F1 = 2.8 * np.cos (X)
F2 = 5 * np.sin (X)
F3 = 0.3 * np.sin (X)

alt�ekil1 = �ekil.add_subplot (�zgara [0, 0:3])
alt�ekil1.set_facecolor (Renk.renk())
alt�ekil1.plot (X, F1, 'r-', X, F2, "y-")

alt�ekil2 = �ekil.add_subplot (�zgara [1, 0:2])
alt�ekil2.set_facecolor (Renk.renk())
alt�ekil2.plot (X, F3, "g")

alt�ekil3 = �ekil.add_subplot (�zgara [1:3, 2])
alt�ekil3.set_facecolor (Renk.renk())
alt�ekil3.plot ([0,1,2,3,4], [0,1,10,100,1000], 'b-')

alt�ekil4 = �ekil.add_subplot (�zgara [2, 0])
alt�ekil4.set_facecolor (Renk.renk())
alt�ekil4.plot ([0,1,2,3,4], [51, 48, 0, 42, 60], 'r-')

alt�ekil5 = �ekil.add_subplot (�zgara [2, 1])
alt�ekil5.set_facecolor (Renk.renk())
alt�ekil5.plot ([0,1,2,3,4], [7.5, 7, 2, 1, 0], "m")

�ekil.tight_layout()
mp.show()
