# coding:iso-8859-9 T�rk�e

import re

# �rnekteki D�zenli�fade=RegularExpression=re mod�l metodu t�m rakaml� �S�A kelimeleri yerine "***" koyar...
# sub-stitute (r-aw"kal�p", "de�i�tir", "dizge") #raw'da esc=\ etkisizdir

print (re.sub (r"([�S�A])(\d+)", "***", "�nce �1957y�l�04ay�17g�n�, Sonra S2018, �st �1512bug�n ve Alt A1704") )
