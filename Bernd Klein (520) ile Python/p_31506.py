# coding:iso-8859-9 T�rk�e
# p_31506.py: Izgaral�k/GridSpec ile alt�ekli �l�ekleme ve konumland�rma �rne�i.

import matplotlib.pyplot as mp
from matplotlib.gridspec import GridSpec
from p_315 import Renk

�ekil = mp.figure()
�zgara = GridSpec (1, 1) # Tek sat�r ve tek s�tun...
�ekil.add_subplot (�zgara [0, 0] ) # alt�ekil...
mp.show()
#-------------------------------------------------------------------------------------------------

mp.style.use ("dark_background")
�ekil = mp.figure()
�zgara = GridSpec (1, 1,
    bottom=0.25, # [0,0]'dan uzakl���=%25
    left=0.15, # %15
    top=0.99) # %99
�ekil.add_subplot (�zgara [0, 0] ) # alt�ekil...
mp.show()
#-------------------------------------------------------------------------------------------------

�ekil = mp.figure()
�ekil.set_facecolor (Renk.renk())
�zgara = GridSpec (1, 1,
    bottom=0.3, # [0,0]'dan uzakl���=%30
    left=0.099, # %9.9
    top=0.7) # %70
�ekil.add_subplot (�zgara [0, 0] ).set_facecolor (Renk.renk())
mp.show()
