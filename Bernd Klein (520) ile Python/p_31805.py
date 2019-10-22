# coding:iso-8859-9 T�rk�e
# p_31805.py: Bir resmi �e�itli renk karmalar�yla tonlama �rne�i.

#import numpy as np
import matplotlib.pyplot as mp
from p_315 import Renk

mp.figure().set_facecolor (Renk.renk())
mp.title ("�arli �aplin", fontsize=15, color="r")
mp.axis ("off")

�arli= mp.imread ('resim/�aplin.png')
mp.gray()
mp.imshow (�arli)
mp.show()

print ("�arli �aplin'in .png dosya datalar�:\n", �arli, sep="")
print ("\n�arli �aplin'in .png dosya �ekli: ", �arli.shape, sep="")
#-------------------------------------------------------------------------------------------------------

mp.figure().set_facecolor (Renk.renk())
mp.title ("Negatif-tonlu �arli �aplin", fontsize=15, color=Renk.renk())
mp.axis ("off")

mp.imshow (�arli [:, :, 0] * -1)
mp.show()
#-------------------------------------------------------------------------------------------------------

renkler = {'afmhot', 'autumn', 'bone', 'binary', 'bwr', 'brg', 
         'CMRmap', 'cool', 'copper', 'cubehelix', 'Greens'}
X = [  (4,3,1, (1, 0, 0)), (4,3,2, (0.5, 0.5, 0)), (4,3,3, (0, 1, 0)), 
       (4,3,4, (0, 0.5, 0.5)),  (4,3,(5,8), (0, 0, 1)), (4,3,6, (1, 1, 0)), 
       (4,3,7, (0.5, 1, 0) ),               (4,3,9, (0, 0.5, 0.5)),
       (4,3,10, (0, 0.5, 1)), (4,3,11, (0, 1, 1)),    (4,3,12, (0.5, 1, 1))]

�ekil = mp.figure (figsize=(6, 5))
�ekil.set_facecolor (Renk.renk())
mp.title ("�e�itli �arli �aplin Profilleri", fontsize=15, color=Renk.renk())
mp.axis ("off")

for i, j, n, factor in X:
    alt�ekil = �ekil.add_subplot (i, j, n)
    alt�ekil.axis ("off")
    alt�ekil.imshow (�arli [:,:,0], cmap=renkler.pop())

mp.show()



"""��kt�:
>python p_31805.py
�arli �aplin'in .png dosya datalar�:
[[[0. 0. 0. 1.]
  [0. 0. 0. 1.]
  [0. 0. 0. 1.]
  ...
  [0. 0. 0. 1.]
  [0. 0. 0. 1.]
  [0. 0. 0. 1.]]

 [[0. 0. 0. 1.]
  [0. 0. 0. 1.]
  [0. 0. 0. 1.]
  ...
  [0. 0. 0. 1.]
  [0. 0. 0. 1.]
  [0. 0. 0. 1.]]

 [[0. 0. 0. 1.]
  [0. 0. 0. 1.]
  [0. 0. 0. 1.]
  ...
  [0. 0. 0. 1.]
  [0. 0. 0. 1.]
  [0. 0. 0. 1.]]

 ...

 [[0. 0. 0. 1.]
  [0. 0. 0. 1.]
  [0. 0. 0. 1.]
  ...
  [0. 0. 0. 1.]
  [0. 0. 0. 1.]
  [0. 0. 0. 1.]]

 [[0. 0. 0. 1.]
  [0. 0. 0. 1.]
  [0. 0. 0. 1.]
  ...
  [0. 0. 0. 1.]
  [0. 0. 0. 1.]
  [0. 0. 0. 1.]]

 [[0. 0. 0. 1.]
  [0. 0. 0. 1.]
  [0. 0. 0. 1.]
  ...
  [0. 0. 0. 1.]
  [0. 0. 0. 1.]
  [0. 0. 0. 1.]]]

�arli �aplin'in .png dosya �ekli: (210, 184, 4)
"""