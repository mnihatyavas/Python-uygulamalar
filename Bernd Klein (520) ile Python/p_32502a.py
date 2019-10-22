#coding:iso-8859-9 Türkçe
# p_32502a.py: Pandas veri çerçevesinin çizgi grafik olarak kullanılması örneği.

import matplotlib.pyplot as mp
import pandas as pd

mp.style.use ("dark_background")

şehirler = {"ad":
    ["Londra", "Berlin", "Madrid", "Roma", "Paris", "Viyana", "Buçarest",
    "Hamburg", "Budapeşte", "Varşova", "Barselona", "Münih", "Milano"],
            "nüfus":
    [8615246, 3562166, 3165235, 2874038, 2273305, 1805681, 1803425,
    1760433, 1754000, 1740119, 1602386, 1493900, 1350680],
            "yüzölçümü":
    [1572, 891.85, 605.77, 1285, 105.4, 414.6, 228,
    755, 525.2, 517, 101.9, 310.4, 181.8] }

veriÇerçevesi = pd.DataFrame (şehirler,
    columns=["nüfus", "yüzölçümü"],
    index=şehirler ["ad"] )

print ("Şehirler veri çerçevesi:\n", veriÇerçevesi, sep="")

veriÇerçevesi ["yüzölçümü"] *=1000
veriÇerçevesi.plot()
mp.show()
#-------------------------------------------------------------------------------------------------------

veriÇerçevesi.plot (
    xticks=range (len (veriÇerçevesi.index)),
    use_index=True) # X-eksende şehir adları tam yansıyacak...
mp.show() # Şehir adları üst-steyse pencereyi tam aç, yada...
#-------------------------------------------------------------------------------------------------------

veriÇerçevesi.plot (
    xticks=range (len (veriÇerçevesi.index)),
    use_index=True,
    rot=90) # X-eksende şehir adları dikey yansıyacak...
mp.show() # Şehir adları alttaysa, Configure-subplots->bottom ayarını artır...
