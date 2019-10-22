# coding:iso-8859-9 Türkçe

from time import time, sleep
from datetime import datetime
from random import randint, random

sayı = randint (0, 10**7)
print ("Azami 10 sn bekle")

ilk = time()
for i in range (sayı): sayı +=1
print ('\nİşlem süresi:', round (time() - ilk, 3), "saniye'dir.")

try: bekle = abs (eval (input ("\nKaç saniye bekleyelim: ")))
except Exception: bekle = randint (0, 20) + random()
if bekle > 20: bekle = 20
sleep (bekle)
print ("{:.3f} saniye bekledik." .format (bekle) )

zaman = int (time() )
gün = zaman // 86400
yıl = gün // 365
artıkGün = gün - yıl*365 - (2018-1970) // 4 - 2
saat =  ((zaman % 86400 // 3600) + 3) % 24 # 3 saatlık saat dilimi telefisi
dakika = zaman % 3600 // 60
saniye = zaman % 60
print ("\n1.1.1970'den beri geçen süre {} yıl, {} gün, {} artık gün, {} saat, {} dakika ve {} saniyedir."\
        .format (yıl, gün, artıkGün, saat, dakika, saniye) )

tarih = datetime (1,1,1).now()
print ("\nŞimdiki standart tarih ve zaman:", tarih)
print ("Biçimlediğimiz zaman ve tarih-1: [{}:{:02d}:{:02d}, {}/{}/{}]"\
        .format (tarih.hour, tarih.minute, tarih.second, tarih.day, tarih.month, tarih.year) )
am_pm = 'AM' if tarih.hour < 12 else 'PM'
print ("Biçimlediğimiz zaman ve tarih-2: [{}:{:02d}:{:02d} {}, {}/{}/{}]"\
        .format (tarih.hour%12, tarih.minute, tarih.second, am_pm, tarih.day, tarih.month, tarih.year) )

"""strftime fonksiyonundaki kodla biçimlenen tarih ve zaman
%c -->Yerel biçimlenen tarih ve zaman
%x, %X -->%c ile biçimli tarih ve zaman
%d -->Ayın günü
%j -->Yılın (artık) günü
%a, %A -->Kısa ve uzun haftanın gün adı
%m -->(01-12) ay rakamı
%b, %B -->Kısa ve uzun ay adı
%y, %Y -->2 ve 4 rakamlı yıl
%H, %I -->24 ve 12 saat değeri
%M -->Dakika değeri
%S -->Saniye değeri
%p -->am veya pm
"""

print ("\nGünadı ve tarih-1:", tarih.strftime ('%A %x') )
print ("Tarih ve zaman-2.:", tarih.strftime ('%c') )
print ("Tarih ve zaman-3.:", tarih.strftime ("%Y yilinin %B ayinin %d'i %A ve saat %I:%M:%S %p") ) # strftime UTF-8 dışı açıklamayı kabul etmiyor...
print ("Tarih ve zaman-4.:", tarih.strftime ('{}:%M:%S %p %B {} %A').format (tarih.hour%12, tarih.day))

tarih1 = datetime (2018,12,14) # Yıl, ay, gün; saat, dakika, saniye, 999999 rakam
tarih2 = datetime (1957, 4, 17, 14, 35, 42, 234976)
print ("\nYarattığımız tarih nesnesi-1:", tarih1)
print ("Yarattığımız tarih nesnesi-2:", tarih2)
print ("2 tarih arasından geçen süre:", tarih1-tarih2)