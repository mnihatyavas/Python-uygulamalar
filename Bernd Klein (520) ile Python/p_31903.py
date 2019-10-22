# coding:iso-8859-9 T�rk�e
# p_31903.py: �ki resmi �eklen e�le�tirip �st�ste bindirme �rne�i.

import numpy as np
import matplotlib.pyplot as mp
import matplotlib.image as mi
from p_315 import Renk

def resim�r�nt�s� (resim, n, m=1):
    if n == 1: �r�nt�Resimler = resim
    else:
        dikey�r�nt� = []
        for i in range (n): dikey�r�nt�.append (resim)  
        �r�nt�Resimler = np.concatenate (dikey�r�nt�, axis=0) # Dikey y-ekseni...
    if m > 1:
        yatay�r�nt� = []
        for i in range (m): yatay�r�nt�.append (�r�nt�Resimler)
        �r�nt�Resimler = np.concatenate (yatay�r�nt�, axis=1) # Yatay x-ekseni
    return �r�nt�Resimler

atResmi = mi.imread ('resim/at�konu.png')
# atResmi ve duvarDekorasyonu/dd ayn� ebatta olacak...
bk = mi.imread ('resim/boyac�larKal�b�.png')
dd = resim�r�nt�s� (bk, 3, 4)

mp.style.use ("dark_background")
mp.axis ("off")
mp.title ("(3x4) Ebatl� DuvarDekorasyonu", color=Renk.renk())
mp.imshow (dd)
mp.show()
#-------------------------------------------------------------------------------------------------

dd�ekli = dd.shape
ar�ekli = atResmi.shape
boy, en, renkler = [min (x) for x in  zip (*(dd�ekli, ar�ekli))]
atResmi = atResmi [0:boy, 0:en]

mp.style.use ("dark_background")
mp.title ("DuvarDekorasyonu (3x4) ebatl� at-@ �konu Resmi", color=Renk.renk())
mp.axis ("off")
mp.imshow (atResmi)
mp.show()
#-------------------------------------------------------------------------------------------------

karart�lanDD = dd * (1 - 0.6)

mp.style.use ("dark_background")
mp.title ("%60 Karart�lan DuvarDekorasyonu", color=Renk.renk())
mp.axis ("off")
mp.imshow (karart�lanDD)
mp.show()
#-------------------------------------------------------------------------------------------------

karmaResim1 = np.where (atResmi [:,:, 0:3] > [0.9, 0.9, 0.9], karart�lanDD, dd)

mp.style.use ("dark_background")
mp.title ("Karart�lan Dekor �st� dekorlu @ Resmi", color=Renk.renk())
mp.axis ("off")
mp.imshow (karmaResim1)
mp.show()
#-------------------------------------------------------------------------------------------------

karmaResim2 = np.where (atResmi [:,:, 0:3] > [0.8, 0.8, 0.8], dd, karart�lanDD)

mp.figure().set_facecolor (Renk.renk())
mp.title ("Dekor �st� karart�l� dekorlu @ Resmi", color=Renk.renk())
mp.axis ("off")
mp.imshow (karmaResim2)
mp.show()
#-------------------------------------------------------------------------------------------------

print ("@ resmi �ekli: ", atResmi.shape,
    "\nDuvar dekorasyonu �ekli: ", dd�ekli,
    "\nKarart�lan duvar dekorasyonu �ekli: ", karart�lanDD.shape,
    "\nKarma resim �ekli: ", karmaResim1.shape, sep="")
#mi.imsave ('dekorluAt1.png', karmaResim1)
#mi.imsave ('dekorluAt2.png', karmaResim2)



"""��kt�:
>python p_31903.py
@ resmi �ekli: (1077, 1028, 4)
Duvar dekorasyonu �ekli: (1077, 1028, 3)
Karart�lan duvar dekorasyonu �ekli: (1077, 1028, 3)
Karma resim �ekli: (1077, 1028, 3)

"""
