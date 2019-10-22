#coding:iso-8859-9 Türkçe
# p_32501.py: Pandas serilerinin çizgi grafik olarak kullanılması örneği.

import matplotlib.pyplot as mp
import pandas as pd

mp.style.use ("dark_background")
veriler = [100, 120, 140, 180, 200, 210, 214]
seri = pd.Series (veriler) #Varsayılı: index=range (len (veriler)))
seri.plot() # Varsayılı: use_index=False

mp.show()
#------------------------------------------------------------------------------------------------------

meyveler = ['elma', 'portakal', 'kiraz', 'armut', "muz", "şeftali", "kayısı"]
miktarları = [20, 33, 52, 15, 27, 42, 9]
seri = pd.Series (miktarları, index=meyveler)
seri.plot()

mp.show()