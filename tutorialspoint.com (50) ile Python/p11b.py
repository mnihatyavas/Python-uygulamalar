# coding:iso-8859-9 Türkçe
# Python3 - Date & Time

import calendar;
import time;

yıl = int (input ("Yıllık takvim yılını girin: "))
print (calendar.calendar (yıl, w = 2, l = 1, c = 6))

input ("Devam için [Ent]:")
calendar.setfirstweekday (5)
print (calendar.calendar (yıl, w = 2, l = 1, c = 6))

print (yıl, "artık yıl mı?", calendar.isleap (yıl))

print ("1970->2018 arası artık yılların sayısı:", calendar.leapdays (1970, 2018) )
calendar.setfirstweekday (0)

ay = int (input ("Takvim ayını girin [1-12]: "))
print (calendar.month (yıl, ay, w = 2, l = 1) )
print ("Ayın Haftalık Listeleri:\n", calendar.monthcalendar (yıl, ay) )
print ("\nAyın ilk günü endeksi ve ayın toplam gün sayısı:", calendar.monthrange (yıl, ay) )
print ("\nBugün (pazartesinden itibaren) haftanın kaçıncı günü?",
    calendar.weekday (time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_wday) )