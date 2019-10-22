# coding:iso-8859-9 Türkçe
# p_31512.py: Logaritmik dikey ve yatay eksenli ölçek örneği.

import numpy as np
import matplotlib.pyplot as mp
from p_315 import Renk

şekil = mp.figure()
x = np.arange (0, 5, 0.2)

altşekil1 = şekil.add_subplot (1, 2, 1)
altşekil1.set_yscale ("log")
altşekil1.set_title ("Logaritmik Y kapsam")
altşekil1.plot (x,x**0.5,"r--o", x,x**2,"y--^", x,x**3,"b--.")

altşekil2 = şekil.add_subplot (1, 2, 2)
altşekil2.axis ("tight")
altşekil2.set_title ("Sıkı/tight Y kapsam")
altşekil2.plot (x,x**0.5,"r--o", x,x**2,"y--^", x,x**3,"b--.")

mp.show()
#-----------------------------------------------------------------------------------------------------

mp.style.use ("dark_background")
şekil = mp.figure()
x = np.arange (0, 5, 0.2)

altşekil1 = şekil.add_subplot (1, 2, 1)
altşekil1.set_yscale ("log")
altşekil1.set_title ("Logaritmik Y kapsam")
altşekil1.plot (x,x**0.5,"r--o", x,x**2,"y--^", x,x**3,"b--.")

altşekil2 = şekil.add_subplot (1, 2, 2)
altşekil2.axis ("tight")
altşekil2.set_title ("Sıkı/tight Y kapsam")
altşekil2.plot (x,x**0.5,"r--o", x,x**2,"y--^", x,x**3,"b--.")

mp.show()
#-----------------------------------------------------------------------------------------------------

şekil = mp.figure()
şekil.set_facecolor (Renk.renk())
x = np.arange (0, 5, 0.2)

altşekil1 = şekil.add_subplot (1, 2, 1)
altşekil1.set_yscale ("log")
altşekil1.set_title ("Logaritmik Y kapsam")
altşekil1.set_facecolor (Renk.renk())
altşekil1.plot (x,x**0.5,"r--o", x,x**2,"y--^", x,x**3,"b--.")

altşekil2 = şekil.add_subplot (1, 2, 2)
altşekil2.set_xscale ("log")
altşekil1.set_yscale ("log")
altşekil2.set_title ("Logaritmik X kapsam")
altşekil2.set_facecolor (Renk.renk())
altşekil2.plot (x,x**0.5,"r--o", x,x**2,"y--^", x,x**3,"b--.")

mp.show()

