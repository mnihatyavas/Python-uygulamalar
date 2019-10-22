#coding:iso-8859-9 T�rk�e
# p_32502b.py: Pandas veri �er�evesi grafi�inde �ift eksen kullan�lmas� �rne�i.

import matplotlib.pyplot as mp
import pandas as pd
from p_315 import Renk

�ehirler = {"ad": ["Londra", "Berlin", "Madrid", "Roma", "Paris", "Viyana", "Bu�arest",
    "Hamburg", "Budape�te", "Var�ova", "Barselona", "M�nih", "Milano"],
            "n�fus": [8615246, 3562166, 3165235, 2874038, 2273305, 1805681, 1803425,
    1760433, 1754000, 1740119, 1602386, 1493900, 1350680],
            "y�z�l��m": [1572, 891.85, 605.77, 1285, 105.4, 414.6, 228,
    755, 525.2, 517, 101.9, 310.4, 181.8] }

v� = pd.DataFrame (�ehirler, columns=["n�fus", "y�z�l��m"], index=�ehirler ["ad"] )

print ("�ehirler veri �er�evesi:\n", v�, sep="")

�ekil = mp.figure()
�ekil.set_facecolor (Renk.renk() )
�ekil.suptitle ("�ehirlerin �statistikleri")

alt�ekil1 = �ekil.subplots()
alt�ekil1.set_ylabel ("N�fus")
alt�ekil1.set_xlabel ("�ehirler")
alt�ekil1.set_facecolor (Renk.renk() )

alt�ekil2 = alt�ekil1.twinx()
alt�ekil2.set_ylabel ("Y�z�l��m�")

v� ["n�fus"].plot (
    ax=alt�ekil1,
    style="-", color=Renk.renk(),
    xticks=range (len (v�.index)),
    use_index=True,
    rot=90)
v� ["y�z�l��m"].plot (
    ax=alt�ekil2,
    style="--", color=Renk.renk(),
    use_index=True,
    rot=90)
�ekil.legend()
mp.show()
#-------------------------------------------------------------------------------------------------------

mp.style.use ("dark_background")
alt�ekil1= v� ["n�fus"].plot (style="-", color=Renk.renk(),
                                   xticks=range (len (v�.index)),
                                   use_index=True, 
                                   rot=90)
alt�ekil2 = alt�ekil1.twinx()
v�["y�z�l��m"].plot (ax=alt�ekil2,
                        style="-", color=Renk.renk(),
                        use_index=True,
                        rot=90)
alt�ekil1.legend (loc = (.7,.9), frameon = False)
alt�ekil2.legend ( loc = (.7, .85), frameon = False)
alt�ekil1.set_facecolor (Renk.renk() )
mp.show()



"""��kt�:
>python p_32502b.py
�ehirler veri �er�evesi:
             n�fus  y�z�l��m
Londra     8615246   1572.00
Berlin     3562166    891.85
Madrid     3165235    605.77
Roma       2874038   1285.00
Paris      2273305    105.40
Viyana     1805681    414.60
Bu�arest   1803425    228.00
Hamburg    1760433    755.00
Budape�te  1754000    525.20
Var�ova    1740119    517.00
Barselona  1602386    101.90
M�nih      1493900    310.40
Milano     1350680    181.80
"""