# coding:iso-8859-9 Türkçe
# p_31701.py: Izgara kesişim eşhatlar haritalama grafiği örneği.

import numpy as np
import matplotlib.pyplot as mp
from p_315 import Renk

xlistesi = np.linspace (-3.0, 3.0, 3)
ylistesi = np.linspace (-3.0, 3.0, 4)
X, Y = np.meshgrid (xlistesi, ylistesi)

print ("Liste x:\n", xlistesi, sep="")
print ("\nListe y:\n", ylistesi, sep="")
print ("\nÜretilen ızgaranın x değerleri:\n", X, sep="")
print ("\nÜretilen ızgaranın y değerleri:\n", Y, sep="")
print ("-"*50)
#--------------------------------------------------------------------------------------------------------

Z = np.sqrt (X**2 + Y**2)
#Z = np.abs (X) + np.abs (Y)

print ("\nIzgara kesişim kare toplamı karekök değerleri:\n", Z, sep="")
#--------------------------------------------------------------------------------------------------------

#mp.style.use ("dark_background")
mp.figure()

eşhatlar = mp.contour (X, Y, Z)
mp.clabel (eşhatlar, inline=True, fontsize=10)
mp.title ('Eşhatlar Grafiği')
mp.xlabel ('x (sm)')
mp.ylabel ('y (sm)')

mp.show()
#--------------------------------------------------------------------------------------------------------

şekil = mp.figure()
şekil.set_facecolor (Renk.renk())

eşhatlar = şekil.add_subplot()
eşhatlar.set_facecolor (Renk.renk())
eşhatlar = mp.contour (X, Y, Z)
mp.clabel (eşhatlar, inline=True, fontsize=10)
mp.title ('Eşhatlar Grafiği', color=Renk.renk())
mp.xlabel ('x (sm)', color=Renk.renk())
mp.ylabel ('y (sm)', color=Renk.renk())

mp.show()
#--------------------------------------------------------------------------------------------------------

şekil = mp.figure()
şekil.set_facecolor (Renk.renk())

eşhatlar = şekil.add_subplot()
eşhatlar.set_facecolor (Renk.renk())
renkler = [Renk.renk() for _ in range (len (Z))]
kontur = mp.contour (X, Y, Z, colors=renkler, linestyles="dashed")
mp.clabel (kontur, inline=True, fontsize=10, colors=renkler)
mp.title ('Eşhatlar Grafiği', color=Renk.renk())
mp.xlabel ('x (sm)', color=Renk.renk())
mp.ylabel ('y (sm)', color=Renk.renk())

mp.show()



"""Çıktı:
>python p_31701.py
Liste x:
[-3.  0.  3.]

Liste y:
[-3. -1.  1.  3.]

Üretilen ızgaranın x değerleri:
[[-3.  0.  3.]
 [-3.  0.  3.]
 [-3.  0.  3.]
 [-3.  0.  3.]]

Üretilen ızgaranın y değerleri:
[[-3. -3. -3.]
 [-1. -1. -1.]
 [ 1.  1.  1.]
 [ 3.  3.  3.]]
--------------------------------------------------

Izgara kesişim kare toplamı karekök değerleri:
[[4.24264069 3.         4.24264069]
 [3.16227766 1.         3.16227766]
 [3.16227766 1.         3.16227766]
 [4.24264069 3.         4.24264069]]
"""