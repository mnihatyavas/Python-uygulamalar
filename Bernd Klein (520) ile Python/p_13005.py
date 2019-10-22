# coding:iso-8859-9 T�rk�e
# p_13005.py: re.search ile grup rakamlar ve ":" sonras�n� arama �rne�i.

import re

d�zifade = re.search (r"[0-9]+", "M��teri no: 232454, Tarih: 4 Mart, 2019")
print (d�zifade.group() ) # Enaz 1 ve dahafazla olabilen ilk rakam-lar grubu...
print (d�zifade.span() )
print (d�zifade.start() )
print (d�zifade.end() )
print (d�zifade.span()[0] )
print (d�zifade.span()[1] )

print()
d�zifade = re.search ("([0-9]+).*: (.*)", "M��teri no: 232454, Tarih: 4 Mart, 2019") # Parantezli �oklu gruplar...
print (d�zifade.group() ) # Grup rakamlar ve : sonras�
print (d�zifade.group (1) )
print (d�zifade.group (2) )
try: print (d�zifade.group (3) )
except Exception as ist: print ("Hata:", ist)
print (d�zifade.group (1, 2) )

"""��kt�:
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