# coding:iso-8859-9 Türkçe
# p_31904.py: Üç farklı resmi karmalaştırıp üstüste gösterme örneği.

import numpy as np
import matplotlib.pyplot as mp
import matplotlib.image as mi
from p_315 import Renk

resimler = [mi.imread (resim) for resim in ["resim/sandalye.png", "resim/deniz.png", "resim/dekor.png"] ]
sandalye, deniz, dekor = resimler

print (sandalye.shape, deniz.shape, dekor.shape)

mp.style.use ("dark_background")
mp.title ("(256,201,4) şekilli Sandalye", color="r")
mp.axis ("off")
mp.imshow (sandalye)
mp.show()
#----------------------------------------------------------------------------------------------------

mp.style.use ("dark_background")
mp.title ("(256,201,4) şekilli Deniz", color="r")
mp.axis ("off")
mp.imshow (deniz)
mp.show()
#----------------------------------------------------------------------------------------------------

mp.style.use ("dark_background")
mp.title ("(256,201,4) şekilli Dekor", color="r")
mp.axis ("off")
mp.imshow (dekor)
mp.show()
#----------------------------------------------------------------------------------------------------

karma1 = np.where (sandalye > [0.9, 0.9, 0.9, 0.9], dekor, deniz)
#karma1 = np.where (sandalye[:,:,0:3] > [0.9, 0.9, 0.9], dekor[:,:,0:3], deniz[:,:,0:3])

mp.style.use ("dark_background")
mp.title ("Dekor üstü denizli Sandalye", color="r")
mp.axis("off")
mp.imshow (karma1)
mp.show()
#---------------------------------------------------------------------------------------------------

#karma2 = np.where (sandalye > [0.8, 0.8, 0.8, 0.8], deniz, dekor)
karma2 = np.where (sandalye[:,:,0:3] > [0.8, 0.8, 0.8], deniz[:,:,0:3], dekor[:,:,0:3])

mp.figure().set_facecolor (Renk.renk())
mp.title ("Deniz üstü dekorlu Sandalye", color=Renk.renk())
mp.axis("off")
mp.imshow (karma2)
mp.show()



"""Çıktı:
>python p_31904.py
(256, 201, 4) (256, 201, 4) (256, 201, 4)
"""