#coding:iso-8859-9 T�rk�e
# p_32703.py: Mod�l datetime'�n datetime ve timedelta s�n�f� �rne�i.

from datetime import datetime, timedelta
import pytz

zt = datetime (2019, 8, 11, 0, 26, 45)
print ("Verili zamanl� tarih:", zt)
print ("Verili zamnl� tarih naif/b�n mi?", (zt.tzinfo == None) )

zt2 = datetime.now (pytz.utc)
print ("�imdinin utc'li zamanl� tarihi:", zt2)
print ("Verili zamanl� tarih aware/uyan�k mi?", (zt2.tzinfo != None), (zt2.tzinfo.utcoffset (zt2) != None) )
print ("Evrensel zaman koordinat� ve saat fark�:", zt2.tzinfo, zt2.tzinfo.utcoffset (zt2) )

g�nSay�s� = 5
ilk = datetime (2019, 2, 27)
tarihler = [ilk + timedelta (days=x) for x in range (0, g�nSay�s�)]
print ("\n5 g�nl�k timedelta g�n art���:\n", "-"*30, sep="")
for tarih in tarihler: print (tarih)

ilk = datetime (2019, 1, 2)
tarihler = [ilk - timedelta (days=x) for x in range (0, g�nSay�s�)]
print ("\n5 g�nl�k timedelta g�n azal���:\n", "-"*31, sep="")
for tarih in tarihler: print (tarih)
print ("-"*59)
#-----------------------------------------------------------------------------------------------------

g�nFark� = datetime (2019, 8,12, 3, 8, 45) - datetime (1959, 4, 17, 14, 30)
print ("\nYa� ve g�n say�s� kar��l���: ", (2019 - 1957), " y�l ve ", g�nFark�, sep="")
print ("Ya�'�n g�n say�s� ve saniye artan�:", g�nFark�.days, g�nFark�.seconds)
print ("-"*59)
#-----------------------------------------------------------------------------------------------------

tarih1 = datetime (1957, 4, 17)
tarih2 = tarih1 + timedelta (300) # 300 g�n sonras�...
tarih3 = tarih1 - timedelta (300) # 300 g�n �ncesi...
tarih4 = tarih1 + 3.14 * timedelta (300) # 3.14*300=942 g�n ilavesi...
tarih5 = tarih2 + timedelta (0, 3661)
print ("\nVerilen tarih: ", tarih1,
    "\n300 g�n sonras�: ", tarih2,
    "\n300 g�n ve 3661 saniye sonras�: ", tarih5,
    "\n300 g�n �ncesi: ", tarih3,
    "\n3.14 * 300 g�n sonras�: ", tarih4,
    "\nSon eklenen tarihin g�n fark�: ", (tarih4 - tarih1), sep="")



"""��kt�:
>python p_32703.py
Verili zamanl� tarih: 2019-08-11 00:26:45
Verili zamnl� tarih naif/b�n mi? True
�imdinin utc'li zamanl� tarihi: 2019-08-12 00:40:17.717456+00:00
Verili zamanl� tarih aware/uyan�k mi? True True
Evrensel zaman koordinat� ve saat fark�: UTC 0:00:00

5 g�nl�k timedelta g�n art���:
------------------------------
2019-02-27 00:00:00
2019-02-28 00:00:00
2019-03-01 00:00:00
2019-03-02 00:00:00
2019-03-03 00:00:00

5 g�nl�k timedelta g�n azal���:
-------------------------------
2019-01-02 00:00:00
2019-01-01 00:00:00
2018-12-31 00:00:00
2018-12-30 00:00:00
2018-12-29 00:00:00
-----------------------------------------------------------

Ya� ve g�n say�s� kar��l���: 62 y�l ve 22031 days, 12:38:45
Ya�'�n g�n say�s� ve saniye artan�: 22031 45525
-----------------------------------------------------------

Verilen tarih: 1957-04-17 00:00:00
300 g�n sonras�: 1958-02-11 00:00:00
300 g�n ve 3661 saniye sonras�: 1958-02-11 01:01:01
300 g�n �ncesi: 1956-06-21 00:00:00
3.14 * 300 g�n sonras�: 1959-11-15 00:00:00
Son eklenen tarihin g�n fark�: 942 days, 0:00:00
"""