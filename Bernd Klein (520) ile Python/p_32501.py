#coding:iso-8859-9 T�rk�e
# p_32501.py: Pandas serilerinin �izgi grafik olarak kullan�lmas� �rne�i.

import matplotlib.pyplot as mp
import pandas as pd

mp.style.use ("dark_background")
veriler = [100, 120, 140, 180, 200, 210, 214]
seri = pd.Series (veriler) #Varsay�l�: index=range (len (veriler)))
seri.plot() # Varsay�l�: use_index=False

mp.show()
#------------------------------------------------------------------------------------------------------

meyveler = ['elma', 'portakal', 'kiraz', 'armut', "muz", "�eftali", "kay�s�"]
miktarlar� = [20, 33, 52, 15, 27, 42, 9]
seri = pd.Series (miktarlar�, index=meyveler)
seri.plot()

mp.show()