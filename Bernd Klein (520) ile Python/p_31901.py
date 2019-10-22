# coding:iso-8859-9 Türkçe
# p_31901.py: Resmi çoklu satır sütunlu örüntü kalıbı olarak kullanma örneği.

import numpy as np
import matplotlib.pyplot as mp
import matplotlib.image as mi
from p_315 import Renk

def resimÖrüntüsü (resim, n, m=1): # (n,m): (satır x sütun)
    if n == 1: örüntüResimler = resim
    else:
        dikeyÖrüntü = []
        for i in range (n): dikeyÖrüntü.append (resim)  
        örüntüResimler = np.concatenate (dikeyÖrüntü, axis=0) # Dikey y-ekseni...
    if m > 1:
        yatayÖrüntü = []
        for i in range (m): yatayÖrüntü.append (örüntüResimler)  
        örüntüResimler = np.concatenate (yatayÖrüntü, axis=1 ) # Yatay x-ekseni
    return örüntüResimler

mp.style.use ("dark_background")
boyacılarKalıbı = mi.imread ('resim/boyacılarKalıbı.png')
duvarDekorasyonu = resimÖrüntüsü (boyacılarKalıbı, 3, 4)

mp.title ("(3x4) Örüntülü 4'er Avatarlı Resimli Kalıp")
mp.axis ("off")
mp.imshow (duvarDekorasyonu)
mp.show()
#-----------------------------------------------------------------------------------------------------

duvarDekorasyonu = resimÖrüntüsü (boyacılarKalıbı, 4, 5)

mp.figure().set_facecolor (Renk.renk())
mp.title ("(4x5) Örüntülü 4'er Avatarlı Resimli Kalıp", color=Renk.renk())
mp.axis ("off")
mp.imshow (duvarDekorasyonu)
mp.show()