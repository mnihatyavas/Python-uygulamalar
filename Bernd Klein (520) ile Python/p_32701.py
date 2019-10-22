#coding:iso-8859-9 T�rk�e
# p_32701.py: Mod�l datetime'�n date s�n�f� �rne�i.

from datetime import date

tarih = date (2019, 8, 10)
print ("Girilen tarih:", tarih)
print ("Varsay�l� enk���k tarih:", date.min)
print ("Varsay�l� enb�y�k tarih:", date.max)
print ("1582 Ocak 1 ve verili", tarih, "tarih aras�nda ka� g�n var?", tarih.toordinal() )
print ("1582 Ocak 1'e", tarih.toordinal(), "g�n eklenirse hangi tarihe ula��l�r?", date.fromordinal (tarih.toordinal() ) )
print (tarih, "tarihinin hafta g�n no'su:", tarih.weekday() )
print ("Bug�n�n tarihi:", date.today() )
print ("Verili tarihin g�n, ay ve y�l�:", tarih.day, tarih.month, tarih.year)
print ("Verili tarihin ctime bi�emi:", date (2019, 8, 11).ctime() )



"""��kt�:
>python p_32701.py
Girilen tarih: 2019-08-10
Varsay�l� enk���k tarih: 0001-01-01
Varsay�l� enb�y�k tarih: 9999-12-31
1582 Ocak 1 ve verili 2019-08-10 tarih aras�nda ka� g�n var? 737281
1582 Ocak 1'e 737281 g�n eklenirse hangi tarihe ula��l�r? 2019-08-10
2019-08-10 tarihinin hafta g�n no'su: 5
Bug�n�n tarihi: 2019-08-10
Verili tarihin g�n, ay ve y�l�: 10 8 2019
Verili tarihin ctime bi�emi: Sun Aug 11 00:00:00 2019
"""