# coding:iso-8859-9 T�rk�e
# Python3 - Date & Time

import calendar;
import time;

y�l = int (input ("Y�ll�k takvim y�l�n� girin: "))
print (calendar.calendar (y�l, w = 2, l = 1, c = 6))

input ("Devam i�in [Ent]:")
calendar.setfirstweekday (5)
print (calendar.calendar (y�l, w = 2, l = 1, c = 6))

print (y�l, "art�k y�l m�?", calendar.isleap (y�l))

print ("1970->2018 aras� art�k y�llar�n say�s�:", calendar.leapdays (1970, 2018) )
calendar.setfirstweekday (0)

ay = int (input ("Takvim ay�n� girin [1-12]: "))
print (calendar.month (y�l, ay, w = 2, l = 1) )
print ("Ay�n Haftal�k Listeleri:\n", calendar.monthcalendar (y�l, ay) )
print ("\nAy�n ilk g�n� endeksi ve ay�n toplam g�n say�s�:", calendar.monthrange (y�l, ay) )
print ("\nBug�n (pazartesinden itibaren) haftan�n ka��nc� g�n�?",
    calendar.weekday (time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_wday) )