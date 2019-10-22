# coding:iso-8859-9 Türkçe
# p_31903.py: İki resmi şeklen eşleştirip üstüste bindirme örneği.

import numpy as np
import matplotlib.pyplot as mp
import matplotlib.image as mi
from p_315 import Renk

def resimÖrüntüsü (resim, n, m=1):
    if n == 1: örüntüResimler = resim
    else:
        dikeyÖrüntü = []
        for i in range (n): dikeyÖrüntü.append (resim)  
        örüntüResimler = np.concatenate (dikeyÖrüntü, axis=0) # Dikey y-ekseni...
    if m > 1:
        yatayÖrüntü = []
        for i in range (m): yatayÖrüntü.append (örüntüResimler)
        örüntüResimler = np.concatenate (yatayÖrüntü, axis=1) # Yatay x-ekseni
    return örüntüResimler

atResmi = mi.imread ('resim/atİkonu.png')
# atResmi ve duvarDekorasyonu/dd aynı ebatta olacak...
bk = mi.imread ('resim/boyacılarKalıbı.png')
dd = resimÖrüntüsü (bk, 3, 4)

mp.style.use ("dark_background")
mp.axis ("off")
mp.title ("(3x4) Ebatlı DuvarDekorasyonu", color=Renk.renk())
mp.imshow (dd)
mp.show()
#-------------------------------------------------------------------------------------------------

ddŞekli = dd.shape
arŞekli = atResmi.shape
boy, en, renkler = [min (x) for x in  zip (*(ddŞekli, arŞekli))]
atResmi = atResmi [0:boy, 0:en]

mp.style.use ("dark_background")
mp.title ("DuvarDekorasyonu (3x4) ebatlı at-@ İkonu Resmi", color=Renk.renk())
mp.axis ("off")
mp.imshow (atResmi)
mp.show()
#-------------------------------------------------------------------------------------------------

karartılanDD = dd * (1 - 0.6)

mp.style.use ("dark_background")
mp.title ("%60 Karartılan DuvarDekorasyonu", color=Renk.renk())
mp.axis ("off")
mp.imshow (karartılanDD)
mp.show()
#-------------------------------------------------------------------------------------------------

karmaResim1 = np.where (atResmi [:,:, 0:3] > [0.9, 0.9, 0.9], karartılanDD, dd)

mp.style.use ("dark_background")
mp.title ("Karartılan Dekor üstü dekorlu @ Resmi", color=Renk.renk())
mp.axis ("off")
mp.imshow (karmaResim1)
mp.show()
#-------------------------------------------------------------------------------------------------

karmaResim2 = np.where (atResmi [:,:, 0:3] > [0.8, 0.8, 0.8], dd, karartılanDD)

mp.figure().set_facecolor (Renk.renk())
mp.title ("Dekor üstü karartılı dekorlu @ Resmi", color=Renk.renk())
mp.axis ("off")
mp.imshow (karmaResim2)
mp.show()
#-------------------------------------------------------------------------------------------------

print ("@ resmi şekli: ", atResmi.shape,
    "\nDuvar dekorasyonu şekli: ", ddŞekli,
    "\nKarartılan duvar dekorasyonu şekli: ", karartılanDD.shape,
    "\nKarma resim şekli: ", karmaResim1.shape, sep="")
#mi.imsave ('dekorluAt1.png', karmaResim1)
#mi.imsave ('dekorluAt2.png', karmaResim2)



"""Çıktı:
>python p_31903.py
@ resmi şekli: (1077, 1028, 4)
Duvar dekorasyonu şekli: (1077, 1028, 3)
Karartılan duvar dekorasyonu şekli: (1077, 1028, 3)
Karma resim şekli: (1077, 1028, 3)

"""
