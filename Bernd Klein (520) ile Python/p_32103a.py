#coding: iso-8859-9 Türkçe
# p_32103a.py: Veri çerçevelerinin yeniden-endekslenmesi örneği.

import pandas as pd

endeks = ['Firefox', 'Chrome', 'Safari', 'IE10', 'Konqueror', "Maxthon"]
veriÇerçevesi = pd.DataFrame ( {
    'http Statüsü': [200, 200, 404, 404, 301, 250],
    'Tepki Süresi': [0.04, 0.02, 0.07, 0.08, 1.0, 0.03] },
    index=endeks)
print ("Tarayıcıların orijinal veri çerçevesi:\n", veriÇerçevesi, sep="")

yeniEndeks = ['Safari', 'Iceweasel', 'Comodo Dragon', 'IE10', "Apple", 'Chrome']
vç2 = veriÇerçevesi.reindex (yeniEndeks)
print ("\nTarayıcıların namevcut=NaN'lı YENİ veri çerçevesi:\n", vç2, sep="")

vç3 = veriÇerçevesi.reindex (yeniEndeks, fill_value=0) # NaN fill_value=0 olmuyor, oluyor...
print ("\nTarayıcıların namevcut=0'lı YENİ veri çerçevesi:\n", vç3, sep="")



"""Çıktı:
>python p_32103a.py
Tarayıcıların orijinal veri çerçevesi:
           http Statüsü  Tepki Süresi
Firefox             200          0.04
Chrome              200          0.02
Safari              404          0.07
IE10                404          0.08
Konqueror           301          1.00
Maxthon             250          0.03

Tarayıcıların namevcut=NaN'lı YENİ veri çerçevesi:
               http Statüsü  Tepki Süresi
Safari                404.0          0.07
Iceweasel               NaN           NaN
Comodo Dragon           NaN           NaN
IE10                  404.0          0.08
Apple                   NaN           NaN
Chrome                200.0          0.02

Tarayıcıların namevcut=0'lı YENİ veri çerçevesi:
               http Statüsü  Tepki Süresi
Safari                  404          0.07
Iceweasel                 0          0.00
Comodo Dragon             0          0.00
IE10                    404          0.08
Apple                     0          0.00
Chrome                  200          0.02
"""