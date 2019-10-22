#coding:iso-8859-9 Türkçe
# p_32703.py: Modül datetime'ın datetime ve timedelta sınıfı örneği.

from datetime import datetime, timedelta
import pytz

zt = datetime (2019, 8, 11, 0, 26, 45)
print ("Verili zamanlı tarih:", zt)
print ("Verili zamnlı tarih naif/bön mi?", (zt.tzinfo == None) )

zt2 = datetime.now (pytz.utc)
print ("Şimdinin utc'li zamanlı tarihi:", zt2)
print ("Verili zamanlı tarih aware/uyanık mi?", (zt2.tzinfo != None), (zt2.tzinfo.utcoffset (zt2) != None) )
print ("Evrensel zaman koordinatı ve saat farkı:", zt2.tzinfo, zt2.tzinfo.utcoffset (zt2) )

günSayısı = 5
ilk = datetime (2019, 2, 27)
tarihler = [ilk + timedelta (days=x) for x in range (0, günSayısı)]
print ("\n5 günlük timedelta gün artışı:\n", "-"*30, sep="")
for tarih in tarihler: print (tarih)

ilk = datetime (2019, 1, 2)
tarihler = [ilk - timedelta (days=x) for x in range (0, günSayısı)]
print ("\n5 günlük timedelta gün azalışı:\n", "-"*31, sep="")
for tarih in tarihler: print (tarih)
print ("-"*59)
#-----------------------------------------------------------------------------------------------------

günFarkı = datetime (2019, 8,12, 3, 8, 45) - datetime (1959, 4, 17, 14, 30)
print ("\nYaş ve gün sayısı karşılığı: ", (2019 - 1957), " yıl ve ", günFarkı, sep="")
print ("Yaş'ın gün sayısı ve saniye artanı:", günFarkı.days, günFarkı.seconds)
print ("-"*59)
#-----------------------------------------------------------------------------------------------------

tarih1 = datetime (1957, 4, 17)
tarih2 = tarih1 + timedelta (300) # 300 gün sonrası...
tarih3 = tarih1 - timedelta (300) # 300 gün öncesi...
tarih4 = tarih1 + 3.14 * timedelta (300) # 3.14*300=942 gün ilavesi...
tarih5 = tarih2 + timedelta (0, 3661)
print ("\nVerilen tarih: ", tarih1,
    "\n300 gün sonrası: ", tarih2,
    "\n300 gün ve 3661 saniye sonrası: ", tarih5,
    "\n300 gün öncesi: ", tarih3,
    "\n3.14 * 300 gün sonrası: ", tarih4,
    "\nSon eklenen tarihin gün farkı: ", (tarih4 - tarih1), sep="")



"""Çıktı:
>python p_32703.py
Verili zamanlı tarih: 2019-08-11 00:26:45
Verili zamnlı tarih naif/bön mi? True
Şimdinin utc'li zamanlı tarihi: 2019-08-12 00:40:17.717456+00:00
Verili zamanlı tarih aware/uyanık mi? True True
Evrensel zaman koordinatı ve saat farkı: UTC 0:00:00

5 günlük timedelta gün artışı:
------------------------------
2019-02-27 00:00:00
2019-02-28 00:00:00
2019-03-01 00:00:00
2019-03-02 00:00:00
2019-03-03 00:00:00

5 günlük timedelta gün azalışı:
-------------------------------
2019-01-02 00:00:00
2019-01-01 00:00:00
2018-12-31 00:00:00
2018-12-30 00:00:00
2018-12-29 00:00:00
-----------------------------------------------------------

Yaş ve gün sayısı karşılığı: 62 yıl ve 22031 days, 12:38:45
Yaş'ın gün sayısı ve saniye artanı: 22031 45525
-----------------------------------------------------------

Verilen tarih: 1957-04-17 00:00:00
300 gün sonrası: 1958-02-11 00:00:00
300 gün ve 3661 saniye sonrası: 1958-02-11 01:01:01
300 gün öncesi: 1956-06-21 00:00:00
3.14 * 300 gün sonrası: 1959-11-15 00:00:00
Son eklenen tarihin gün farkı: 942 days, 0:00:00
"""