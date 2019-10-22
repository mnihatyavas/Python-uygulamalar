#coding:iso-8859-9 Türkçe
# p_32701.py: Modül datetime'ın date sınıfı örneği.

from datetime import date

tarih = date (2019, 8, 10)
print ("Girilen tarih:", tarih)
print ("Varsayılı enküçük tarih:", date.min)
print ("Varsayılı enbüyük tarih:", date.max)
print ("1582 Ocak 1 ve verili", tarih, "tarih arasında kaç gün var?", tarih.toordinal() )
print ("1582 Ocak 1'e", tarih.toordinal(), "gün eklenirse hangi tarihe ulaşılır?", date.fromordinal (tarih.toordinal() ) )
print (tarih, "tarihinin hafta gün no'su:", tarih.weekday() )
print ("Bugünün tarihi:", date.today() )
print ("Verili tarihin gün, ay ve yılı:", tarih.day, tarih.month, tarih.year)
print ("Verili tarihin ctime biçemi:", date (2019, 8, 11).ctime() )



"""Çıktı:
>python p_32701.py
Girilen tarih: 2019-08-10
Varsayılı enküçük tarih: 0001-01-01
Varsayılı enbüyük tarih: 9999-12-31
1582 Ocak 1 ve verili 2019-08-10 tarih arasında kaç gün var? 737281
1582 Ocak 1'e 737281 gün eklenirse hangi tarihe ulaşılır? 2019-08-10
2019-08-10 tarihinin hafta gün no'su: 5
Bugünün tarihi: 2019-08-10
Verili tarihin gün, ay ve yılı: 10 8 2019
Verili tarihin ctime biçemi: Sun Aug 11 00:00:00 2019
"""