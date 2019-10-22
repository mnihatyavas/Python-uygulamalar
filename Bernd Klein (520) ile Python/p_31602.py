# coding:iso-8859-9 T�rk�e
# p_31602.py: �oklu kutulu, normalle�tirilmi� ve k�m�latif gauss histogram� �rne�i.

import numpy as np
import matplotlib.pyplot as mp
from p_315 import Renk

gaussSay�lar� = np.random.normal (size=10000)
mp.title ("100 kutulu Gauss Histogram'�", color="b")
#mp.hist (gaussSay�lar�) = mp.hist (gaussSay�lar�, bins=10)
mp.hist (gaussSay�lar�, bins=100) # Varsay�l� 10 de�il 100 adet kutu...
mp.show()
#----------------------------------------------------------------------------------------------------

mp.title ("Kutu/10000 Gauss Histogram'�", color="g")
mp.hist (gaussSay�lar�, bins=100, density=True)
# Yo�unluk: Herbir kutu i�in, (n / (len (x) ) = n/10000)...
# �ntegrali=1, yani herbir kutu en*boy toplam� = 1...
mp.show()
#----------------------------------------------------------------------------------------------------

mp.style.use ("dark_background")
mp.title ("Toplam 1'e Normalle�tirilmi� Gauss Histogram'�", color="Cyan")
mp.hist (
    gaussSay�lar�,
    bins=100, # kutu say�s� = 100
    density=True, # integrali = 1
    stacked=True, # Normalle�tirilmi� toplam� = 1
    edgecolor="#FA4662", # Kutu kenarlar� rengi
    color="#DDFFDD") # kutu i�i rengi
mp.show()
#----------------------------------------------------------------------------------------------------

�ekil = mp.figure (figsize=(7,4))
�ekil.set_facecolor (Renk.renk())

alt�ekil1 = mp.subplot (211)
alt�ekil1.set_title ("100 Kutuluk K�m�latif Gauss Histogram'�", color=Renk.renk())
alt�ekil1.set_facecolor (Renk.renk())
alt�ekil1.hist (
    gaussSay�lar�,
    bins=100,
    density=True,
    stacked=True,
    edgecolor=Renk.renk(),
    color=Renk.renk(),
    cumulative=True) # Normalle�tirilmi� kutular�n soldan-sa� toplam�

alt�ekil2 = mp.subplot (212)
alt�ekil2.set_title ("50 Kutuluk K�m�latif Gauss Histogram'�", color=Renk.renk())
alt�ekil2.set_facecolor (Renk.renk())
alt�ekil2.hist (gaussSay�lar�, bins=50, density=True, stacked=True,
    edgecolor=Renk.renk(), color=Renk.renk(), cumulative=True)

mp.tight_layout()
mp.show()
#----------------------------------------------------------------------------------------------------

�ekil = mp.figure (figsize=(10,5))
�ekil.set_facecolor (Renk.renk())

alt�ekil1 = mp.subplot (121)
alt�ekil1.set_title ("50 Kutuluk K�m�latif Gauss Histogram'�", color=Renk.renk())
alt�ekil1.set_facecolor (Renk.renk())
alt�ekil1.hist (
    gaussSay�lar�,
    bins=50,
    density=True,
    stacked=True,
    edgecolor=Renk.renk(),
    color=Renk.renk(),
    cumulative=True)

alt�ekil2 = mp.subplot (122)
alt�ekil2.set_title ("100 Kutuluk K�m�latif Gauss Histogram'�", color=Renk.renk())
alt�ekil2.set_facecolor (Renk.renk())
alt�ekil2.hist (gaussSay�lar�, bins=100, density=True, stacked=True,
    edgecolor=Renk.renk(), color=Renk.renk(), cumulative=True)

mp.tight_layout()
mp.show()