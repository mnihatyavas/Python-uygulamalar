#coding:iso-8859-9 T�rk�e
# p_32505b.py: Meyveler ve a��rl�klar� serisinin b�t�n ve par�al� b�rek grafi�i �rne�i.

import matplotlib.pyplot as mp
import pandas as pd
from p_315 import Renk
from random import random

mp.style.use ("dark_background")
meyveler = ['elma', 'portakal', 'kiraz', 'armut', "muz", "�eftali", "kay�s�"]
seri = pd.Series ([20, 33, 52, 15, 27, 42, 9], index=meyveler, name="Meyve serisi")

seri.plot (kind="pie", colors=[Renk.renk() for _ in range (len (meyveler))] )
mp.show()

seri.plot.pie (figsize=(4, 4), colors=[Renk.renk() for _ in range (len (meyveler))] )
mp.show()
#--------------------------------------------------------------------------------------------------------

par�ala = [int (random() * 100) / 100 for _ in range (len (meyveler))]
print ("Meyveler ve par�alanma oranlar�:\n", meyveler, "\n", par�ala, sep="")
seri.plot.pie (figsize=(6, 6), explode=par�ala, colors=[Renk.renk() for _ in range (len (meyveler))] )
# Par�alar g�r�nt� d���ysa sa�-�st k��edeki pencere ikonunu tam-geni�let...
mp.show()



"""��kt�:
>python p_32505b.py
Meyveler ve par�alanma oranlar�:
['elma', 'portakal', 'kiraz', 'armut', 'muz', '�eftali', 'kay�s�']
[0.31, 0.76, 0.33, 0.12, 0.46, 0.94, 0.1]

"""