# coding:iso-8859-9 T�rk�e
# p_31701.py: Izgara kesi�im e�hatlar haritalama grafi�i �rne�i.

import numpy as np
import matplotlib.pyplot as mp
from p_315 import Renk

xlistesi = np.linspace (-3.0, 3.0, 3)
ylistesi = np.linspace (-3.0, 3.0, 4)
X, Y = np.meshgrid (xlistesi, ylistesi)

print ("Liste x:\n", xlistesi, sep="")
print ("\nListe y:\n", ylistesi, sep="")
print ("\n�retilen �zgaran�n x de�erleri:\n", X, sep="")
print ("\n�retilen �zgaran�n y de�erleri:\n", Y, sep="")
print ("-"*50)
#--------------------------------------------------------------------------------------------------------

Z = np.sqrt (X**2 + Y**2)
#Z = np.abs (X) + np.abs (Y)

print ("\nIzgara kesi�im kare toplam� karek�k de�erleri:\n", Z, sep="")
#--------------------------------------------------------------------------------------------------------

#mp.style.use ("dark_background")
mp.figure()

e�hatlar = mp.contour (X, Y, Z)
mp.clabel (e�hatlar, inline=True, fontsize=10)
mp.title ('E�hatlar Grafi�i')
mp.xlabel ('x (sm)')
mp.ylabel ('y (sm)')

mp.show()
#--------------------------------------------------------------------------------------------------------

�ekil = mp.figure()
�ekil.set_facecolor (Renk.renk())

e�hatlar = �ekil.add_subplot()
e�hatlar.set_facecolor (Renk.renk())
e�hatlar = mp.contour (X, Y, Z)
mp.clabel (e�hatlar, inline=True, fontsize=10)
mp.title ('E�hatlar Grafi�i', color=Renk.renk())
mp.xlabel ('x (sm)', color=Renk.renk())
mp.ylabel ('y (sm)', color=Renk.renk())

mp.show()
#--------------------------------------------------------------------------------------------------------

�ekil = mp.figure()
�ekil.set_facecolor (Renk.renk())

e�hatlar = �ekil.add_subplot()
e�hatlar.set_facecolor (Renk.renk())
renkler = [Renk.renk() for _ in range (len (Z))]
kontur = mp.contour (X, Y, Z, colors=renkler, linestyles="dashed")
mp.clabel (kontur, inline=True, fontsize=10, colors=renkler)
mp.title ('E�hatlar Grafi�i', color=Renk.renk())
mp.xlabel ('x (sm)', color=Renk.renk())
mp.ylabel ('y (sm)', color=Renk.renk())

mp.show()



"""��kt�:
>python p_31701.py
Liste x:
[-3.  0.  3.]

Liste y:
[-3. -1.  1.  3.]

�retilen �zgaran�n x de�erleri:
[[-3.  0.  3.]
 [-3.  0.  3.]
 [-3.  0.  3.]
 [-3.  0.  3.]]

�retilen �zgaran�n y de�erleri:
[[-3. -3. -3.]
 [-1. -1. -1.]
 [ 1.  1.  1.]
 [ 3.  3.  3.]]
--------------------------------------------------

Izgara kesi�im kare toplam� karek�k de�erleri:
[[4.24264069 3.         4.24264069]
 [3.16227766 1.         3.16227766]
 [3.16227766 1.         3.16227766]
 [4.24264069 3.         4.24264069]]
"""