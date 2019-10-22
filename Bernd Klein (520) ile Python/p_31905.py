# coding:iso-8859-9 Türkçe
# p_31905.py: PIL resmini şekillendirilebilire dönüştürme örneği.

import numpy as np
import matplotlib.pyplot as mp
import matplotlib.image as mi
from PIL import Image as R
from p_315 import Renk

resim = R.open ("resim/sandalye.png") # .jpg'de piksel data kaybı oluyor...
try: print ("PIL open resim şekli:", resim.shape)
except Exception as ist: print (ist)

resim = resim.resize ((1028, 1077)) # Yeniden şekillendirme: (atResmi.shape[1], arResmi.shape[0])
resim = np.asarray (resim)
print ("PIL'den dönüştürülen sandalye resminin şekli:", resim.shape)
print ("Sandalye'nin (200,300) piksel'deki data'sı ():", resim [200, 300])

mp.style.use ("dark_background")
mp.title ("PIL'den dönüştürülen Sandalye", color="r")
mp.axis ("off")
mp.imshow (resim)
mp.show()
#------------------------------------------------------------------------------------------------------


resim = np.asarray (resim, np.float)
resim = resim / 255  
print ("\nSandalye'nin (200,300) piksel'deki normalleşen data'sı ():", resim [200, 300])

mp.figure().set_facecolor (Renk.renk())
mp.title ("0:255-->0:1'e normalleştirilen Sandalye", color=Renk.renk())
mp.axis ("off")
mp.imshow (resim [:,:, 0], cmap="jet")
mp.show()
#--------------

resim = mi.imread ("resim/sandalye.png")
mp.figure().set_facecolor (Renk.renk())
mp.title ("matplotlib.image'le okunan Sandalye", color=Renk.renk())
mp.axis ("off")
mp.imshow (resim [:,:, 0], cmap="YlGnBu_r")
mp.show()



"""Çıktı:
>python p_31905.py
'PngImageFile' object has no attribute 'shape'
PIL'den dönüştürülen sandalye resminin şekli: (1077, 1028, 4)
Sandalye'nin (200,300) piksel'deki data'sı (): [ 27  27  27 255]

Sandalye'nin (200,300) piksel'deki normalleşen data'sı (): [0.10588235 0.10588235 0.10588235 1.        ]
"""