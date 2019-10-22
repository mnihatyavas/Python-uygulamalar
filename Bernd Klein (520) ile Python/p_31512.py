# coding:iso-8859-9 T�rk�e
# p_31512.py: Logaritmik dikey ve yatay eksenli �l�ek �rne�i.

import numpy as np
import matplotlib.pyplot as mp
from p_315 import Renk

�ekil = mp.figure()
x = np.arange (0, 5, 0.2)

alt�ekil1 = �ekil.add_subplot (1, 2, 1)
alt�ekil1.set_yscale ("log")
alt�ekil1.set_title ("Logaritmik Y kapsam")
alt�ekil1.plot (x,x**0.5,"r--o", x,x**2,"y--^", x,x**3,"b--.")

alt�ekil2 = �ekil.add_subplot (1, 2, 2)
alt�ekil2.axis ("tight")
alt�ekil2.set_title ("S�k�/tight Y kapsam")
alt�ekil2.plot (x,x**0.5,"r--o", x,x**2,"y--^", x,x**3,"b--.")

mp.show()
#-----------------------------------------------------------------------------------------------------

mp.style.use ("dark_background")
�ekil = mp.figure()
x = np.arange (0, 5, 0.2)

alt�ekil1 = �ekil.add_subplot (1, 2, 1)
alt�ekil1.set_yscale ("log")
alt�ekil1.set_title ("Logaritmik Y kapsam")
alt�ekil1.plot (x,x**0.5,"r--o", x,x**2,"y--^", x,x**3,"b--.")

alt�ekil2 = �ekil.add_subplot (1, 2, 2)
alt�ekil2.axis ("tight")
alt�ekil2.set_title ("S�k�/tight Y kapsam")
alt�ekil2.plot (x,x**0.5,"r--o", x,x**2,"y--^", x,x**3,"b--.")

mp.show()
#-----------------------------------------------------------------------------------------------------

�ekil = mp.figure()
�ekil.set_facecolor (Renk.renk())
x = np.arange (0, 5, 0.2)

alt�ekil1 = �ekil.add_subplot (1, 2, 1)
alt�ekil1.set_yscale ("log")
alt�ekil1.set_title ("Logaritmik Y kapsam")
alt�ekil1.set_facecolor (Renk.renk())
alt�ekil1.plot (x,x**0.5,"r--o", x,x**2,"y--^", x,x**3,"b--.")

alt�ekil2 = �ekil.add_subplot (1, 2, 2)
alt�ekil2.set_xscale ("log")
alt�ekil1.set_yscale ("log")
alt�ekil2.set_title ("Logaritmik X kapsam")
alt�ekil2.set_facecolor (Renk.renk())
alt�ekil2.plot (x,x**0.5,"r--o", x,x**2,"y--^", x,x**3,"b--.")

mp.show()

