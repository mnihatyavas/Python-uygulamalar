# coding:iso-8859-9 Türkçe
# p_31902.py: Resmin herhangibir dikdörtgen dilimini görüntüleme örneği.

import matplotlib.pyplot as mp
import matplotlib.image as mi
from p_315 import Renk

mp.style.use ("dark_background")
boyacılarKalıbı = mi.imread ('resim/boyacılarKalıbı.png')
dilim = boyacılarKalıbı [90:150, 50:120] # dikdörtgen [satır1:satır2, sütun1:sütun2]

mp.title ("Resmin [satırlar, sütunlar]=[90:150, 50:120] Dilimi")
mp.axis ("off")
mp.imshow (dilim)
mp.show()
#-----------------------------------------------------------------------------------------------------

mp.figure().set_facecolor (Renk.renk())
dilim = boyacılarKalıbı [190:300, 150:240]
mp.title ("Resmin [satırlar, sütunlar]=[190:300, 150:240] Dilimi", color=Renk.renk())
mp.axis ("off")
mp.imshow (dilim)
mp.show()
