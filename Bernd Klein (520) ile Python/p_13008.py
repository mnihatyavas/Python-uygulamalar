# coding:iso-8859-9 T�rk�e
# p_13008.py: G�ncel tarihten re.search'le SS:dd:ss bulma, verileri ve endekslerini yans�tma �rne�i.

import re
from datetime import datetime

# dizge = "10 Mart Pazar 15:37:48 EEST 2019" veya a�a��daki str(..) olabilir...
dizge = str (datetime (1,1,1).now() )

ifade = r"\b(?P<saat>\d\d):(?P<dakika>\d\d):(?P<saniye>\d\d)\b"
# Herbiri "rr:" (�ift-rakam:) �eklinde ve referanslar� saat-dakika-saniye adlar� olan 3 grup

sonu� = re.search (ifade, dizge)
print ("Tarih i�erikli dizgemiz:", dizge)
print ("Saat:", sonu�.group ('saat'), ", Dakika:", sonu�.group ('dakika'), ", Saniye:", sonu�.group ('saniye') )
print ("Saat'�n dizge'deki ilk endeksi:", sonu�.start ("saat"), ", ve son endeksi:", sonu�.end ("saat") )
print ("Dakikan�n dizge'deki ilk ve son endeksi:", sonu�.span ("dakika") )
print ("Saniyenin dizge'deki ilk ve son endeksi:", sonu�.span ("saniye") )

"""��kt�:
>python p_13008.py
Tarih i�erikli dizgemiz: 2019-09-14 22:04:39.076561
Saat: 22 , Dakika: 04 , Saniye: 39
Saat'�n dizge'deki ilk endeksi: 11 , ve son endeksi: 13
Dakikan�n dizge'deki ilk ve son endeksi: (14, 16)
Saniyenin dizge'deki ilk ve son endeksi: (17, 19)
"""