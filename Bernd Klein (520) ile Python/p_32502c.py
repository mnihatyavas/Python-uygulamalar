#coding:iso-8859-9 Türkçe
# p_32502c.py: Pandas veri çerçevesi grafiğinde üç/çoklu eksen kullanılması örneği.

import matplotlib.pyplot as mp
import pandas as pd
from p_315 import Renk

şehirler = {"ad": ["Londra", "Berlin", "Madrid", "Roma", "Paris", "Viyana", "Buçarest",
    "Hamburg", "Budapeşte", "Varşova", "Barselona", "Münih", "Milano"],
            "nüfus": [8615246, 3562166, 3165235, 2874038, 2273305, 1805681, 1803425,
    1760433, 1754000, 1740119, 1602386, 1493900, 1350680],
            "yüzölçüm": [1572, 891.85, 605.77, 1285, 105.4, 414.6, 228,
    755, 525.2, 517, 101.9, 310.4, 181.8] }

vÇ = pd.DataFrame (şehirler, columns=["nüfus", "yüzölçüm"], index=şehirler ["ad"] )
vÇ ["yoğunluk"] = (vÇ ["nüfus"] / vÇ ["yüzölçüm"]).round (2)
print ("Şehirler veri çerçevesi:\n", vÇ, sep="")

şekil = mp.figure()
şekil.suptitle ("Şehir İstatistikleri")
şekil.subplots_adjust (right=0.75)

altşekil1 = şekil.subplots()
altşekil1.set_ylabel ("Nüfus")
altşekil1.set_xlabel ("Şehirler")

şekil.set_facecolor (Renk.renk())
altşekil1.set_facecolor (Renk.renk())

altşekil2, altşekil3 = altşekil1.twinx(), altşekil1.twinx()
altşekil2.set_ylabel ("Yüzölçümü")
altşekil3.set_ylabel ("Yoğunluk")
sağOmurga = altşekil3.spines ['right']
sağOmurga.set_position (('axes', 1.17))
altşekil3.set_frame_on (True)
altşekil3.patch.set_visible (False)

vÇ ["nüfus"].plot (
    ax=altşekil1,
    style="-d", color=Renk.renk(),
    xticks=range (len (vÇ.index)),
    use_index=True,
    rot=90)
vÇ ["yüzölçüm"].plot (
    ax=altşekil2,
    style="--*", color=Renk.renk(),
    use_index=True,
    rot=90)
vÇ ["yoğunluk"].plot (
    ax=altşekil3,
    style="--o", color=Renk.renk(),
    use_index=True,
    rot=90)
şekil.legend()
mp.show()