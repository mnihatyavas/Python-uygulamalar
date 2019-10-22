#coding:iso-8859-9 Türkçe
# p_32502b.py: Pandas veri çerçevesi grafiğinde çift eksen kullanılması örneği.

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

print ("Şehirler veri çerçevesi:\n", vÇ, sep="")

şekil = mp.figure()
şekil.set_facecolor (Renk.renk() )
şekil.suptitle ("Şehirlerin İstatistikleri")

altşekil1 = şekil.subplots()
altşekil1.set_ylabel ("Nüfus")
altşekil1.set_xlabel ("Şehirler")
altşekil1.set_facecolor (Renk.renk() )

altşekil2 = altşekil1.twinx()
altşekil2.set_ylabel ("Yüzölçümü")

vÇ ["nüfus"].plot (
    ax=altşekil1,
    style="-", color=Renk.renk(),
    xticks=range (len (vÇ.index)),
    use_index=True,
    rot=90)
vÇ ["yüzölçüm"].plot (
    ax=altşekil2,
    style="--", color=Renk.renk(),
    use_index=True,
    rot=90)
şekil.legend()
mp.show()
#-------------------------------------------------------------------------------------------------------

mp.style.use ("dark_background")
altşekil1= vÇ ["nüfus"].plot (style="-", color=Renk.renk(),
                                   xticks=range (len (vÇ.index)),
                                   use_index=True, 
                                   rot=90)
altşekil2 = altşekil1.twinx()
vÇ["yüzölçüm"].plot (ax=altşekil2,
                        style="-", color=Renk.renk(),
                        use_index=True,
                        rot=90)
altşekil1.legend (loc = (.7,.9), frameon = False)
altşekil2.legend ( loc = (.7, .85), frameon = False)
altşekil1.set_facecolor (Renk.renk() )
mp.show()



"""Çıktı:
>python p_32502b.py
Şehirler veri çerçevesi:
             nüfus  yüzölçüm
Londra     8615246   1572.00
Berlin     3562166    891.85
Madrid     3165235    605.77
Roma       2874038   1285.00
Paris      2273305    105.40
Viyana     1805681    414.60
Buçarest   1803425    228.00
Hamburg    1760433    755.00
Budapeşte  1754000    525.20
Varşova    1740119    517.00
Barselona  1602386    101.90
Münih      1493900    310.40
Milano     1350680    181.80
"""