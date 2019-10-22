# coding:iso-8859-9 T�rk�e

from time import time, sleep
from datetime import datetime
from random import randint, random

say� = randint (0, 10**7)
print ("Azami 10 sn bekle")

ilk = time()
for i in range (say�): say� +=1
print ('\n��lem s�resi:', round (time() - ilk, 3), "saniye'dir.")

try: bekle = abs (eval (input ("\nKa� saniye bekleyelim: ")))
except Exception: bekle = randint (0, 20) + random()
if bekle > 20: bekle = 20
sleep (bekle)
print ("{:.3f} saniye bekledik." .format (bekle) )

zaman = int (time() )
g�n = zaman // 86400
y�l = g�n // 365
art�kG�n = g�n - y�l*365 - (2018-1970) // 4 - 2
saat =  ((zaman % 86400 // 3600) + 3) % 24 # 3 saatl�k saat dilimi telefisi
dakika = zaman % 3600 // 60
saniye = zaman % 60
print ("\n1.1.1970'den beri ge�en s�re {} y�l, {} g�n, {} art�k g�n, {} saat, {} dakika ve {} saniyedir."\
        .format (y�l, g�n, art�kG�n, saat, dakika, saniye) )

tarih = datetime (1,1,1).now()
print ("\n�imdiki standart tarih ve zaman:", tarih)
print ("Bi�imledi�imiz zaman ve tarih-1: [{}:{:02d}:{:02d}, {}/{}/{}]"\
        .format (tarih.hour, tarih.minute, tarih.second, tarih.day, tarih.month, tarih.year) )
am_pm = 'AM' if tarih.hour < 12 else 'PM'
print ("Bi�imledi�imiz zaman ve tarih-2: [{}:{:02d}:{:02d} {}, {}/{}/{}]"\
        .format (tarih.hour%12, tarih.minute, tarih.second, am_pm, tarih.day, tarih.month, tarih.year) )

"""strftime fonksiyonundaki kodla bi�imlenen tarih ve zaman
%c -->Yerel bi�imlenen tarih ve zaman
%x, %X -->%c ile bi�imli tarih ve zaman
%d -->Ay�n g�n�
%j -->Y�l�n (art�k) g�n�
%a, %A -->K�sa ve uzun haftan�n g�n ad�
%m -->(01-12) ay rakam�
%b, %B -->K�sa ve uzun ay ad�
%y, %Y -->2 ve 4 rakaml� y�l
%H, %I -->24 ve 12 saat de�eri
%M -->Dakika de�eri
%S -->Saniye de�eri
%p -->am veya pm
"""

print ("\nG�nad� ve tarih-1:", tarih.strftime ('%A %x') )
print ("Tarih ve zaman-2.:", tarih.strftime ('%c') )
print ("Tarih ve zaman-3.:", tarih.strftime ("%Y yilinin %B ayinin %d'i %A ve saat %I:%M:%S %p") ) # strftime UTF-8 d��� a��klamay� kabul etmiyor...
print ("Tarih ve zaman-4.:", tarih.strftime ('{}:%M:%S %p %B {} %A').format (tarih.hour%12, tarih.day))

tarih1 = datetime (2018,12,14) # Y�l, ay, g�n; saat, dakika, saniye, 999999 rakam
tarih2 = datetime (1957, 4, 17, 14, 35, 42, 234976)
print ("\nYaratt���m�z tarih nesnesi-1:", tarih1)
print ("Yaratt���m�z tarih nesnesi-2:", tarih2)
print ("2 tarih aras�ndan ge�en s�re:", tarih1-tarih2)