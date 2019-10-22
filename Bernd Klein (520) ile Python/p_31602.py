# coding:iso-8859-9 Türkçe
# p_31602.py: Çoklu kutulu, normalleştirilmiş ve kümülatif gauss histogramı örneği.

import numpy as np
import matplotlib.pyplot as mp
from p_315 import Renk

gaussSayıları = np.random.normal (size=10000)
mp.title ("100 kutulu Gauss Histogram'ı", color="b")
#mp.hist (gaussSayıları) = mp.hist (gaussSayıları, bins=10)
mp.hist (gaussSayıları, bins=100) # Varsayılı 10 değil 100 adet kutu...
mp.show()
#----------------------------------------------------------------------------------------------------

mp.title ("Kutu/10000 Gauss Histogram'ı", color="g")
mp.hist (gaussSayıları, bins=100, density=True)
# Yoğunluk: Herbir kutu için, (n / (len (x) ) = n/10000)...
# İntegrali=1, yani herbir kutu en*boy toplamı = 1...
mp.show()
#----------------------------------------------------------------------------------------------------

mp.style.use ("dark_background")
mp.title ("Toplam 1'e Normalleştirilmiş Gauss Histogram'ı", color="Cyan")
mp.hist (
    gaussSayıları,
    bins=100, # kutu sayısı = 100
    density=True, # integrali = 1
    stacked=True, # Normalleştirilmiş toplamı = 1
    edgecolor="#FA4662", # Kutu kenarları rengi
    color="#DDFFDD") # kutu içi rengi
mp.show()
#----------------------------------------------------------------------------------------------------

şekil = mp.figure (figsize=(7,4))
şekil.set_facecolor (Renk.renk())

altşekil1 = mp.subplot (211)
altşekil1.set_title ("100 Kutuluk Kümülatif Gauss Histogram'ı", color=Renk.renk())
altşekil1.set_facecolor (Renk.renk())
altşekil1.hist (
    gaussSayıları,
    bins=100,
    density=True,
    stacked=True,
    edgecolor=Renk.renk(),
    color=Renk.renk(),
    cumulative=True) # Normalleştirilmiş kutuların soldan-sağ toplamı

altşekil2 = mp.subplot (212)
altşekil2.set_title ("50 Kutuluk Kümülatif Gauss Histogram'ı", color=Renk.renk())
altşekil2.set_facecolor (Renk.renk())
altşekil2.hist (gaussSayıları, bins=50, density=True, stacked=True,
    edgecolor=Renk.renk(), color=Renk.renk(), cumulative=True)

mp.tight_layout()
mp.show()
#----------------------------------------------------------------------------------------------------

şekil = mp.figure (figsize=(10,5))
şekil.set_facecolor (Renk.renk())

altşekil1 = mp.subplot (121)
altşekil1.set_title ("50 Kutuluk Kümülatif Gauss Histogram'ı", color=Renk.renk())
altşekil1.set_facecolor (Renk.renk())
altşekil1.hist (
    gaussSayıları,
    bins=50,
    density=True,
    stacked=True,
    edgecolor=Renk.renk(),
    color=Renk.renk(),
    cumulative=True)

altşekil2 = mp.subplot (122)
altşekil2.set_title ("100 Kutuluk Kümülatif Gauss Histogram'ı", color=Renk.renk())
altşekil2.set_facecolor (Renk.renk())
altşekil2.hist (gaussSayıları, bins=100, density=True, stacked=True,
    edgecolor=Renk.renk(), color=Renk.renk(), cumulative=True)

mp.tight_layout()
mp.show()