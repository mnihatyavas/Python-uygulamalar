#coding:iso-8859-9 T�rk�e
# p_32803.py: Zaman serilerinin grafiklenmesi �rne�i.

import pandas as pd
import matplotlib.pyplot as mp
from datetime import datetime, timedelta
from p_315 import Renk
from random import random

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

g�nSay�s� = 15
ilk = datetime (2019, 8, 13)
tarihler = [ilk + timedelta (days=i) for i in range (g�nSay�s�)]
Mersin = [int (random() * 20 + 15) for _ in range (g�nSay�s�)]
A�r� = [int (random() * 20 + 5) for _ in range (g�nSay�s�)]
zsMersin = pd.Series (Mersin, index=tarihler)
zsA�r� = pd.Series (A�r�, index=tarihler)
ortalama = (zsMersin + zsA�r�) / 2

�ekil = mp.figure (figsize=(10,4))
�ekil.set_facecolor (Renk.renk())

alt�ekil = �ekil.add_subplot()
alt�ekil.set_facecolor (Renk.renk())

mp.title ("G�nboyu S�cakl�klar")
mp.ylabel ("Selsiy�s Derece")
mp.xlabel ("Tarih")

mp.plot (zsMersin, "-d", label="Mersin", color=Renk.renk())
mp.plot (zsA�r�, "--o", label="A�r�", color=Renk.renk())
mp.plot (ortalama, "-.*", label="Ortalama", color=Renk.renk())

mp.legend (loc="best")
mp.show()