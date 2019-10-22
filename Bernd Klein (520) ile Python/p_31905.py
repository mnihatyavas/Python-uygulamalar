# coding:iso-8859-9 T�rk�e
# p_31905.py: PIL resmini �ekillendirilebilire d�n��t�rme �rne�i.

import numpy as np
import matplotlib.pyplot as mp
import matplotlib.image as mi
from PIL import Image as R
from p_315 import Renk

resim = R.open ("resim/sandalye.png") # .jpg'de piksel data kayb� oluyor...
try: print ("PIL open resim �ekli:", resim.shape)
except Exception as ist: print (ist)

resim = resim.resize ((1028, 1077)) # Yeniden �ekillendirme: (atResmi.shape[1], arResmi.shape[0])
resim = np.asarray (resim)
print ("PIL'den d�n��t�r�len sandalye resminin �ekli:", resim.shape)
print ("Sandalye'nin (200,300) piksel'deki data's� ():", resim [200, 300])

mp.style.use ("dark_background")
mp.title ("PIL'den d�n��t�r�len Sandalye", color="r")
mp.axis ("off")
mp.imshow (resim)
mp.show()
#------------------------------------------------------------------------------------------------------


resim = np.asarray (resim, np.float)
resim = resim / 255  
print ("\nSandalye'nin (200,300) piksel'deki normalle�en data's� ():", resim [200, 300])

mp.figure().set_facecolor (Renk.renk())
mp.title ("0:255-->0:1'e normalle�tirilen Sandalye", color=Renk.renk())
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



"""��kt�:
>python p_31905.py
'PngImageFile' object has no attribute 'shape'
PIL'den d�n��t�r�len sandalye resminin �ekli: (1077, 1028, 4)
Sandalye'nin (200,300) piksel'deki data's� (): [ 27  27  27 255]

Sandalye'nin (200,300) piksel'deki normalle�en data's� (): [0.10588235 0.10588235 0.10588235 1.        ]
"""