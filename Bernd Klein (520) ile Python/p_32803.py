#coding:iso-8859-9 Türkçe
# p_32803.py: Zaman serilerinin grafiklenmesi örneği.

import pandas as pd
import matplotlib.pyplot as mp
from datetime import datetime, timedelta
from p_315 import Renk
from random import random

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

günSayısı = 15
ilk = datetime (2019, 8, 13)
tarihler = [ilk + timedelta (days=i) for i in range (günSayısı)]
Mersin = [int (random() * 20 + 15) for _ in range (günSayısı)]
Ağrı = [int (random() * 20 + 5) for _ in range (günSayısı)]
zsMersin = pd.Series (Mersin, index=tarihler)
zsAğrı = pd.Series (Ağrı, index=tarihler)
ortalama = (zsMersin + zsAğrı) / 2

şekil = mp.figure (figsize=(10,4))
şekil.set_facecolor (Renk.renk())

altşekil = şekil.add_subplot()
altşekil.set_facecolor (Renk.renk())

mp.title ("Günboyu Sıcaklıklar")
mp.ylabel ("Selsiyüs Derece")
mp.xlabel ("Tarih")

mp.plot (zsMersin, "-d", label="Mersin", color=Renk.renk())
mp.plot (zsAğrı, "--o", label="Ağrı", color=Renk.renk())
mp.plot (ortalama, "-.*", label="Ortalama", color=Renk.renk())

mp.legend (loc="best")
mp.show()