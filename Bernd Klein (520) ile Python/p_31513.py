# coding:iso-8859-9 T�rk�e
# p_31513.py: Ayn� yatay eksenli ve iki farkl� dikey grafik �rne�i.

import numpy as np
import matplotlib.pyplot as mp
from p_315 import Renk

�ekil, alt�ekil1 = mp.subplots()
x = np.arange (1, 7, 0.5)

alt�ekil1.set_ylabel (r"Dairenin �evresi $(sm)$", fontsize=16, color="blue")
for �entik in alt�ekil1.get_yticklabels(): �entik.set_color ("blue")
alt�ekil1.plot (x, 2 * np.pi * x, "--o", LineWidth=0.8, color="blue")
    
alt�ekil2 = alt�ekil1.twinx()
alt�ekil2.set_ylabel (r"Dairenin alan� $(sm^2)$", fontsize=16, color="Red")
for �entik in alt�ekil2.get_yticklabels(): �entik.set_color ("Red")
alt�ekil2.plot (x, np.pi * x ** 2, "--*", linewidth=0.5, color="Red")

mp.tight_layout()
mp.show()
#---------------------------------------------------------------------------------------------------------

mp.style.use ("dark_background")
�ekil = mp.figure()
x = np.arange (1, 7, 0.5)

alt�ekil1 = �ekil.subplots()
alt�ekil1.set_ylabel (r"Dairenin �evresi $(sm)$", fontsize=16, color="blue")
for label in alt�ekil1.get_yticklabels(): label.set_color ("blue")
alt�ekil1.plot (x, 2 * np.pi * x, "--o", lw=.8, color="blue")
    
alt�ekil2 = alt�ekil1.twinx()
alt�ekil2.set_ylabel (r"Dairenin alan� $(sm^2)$", fontsize=16, color="Red")
for label in alt�ekil2.get_yticklabels(): label.set_color ("Red")
alt�ekil2.plot (x, np.pi * x ** 2, "--*", lw=.5, color="Red")

mp.tight_layout()
mp.show()
#---------------------------------------------------------------------------------------------------------

�ekil = mp.figure()
�ekil.set_facecolor (Renk.renk())
x = np.arange (1, 7, 0.5)

alt�ekil1 = �ekil.subplots()
alt�ekil1.set_facecolor (Renk.renk())
alt�ekil1.set_ylabel (r"Dairenin �evresi $(sm)$", fontsize=16, color="blue")
for label in alt�ekil1.get_yticklabels(): label.set_color ("blue")
alt�ekil1.plot (x, 2 * np.pi * x, "--o", lw=.8, color="blue")
    
alt�ekil2 = alt�ekil1.twinx()
alt�ekil2.set_facecolor (Renk.renk())
alt�ekil2.set_ylabel (r"Dairenin alan� $(sm^2)$", fontsize=16, color="Red")
for label in alt�ekil2.get_yticklabels(): label.set_color ("Red")
alt�ekil2.plot (x, np.pi * x ** 2, "--*", lw=.5, color="Red")

mp.tight_layout()
mp.show()
