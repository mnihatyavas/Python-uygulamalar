# coding:iso-8859-9 Türkçe
# p_13008.py: Güncel tarihten re.search'le SS:dd:ss bulma, verileri ve endekslerini yansıtma örneği.

import re
from datetime import datetime

# dizge = "10 Mart Pazar 15:37:48 EEST 2019" veya aşağıdaki str(..) olabilir...
dizge = str (datetime (1,1,1).now() )

ifade = r"\b(?P<saat>\d\d):(?P<dakika>\d\d):(?P<saniye>\d\d)\b"
# Herbiri "rr:" (çift-rakam:) şeklinde ve referansları saat-dakika-saniye adları olan 3 grup

sonuç = re.search (ifade, dizge)
print ("Tarih içerikli dizgemiz:", dizge)
print ("Saat:", sonuç.group ('saat'), ", Dakika:", sonuç.group ('dakika'), ", Saniye:", sonuç.group ('saniye') )
print ("Saat'ın dizge'deki ilk endeksi:", sonuç.start ("saat"), ", ve son endeksi:", sonuç.end ("saat") )
print ("Dakikanın dizge'deki ilk ve son endeksi:", sonuç.span ("dakika") )
print ("Saniyenin dizge'deki ilk ve son endeksi:", sonuç.span ("saniye") )

"""Çıktı:
>python p_13008.py
Tarih içerikli dizgemiz: 2019-09-14 22:04:39.076561
Saat: 22 , Dakika: 04 , Saniye: 39
Saat'ın dizge'deki ilk endeksi: 11 , ve son endeksi: 13
Dakikanın dizge'deki ilk ve son endeksi: (14, 16)
Saniyenin dizge'deki ilk ve son endeksi: (17, 19)
"""