# coding:iso-8859-9 T�rk�e

import re
from datetime import datetime

S = {'oca':'1', '�ub':'2', 'mar':'3', 'nis':'4', 'may':'5', 'haz':'6',
        'tem':'7', 'a�u':'8', 'eyl':'9', 'eki':'10', 'kas':'11', 'ara':'12'}

print ("G�n�n tarih ve zaman�:", datetime (1,1,1).now())
tarih = input ("\nBir tarih girin [ayad�. 99, 9999]: ")

uyan = re.match ("([A-Za-z������������]+)\.?\s* (\d{1,2}),?\s* (\d{4})", tarih)

print ("\nGirdi�iniz tarih: <<{}/{}/{}>>" .format (uyan.group (2), S[uyan.group (1).lower()[:3]], uyan.group (3)[-2:]) )
