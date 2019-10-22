#coding:iso-8859-9 T�rk�e
# p_32502a.py: Pandas veri �er�evesinin �izgi grafik olarak kullan�lmas� �rne�i.

import matplotlib.pyplot as mp
import pandas as pd

mp.style.use ("dark_background")

�ehirler = {"ad":
    ["Londra", "Berlin", "Madrid", "Roma", "Paris", "Viyana", "Bu�arest",
    "Hamburg", "Budape�te", "Var�ova", "Barselona", "M�nih", "Milano"],
            "n�fus":
    [8615246, 3562166, 3165235, 2874038, 2273305, 1805681, 1803425,
    1760433, 1754000, 1740119, 1602386, 1493900, 1350680],
            "y�z�l��m�":
    [1572, 891.85, 605.77, 1285, 105.4, 414.6, 228,
    755, 525.2, 517, 101.9, 310.4, 181.8] }

veri�er�evesi = pd.DataFrame (�ehirler,
    columns=["n�fus", "y�z�l��m�"],
    index=�ehirler ["ad"] )

print ("�ehirler veri �er�evesi:\n", veri�er�evesi, sep="")

veri�er�evesi ["y�z�l��m�"] *=1000
veri�er�evesi.plot()
mp.show()
#-------------------------------------------------------------------------------------------------------

veri�er�evesi.plot (
    xticks=range (len (veri�er�evesi.index)),
    use_index=True) # X-eksende �ehir adlar� tam yans�yacak...
mp.show() # �ehir adlar� �st-steyse pencereyi tam a�, yada...
#-------------------------------------------------------------------------------------------------------

veri�er�evesi.plot (
    xticks=range (len (veri�er�evesi.index)),
    use_index=True,
    rot=90) # X-eksende �ehir adlar� dikey yans�yacak...
mp.show() # �ehir adlar� alttaysa, Configure-subplots->bottom ayar�n� art�r...
