# coding:iso-8859-9 Türkçe
# p_31513.py: Aynı yatay eksenli ve iki farklı dikey grafik örneği.

import numpy as np
import matplotlib.pyplot as mp
from p_315 import Renk

şekil, altşekil1 = mp.subplots()
x = np.arange (1, 7, 0.5)

altşekil1.set_ylabel (r"Dairenin çevresi $(sm)$", fontsize=16, color="blue")
for çentik in altşekil1.get_yticklabels(): çentik.set_color ("blue")
altşekil1.plot (x, 2 * np.pi * x, "--o", LineWidth=0.8, color="blue")
    
altşekil2 = altşekil1.twinx()
altşekil2.set_ylabel (r"Dairenin alanı $(sm^2)$", fontsize=16, color="Red")
for çentik in altşekil2.get_yticklabels(): çentik.set_color ("Red")
altşekil2.plot (x, np.pi * x ** 2, "--*", linewidth=0.5, color="Red")

mp.tight_layout()
mp.show()
#---------------------------------------------------------------------------------------------------------

mp.style.use ("dark_background")
şekil = mp.figure()
x = np.arange (1, 7, 0.5)

altşekil1 = şekil.subplots()
altşekil1.set_ylabel (r"Dairenin çevresi $(sm)$", fontsize=16, color="blue")
for label in altşekil1.get_yticklabels(): label.set_color ("blue")
altşekil1.plot (x, 2 * np.pi * x, "--o", lw=.8, color="blue")
    
altşekil2 = altşekil1.twinx()
altşekil2.set_ylabel (r"Dairenin alanı $(sm^2)$", fontsize=16, color="Red")
for label in altşekil2.get_yticklabels(): label.set_color ("Red")
altşekil2.plot (x, np.pi * x ** 2, "--*", lw=.5, color="Red")

mp.tight_layout()
mp.show()
#---------------------------------------------------------------------------------------------------------

şekil = mp.figure()
şekil.set_facecolor (Renk.renk())
x = np.arange (1, 7, 0.5)

altşekil1 = şekil.subplots()
altşekil1.set_facecolor (Renk.renk())
altşekil1.set_ylabel (r"Dairenin çevresi $(sm)$", fontsize=16, color="blue")
for label in altşekil1.get_yticklabels(): label.set_color ("blue")
altşekil1.plot (x, 2 * np.pi * x, "--o", lw=.8, color="blue")
    
altşekil2 = altşekil1.twinx()
altşekil2.set_facecolor (Renk.renk())
altşekil2.set_ylabel (r"Dairenin alanı $(sm^2)$", fontsize=16, color="Red")
for label in altşekil2.get_yticklabels(): label.set_color ("Red")
altşekil2.plot (x, np.pi * x ** 2, "--*", lw=.5, color="Red")

mp.tight_layout()
mp.show()
