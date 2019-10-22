#coding:iso-8859-9 Türkçe
# p_32702.py: Modül datetime'ın time sınıfı örneği.

from datetime import time

zaman = time (00, 1, 23)
print ("Verili zaman:", zaman)
print ("Enküçük zaman:", time.min)
print ("Enbüyük zaman:", time.max)
print (zaman, "zamanın saniye, dakika ve saatı:", zaman.second, zaman.minute, zaman.hour)
zaman = zaman.replace (hour=0, minute=7, second=59)
print ("Değiştirilen zaman:", zaman)



"""Çıktı:
>python p_32702.py
Verili zaman: 00:01:23
Enküçük zaman: 00:00:00
Enbüyük zaman: 23:59:59.999999
00:01:23 zamanın saniye, dakika ve saatı: 23 1 0
Değiştirilen zaman: 00:07:59
"""