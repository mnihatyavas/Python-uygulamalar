# coding:iso-8859-9 Türkçe
# p_31506.py: Izgaralık/GridSpec ile altşekli ölçekleme ve konumlandırma örneği.

import matplotlib.pyplot as mp
from matplotlib.gridspec import GridSpec
from p_315 import Renk

şekil = mp.figure()
ızgara = GridSpec (1, 1) # Tek satır ve tek sütun...
şekil.add_subplot (ızgara [0, 0] ) # altşekil...
mp.show()
#-------------------------------------------------------------------------------------------------

mp.style.use ("dark_background")
şekil = mp.figure()
ızgara = GridSpec (1, 1,
    bottom=0.25, # [0,0]'dan uzaklığı=%25
    left=0.15, # %15
    top=0.99) # %99
şekil.add_subplot (ızgara [0, 0] ) # altşekil...
mp.show()
#-------------------------------------------------------------------------------------------------

şekil = mp.figure()
şekil.set_facecolor (Renk.renk())
ızgara = GridSpec (1, 1,
    bottom=0.3, # [0,0]'dan uzaklığı=%30
    left=0.099, # %9.9
    top=0.7) # %70
şekil.add_subplot (ızgara [0, 0] ).set_facecolor (Renk.renk())
mp.show()
