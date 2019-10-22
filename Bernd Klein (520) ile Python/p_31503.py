# coding:iso-8859-9 T�rk�e
# p_31503.py: �oklu farkl� ebatl� alt�ekiller �rne�i.

#import numpy as np
import matplotlib.pyplot as mp

mp.style.use ("dark_background")
X = [ (3,1,1), (3,3,4), (3,3,5), (3,3,6), (3,1,3)]
for sat�r, s�tun, aktifNo in X:
    mp.subplot (sat�r, s�tun, aktifNo).set_facecolor ("Tan")

mp.tight_layout()
mp.show()
#----------------------------------------------------------------------------------------------------

�ekil =mp.figure (figsize=(6,4))
�ekil.subplots_adjust (bottom=0, left=0, top = 1, right=1)
�ekil.set_facecolor ("LightSlateGray")

for i, j, n in X:
    alt�ekil = �ekil.add_subplot (i, j, n)
    alt�ekil.set_xticks ([])
    alt�ekil.set_yticks ([])
mp.show()
#----------------------------------------------------------------------------------------------------

X = [ (3,3,(1,3)), (3,3,4), (3,3,5), (3,3,6), (3,3,(7,9))] # 3 sat�r 3 kolon ve 9 aktifNo'lar...
�ekil =mp.figure (figsize=(6,4))
�ekil.subplots_adjust (bottom=0.05, left=0.05, top = 0.95, right=0.95)
�ekil.set_facecolor('OliveDrab')

for i, j, n in X:
    alt�ekil = �ekil.add_subplot (i, j, n)
    mp.fill_between ([0,1], [0,1], 0, color='Navy', alpha=.9)
    mp.fill_between ([0,1], [0,1],1, color='Brown', alpha=.7)
    mp.xlim (0,1)
    mp.ylim (0,1)
    alt�ekil.set_xticks ([])
    alt�ekil.set_yticks ([])
mp.show()
