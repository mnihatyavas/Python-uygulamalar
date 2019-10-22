# coding:iso-8859-9 Türkçe
# p_31511.py: Eksenlerin dikey-yatay kapsamlarını belirleme örneği.

import numpy as np
import matplotlib.pyplot as mp
from p_315 import Renk

mp.style.use ("dark_background")
şekil = mp.figure (figsize=(10,3)) # en,boy
altşekiller = şekil.subplots (1, 4)
x = np.arange (0, 5, 0.2)

altşekiller [0].set_title ("Varsayılı x-y kapsamı")
altşekiller [0].plot (x,x**0.5, x,x**2, x,x**3)

altşekiller[1].axis ("tight")
altşekiller[1].set_title ("Sıkı [0,1] x-y kapsamı")
altşekiller[1].plot (x,x**0.5,"r--o", x,x**2,"y--*", x,x**3,"b--^")

altşekiller[2].axis ("off")
altşekiller[2].set_title ("Kapalı/off x-y kapsamı")
altşekiller[2].plot (x,x**0.5,Renk.renk(), x,x**2,Renk.renk(), x,x**3,Renk.renk())

altşekiller[3].set_xlim ([1, 5])
altşekiller[3].set_ylim ([0, 60])
altşekiller[3].set_title ("Özel x-y kapsamı");
altşekiller[3].plot (x,x**0.5,"r-", x, x**2,"y--o", x, x**3,"b--*")

mp.tight_layout()
mp.show()
#---------------------------------------------------------------------------------------------------------

şekil, altşekiller = mp.subplots (1, 4, figsize=(10, 3))
şekil.set_facecolor (Renk.renk())
x = np.arange (0, 5, 0.2)

altşekiller [0].set_title ("Varsayılı x-y kapsamı")
altşekiller [0].set_facecolor (Renk.renk())
altşekiller [0].plot (x,x**0.5, x,x**2, x,x**3)

altşekiller[1].axis ("tight")
altşekiller[1].set_title ("Sıkı [0,1] x-y kapsamı")
altşekiller [1].set_facecolor (Renk.renk())
altşekiller[1].plot (x,x**0.5,"r--o", x,x**2,"y--*", x,x**3,"b--^")

altşekiller[2].axis ("off")
altşekiller[2].set_title ("Kapalı/off x-y kapsamı")
altşekiller [2].set_facecolor (Renk.renk())
altşekiller[2].plot (x,x**0.5,Renk.renk(), x,x**2,Renk.renk(), x,x**3,Renk.renk())

altşekiller[3].set_xlim ([1, 5])
altşekiller[3].set_ylim ([0, 60])
altşekiller[3].set_title ("Özel x-y kapsamı");
altşekiller [3].set_facecolor (Renk.renk())
altşekiller[3].plot (x,x**0.5,"r-", x, x**2,"y--o", x, x**3,"b--*")

mp.tight_layout()
mp.show()