# coding:iso-8859-9 T�rk�e
# p_31902.py: Resmin herhangibir dikd�rtgen dilimini g�r�nt�leme �rne�i.

import matplotlib.pyplot as mp
import matplotlib.image as mi
from p_315 import Renk

mp.style.use ("dark_background")
boyac�larKal�b� = mi.imread ('resim/boyac�larKal�b�.png')
dilim = boyac�larKal�b� [90:150, 50:120] # dikd�rtgen [sat�r1:sat�r2, s�tun1:s�tun2]

mp.title ("Resmin [sat�rlar, s�tunlar]=[90:150, 50:120] Dilimi")
mp.axis ("off")
mp.imshow (dilim)
mp.show()
#-----------------------------------------------------------------------------------------------------

mp.figure().set_facecolor (Renk.renk())
dilim = boyac�larKal�b� [190:300, 150:240]
mp.title ("Resmin [sat�rlar, s�tunlar]=[190:300, 150:240] Dilimi", color=Renk.renk())
mp.axis ("off")
mp.imshow (dilim)
mp.show()
