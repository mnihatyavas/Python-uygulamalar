#coding: iso-8859-9 T�rk�e
# p_32103a.py: Veri �er�evelerinin yeniden-endekslenmesi �rne�i.

import pandas as pd

endeks = ['Firefox', 'Chrome', 'Safari', 'IE10', 'Konqueror', "Maxthon"]
veri�er�evesi = pd.DataFrame ( {
    'http Stat�s�': [200, 200, 404, 404, 301, 250],
    'Tepki S�resi': [0.04, 0.02, 0.07, 0.08, 1.0, 0.03] },
    index=endeks)
print ("Taray�c�lar�n orijinal veri �er�evesi:\n", veri�er�evesi, sep="")

yeniEndeks = ['Safari', 'Iceweasel', 'Comodo Dragon', 'IE10', "Apple", 'Chrome']
v�2 = veri�er�evesi.reindex (yeniEndeks)
print ("\nTaray�c�lar�n namevcut=NaN'l� YEN� veri �er�evesi:\n", v�2, sep="")

v�3 = veri�er�evesi.reindex (yeniEndeks, fill_value=0) # NaN fill_value=0 olmuyor, oluyor...
print ("\nTaray�c�lar�n namevcut=0'l� YEN� veri �er�evesi:\n", v�3, sep="")



"""��kt�:
>python p_32103a.py
Taray�c�lar�n orijinal veri �er�evesi:
           http Stat�s�  Tepki S�resi
Firefox             200          0.04
Chrome              200          0.02
Safari              404          0.07
IE10                404          0.08
Konqueror           301          1.00
Maxthon             250          0.03

Taray�c�lar�n namevcut=NaN'l� YEN� veri �er�evesi:
               http Stat�s�  Tepki S�resi
Safari                404.0          0.07
Iceweasel               NaN           NaN
Comodo Dragon           NaN           NaN
IE10                  404.0          0.08
Apple                   NaN           NaN
Chrome                200.0          0.02

Taray�c�lar�n namevcut=0'l� YEN� veri �er�evesi:
               http Stat�s�  Tepki S�resi
Safari                  404          0.07
Iceweasel                 0          0.00
Comodo Dragon             0          0.00
IE10                    404          0.08
Apple                     0          0.00
Chrome                  200          0.02
"""