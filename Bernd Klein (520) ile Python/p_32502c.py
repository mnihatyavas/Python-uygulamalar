#coding:iso-8859-9 T�rk�e
# p_32502c.py: Pandas veri �er�evesi grafi�inde ��/�oklu eksen kullan�lmas� �rne�i.

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
v� ["yo�unluk"] = (v� ["n�fus"] / v� ["y�z�l��m"]).round (2)
print ("�ehirler veri �er�evesi:\n", v�, sep="")

�ekil = mp.figure()
�ekil.suptitle ("�ehir �statistikleri")
�ekil.subplots_adjust (right=0.75)

alt�ekil1 = �ekil.subplots()
alt�ekil1.set_ylabel ("N�fus")
alt�ekil1.set_xlabel ("�ehirler")

�ekil.set_facecolor (Renk.renk())
alt�ekil1.set_facecolor (Renk.renk())

alt�ekil2, alt�ekil3 = alt�ekil1.twinx(), alt�ekil1.twinx()
alt�ekil2.set_ylabel ("Y�z�l��m�")
alt�ekil3.set_ylabel ("Yo�unluk")
sa�Omurga = alt�ekil3.spines ['right']
sa�Omurga.set_position (('axes', 1.17))
alt�ekil3.set_frame_on (True)
alt�ekil3.patch.set_visible (False)

v� ["n�fus"].plot (
    ax=alt�ekil1,
    style="-d", color=Renk.renk(),
    xticks=range (len (v�.index)),
    use_index=True,
    rot=90)
v� ["y�z�l��m"].plot (
    ax=alt�ekil2,
    style="--*", color=Renk.renk(),
    use_index=True,
    rot=90)
v� ["yo�unluk"].plot (
    ax=alt�ekil3,
    style="--o", color=Renk.renk(),
    use_index=True,
    rot=90)
�ekil.legend()
mp.show()