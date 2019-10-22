# coding:iso-8859-9 T�rk�e
# p_31511.py: Eksenlerin dikey-yatay kapsamlar�n� belirleme �rne�i.

import numpy as np
import matplotlib.pyplot as mp
from p_315 import Renk

mp.style.use ("dark_background")
�ekil = mp.figure (figsize=(10,3)) # en,boy
alt�ekiller = �ekil.subplots (1, 4)
x = np.arange (0, 5, 0.2)

alt�ekiller [0].set_title ("Varsay�l� x-y kapsam�")
alt�ekiller [0].plot (x,x**0.5, x,x**2, x,x**3)

alt�ekiller[1].axis ("tight")
alt�ekiller[1].set_title ("S�k� [0,1] x-y kapsam�")
alt�ekiller[1].plot (x,x**0.5,"r--o", x,x**2,"y--*", x,x**3,"b--^")

alt�ekiller[2].axis ("off")
alt�ekiller[2].set_title ("Kapal�/off x-y kapsam�")
alt�ekiller[2].plot (x,x**0.5,Renk.renk(), x,x**2,Renk.renk(), x,x**3,Renk.renk())

alt�ekiller[3].set_xlim ([1, 5])
alt�ekiller[3].set_ylim ([0, 60])
alt�ekiller[3].set_title ("�zel x-y kapsam�");
alt�ekiller[3].plot (x,x**0.5,"r-", x, x**2,"y--o", x, x**3,"b--*")

mp.tight_layout()
mp.show()
#---------------------------------------------------------------------------------------------------------

�ekil, alt�ekiller = mp.subplots (1, 4, figsize=(10, 3))
�ekil.set_facecolor (Renk.renk())
x = np.arange (0, 5, 0.2)

alt�ekiller [0].set_title ("Varsay�l� x-y kapsam�")
alt�ekiller [0].set_facecolor (Renk.renk())
alt�ekiller [0].plot (x,x**0.5, x,x**2, x,x**3)

alt�ekiller[1].axis ("tight")
alt�ekiller[1].set_title ("S�k� [0,1] x-y kapsam�")
alt�ekiller [1].set_facecolor (Renk.renk())
alt�ekiller[1].plot (x,x**0.5,"r--o", x,x**2,"y--*", x,x**3,"b--^")

alt�ekiller[2].axis ("off")
alt�ekiller[2].set_title ("Kapal�/off x-y kapsam�")
alt�ekiller [2].set_facecolor (Renk.renk())
alt�ekiller[2].plot (x,x**0.5,Renk.renk(), x,x**2,Renk.renk(), x,x**3,Renk.renk())

alt�ekiller[3].set_xlim ([1, 5])
alt�ekiller[3].set_ylim ([0, 60])
alt�ekiller[3].set_title ("�zel x-y kapsam�");
alt�ekiller [3].set_facecolor (Renk.renk())
alt�ekiller[3].plot (x,x**0.5,"r-", x, x**2,"y--o", x, x**3,"b--*")

mp.tight_layout()
mp.show()