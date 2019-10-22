# coding:iso-8859-9 Türkçe
# p_13005.py: re.search ile grup rakamlar ve ":" sonrasını arama örneği.

import re

düzifade = re.search (r"[0-9]+", "Müşteri no: 232454, Tarih: 4 Mart, 2019")
print (düzifade.group() ) # Enaz 1 ve dahafazla olabilen ilk rakam-lar grubu...
print (düzifade.span() )
print (düzifade.start() )
print (düzifade.end() )
print (düzifade.span()[0] )
print (düzifade.span()[1] )

print()
düzifade = re.search ("([0-9]+).*: (.*)", "Müşteri no: 232454, Tarih: 4 Mart, 2019") # Parantezli çoklu gruplar...
print (düzifade.group() ) # Grup rakamlar ve : sonrası
print (düzifade.group (1) )
print (düzifade.group (2) )
try: print (düzifade.group (3) )
except Exception as ist: print ("Hata:", ist)
print (düzifade.group (1, 2) )

"""Çıktı:
>python p_13005.py
232454
(12, 18)
12
18
12
18

232454, Tarih: 4 Mart, 2019
232454
4 Mart, 2019
Hata: no such group
('232454', '4 Mart, 2019')
"""