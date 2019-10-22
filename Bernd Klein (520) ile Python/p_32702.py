#coding:iso-8859-9 T�rk�e
# p_32702.py: Mod�l datetime'�n time s�n�f� �rne�i.

from datetime import time

zaman = time (00, 1, 23)
print ("Verili zaman:", zaman)
print ("Enk���k zaman:", time.min)
print ("Enb�y�k zaman:", time.max)
print (zaman, "zaman�n saniye, dakika ve saat�:", zaman.second, zaman.minute, zaman.hour)
zaman = zaman.replace (hour=0, minute=7, second=59)
print ("De�i�tirilen zaman:", zaman)



"""��kt�:
>python p_32702.py
Verili zaman: 00:01:23
Enk���k zaman: 00:00:00
Enb�y�k zaman: 23:59:59.999999
00:01:23 zaman�n saniye, dakika ve saat�: 23 1 0
De�i�tirilen zaman: 00:07:59
"""