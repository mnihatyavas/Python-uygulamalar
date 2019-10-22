# coding:iso-8859-9 Türkçe
# p_31805.py: Bir resmi çeşitli renk karmalarıyla tonlama örneği.

#import numpy as np
import matplotlib.pyplot as mp
from p_315 import Renk

mp.figure().set_facecolor (Renk.renk())
mp.title ("Çarli Çaplin", fontsize=15, color="r")
mp.axis ("off")

Çarli= mp.imread ('resim/çaplin.png')
mp.gray()
mp.imshow (Çarli)
mp.show()

print ("Çarli çaplin'in .png dosya dataları:\n", Çarli, sep="")
print ("\nÇarli çaplin'in .png dosya şekli: ", Çarli.shape, sep="")
#-------------------------------------------------------------------------------------------------------

mp.figure().set_facecolor (Renk.renk())
mp.title ("Negatif-tonlu Çarli Çaplin", fontsize=15, color=Renk.renk())
mp.axis ("off")

mp.imshow (Çarli [:, :, 0] * -1)
mp.show()
#-------------------------------------------------------------------------------------------------------

renkler = {'afmhot', 'autumn', 'bone', 'binary', 'bwr', 'brg', 
         'CMRmap', 'cool', 'copper', 'cubehelix', 'Greens'}
X = [  (4,3,1, (1, 0, 0)), (4,3,2, (0.5, 0.5, 0)), (4,3,3, (0, 1, 0)), 
       (4,3,4, (0, 0.5, 0.5)),  (4,3,(5,8), (0, 0, 1)), (4,3,6, (1, 1, 0)), 
       (4,3,7, (0.5, 1, 0) ),               (4,3,9, (0, 0.5, 0.5)),
       (4,3,10, (0, 0.5, 1)), (4,3,11, (0, 1, 1)),    (4,3,12, (0.5, 1, 1))]

şekil = mp.figure (figsize=(6, 5))
şekil.set_facecolor (Renk.renk())
mp.title ("Çeşitli Çarli Çaplin Profilleri", fontsize=15, color=Renk.renk())
mp.axis ("off")

for i, j, n, factor in X:
    altşekil = şekil.add_subplot (i, j, n)
    altşekil.axis ("off")
    altşekil.imshow (Çarli [:,:,0], cmap=renkler.pop())

mp.show()



"""Çıktı:
>python p_31805.py
Çarli çaplin'in .png dosya dataları:
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

Çarli çaplin'in .png dosya şekli: (210, 184, 4)
"""