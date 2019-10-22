# coding:iso-8859-9 Türkçe
# p_31503.py: Çoklu farklı ebatlı altşekiller örneği.

#import numpy as np
import matplotlib.pyplot as mp

mp.style.use ("dark_background")
X = [ (3,1,1), (3,3,4), (3,3,5), (3,3,6), (3,1,3)]
for satır, sütun, aktifNo in X:
    mp.subplot (satır, sütun, aktifNo).set_facecolor ("Tan")

mp.tight_layout()
mp.show()
#----------------------------------------------------------------------------------------------------

şekil =mp.figure (figsize=(6,4))
şekil.subplots_adjust (bottom=0, left=0, top = 1, right=1)
şekil.set_facecolor ("LightSlateGray")

for i, j, n in X:
    altşekil = şekil.add_subplot (i, j, n)
    altşekil.set_xticks ([])
    altşekil.set_yticks ([])
mp.show()
#----------------------------------------------------------------------------------------------------

X = [ (3,3,(1,3)), (3,3,4), (3,3,5), (3,3,6), (3,3,(7,9))] # 3 satır 3 kolon ve 9 aktifNo'lar...
şekil =mp.figure (figsize=(6,4))
şekil.subplots_adjust (bottom=0.05, left=0.05, top = 0.95, right=0.95)
şekil.set_facecolor('OliveDrab')

for i, j, n in X:
    altşekil = şekil.add_subplot (i, j, n)
    mp.fill_between ([0,1], [0,1], 0, color='Navy', alpha=.9)
    mp.fill_between ([0,1], [0,1],1, color='Brown', alpha=.7)
    mp.xlim (0,1)
    mp.ylim (0,1)
    altşekil.set_xticks ([])
    altşekil.set_yticks ([])
mp.show()
