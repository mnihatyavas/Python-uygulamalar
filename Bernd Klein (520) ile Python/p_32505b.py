#coding:iso-8859-9 Türkçe
# p_32505b.py: Meyveler ve ağırlıkları serisinin bütün ve parçalı börek grafiği örneği.

import matplotlib.pyplot as mp
import pandas as pd
from p_315 import Renk
from random import random

mp.style.use ("dark_background")
meyveler = ['elma', 'portakal', 'kiraz', 'armut', "muz", "şeftali", "kayısı"]
seri = pd.Series ([20, 33, 52, 15, 27, 42, 9], index=meyveler, name="Meyve serisi")

seri.plot (kind="pie", colors=[Renk.renk() for _ in range (len (meyveler))] )
mp.show()

seri.plot.pie (figsize=(4, 4), colors=[Renk.renk() for _ in range (len (meyveler))] )
mp.show()
#--------------------------------------------------------------------------------------------------------

parçala = [int (random() * 100) / 100 for _ in range (len (meyveler))]
print ("Meyveler ve parçalanma oranları:\n", meyveler, "\n", parçala, sep="")
seri.plot.pie (figsize=(6, 6), explode=parçala, colors=[Renk.renk() for _ in range (len (meyveler))] )
# Parçalar görüntü dışıysa sağ-üst köşedeki pencere ikonunu tam-genişlet...
mp.show()



"""Çıktı:
>python p_32505b.py
Meyveler ve parçalanma oranları:
['elma', 'portakal', 'kiraz', 'armut', 'muz', 'şeftali', 'kayısı']
[0.31, 0.76, 0.33, 0.12, 0.46, 0.94, 0.1]

"""