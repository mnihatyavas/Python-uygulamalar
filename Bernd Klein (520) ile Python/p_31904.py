# coding:iso-8859-9 T�rk�e
# p_31904.py: �� farkl� resmi karmala�t�r�p �st�ste g�sterme �rne�i.

import numpy as np
import matplotlib.pyplot as mp
import matplotlib.image as mi
from p_315 import Renk

resimler = [mi.imread (resim) for resim in ["resim/sandalye.png", "resim/deniz.png", "resim/dekor.png"] ]
sandalye, deniz, dekor = resimler

print (sandalye.shape, deniz.shape, dekor.shape)

mp.style.use ("dark_background")
mp.title ("(256,201,4) �ekilli Sandalye", color="r")
mp.axis ("off")
mp.imshow (sandalye)
mp.show()
#----------------------------------------------------------------------------------------------------

mp.style.use ("dark_background")
mp.title ("(256,201,4) �ekilli Deniz", color="r")
mp.axis ("off")
mp.imshow (deniz)
mp.show()
#----------------------------------------------------------------------------------------------------

mp.style.use ("dark_background")
mp.title ("(256,201,4) �ekilli Dekor", color="r")
mp.axis ("off")
mp.imshow (dekor)
mp.show()
#----------------------------------------------------------------------------------------------------

karma1 = np.where (sandalye > [0.9, 0.9, 0.9, 0.9], dekor, deniz)
#karma1 = np.where (sandalye[:,:,0:3] > [0.9, 0.9, 0.9], dekor[:,:,0:3], deniz[:,:,0:3])

mp.style.use ("dark_background")
mp.title ("Dekor �st� denizli Sandalye", color="r")
mp.axis("off")
mp.imshow (karma1)
mp.show()
#---------------------------------------------------------------------------------------------------

#karma2 = np.where (sandalye > [0.8, 0.8, 0.8, 0.8], deniz, dekor)
karma2 = np.where (sandalye[:,:,0:3] > [0.8, 0.8, 0.8], deniz[:,:,0:3], dekor[:,:,0:3])

mp.figure().set_facecolor (Renk.renk())
mp.title ("Deniz �st� dekorlu Sandalye", color=Renk.renk())
mp.axis("off")
mp.imshow (karma2)
mp.show()



"""��kt�:
>python p_31904.py
(256, 201, 4) (256, 201, 4) (256, 201, 4)
"""