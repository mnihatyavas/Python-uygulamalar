#coding:iso-8859-9 T�rk�e
# p_32704.py: Dizgeyi strftime, strptime ve parse ile bi�emleme �rne�i.

from datetime import datetime, timedelta
from dateutil.parser import parse

tarih1 = datetime (2019, 8, 12)
tarih1 += timedelta (0, 3661)

print ("Datetime tipli tarih: ", tarih1, type (tarih1),
    "\nDizge tipli tarih: ", str (tarih1), type (str (tarih1)), sep="") # str kullan�m�...
#----------------------------------------------------------------------------------------------------

g�nler = ["Pazar", "Pazartesi", "Sal�", "�ar�amba", "Per�embe", "Cuma", "Cumartesi"]
print ("\nDatetime tarihin bi�emlisi:", tarih1.strftime ("[Gun-Ay-Yil: %d-%m-%Y]") ) # strftime kullan�m�...
print ("K�sa ismen haftan�n g�n�: " + tarih1.strftime ('%a') )
print ("Uzun ismen haftan�n g�n�: " + tarih1.strftime ('%A') )
print ("Rakamen haftan�n g�n�: " + tarih1.strftime ('%w') ) # 0-->6
print ("T�rk�e uzun ismen haftan�n g�n�: " + g�nler [eval (tarih1.strftime ('%w'))] )
#----------------------------------------------------------------------------------------------------

aylar = ["Ocak", "�ubat", "Mart", "Nisan", "May�s", "Haziran", "Temmuz", "A�ustos", "Eyl�l", "Ekim", "Kas�m", "Aral�k"]
print ("\nRakamen ay�n g�n�:", tarih1.strftime ('%d') )
print ("K�sa ismen ay:", tarih1.strftime ('%b') )
print ("Uzun ismen ay:", tarih1.strftime ('%B') )
print ("Rakamen ay:", tarih1.strftime ('%m') ) # 1-->12
if eval (tarih1.strftime ('%m')[0]): ay = eval (tarih1.strftime ('%m')) - 1
else: ay = eval (tarih1.strftime ('%m')[1]) - 1
print ("T�rk�e uzun ismen ay:", aylar [ay] )
print ("-"*42)
#----------------------------------------------------------------------------------------------------

tarih2 = datetime.strptime ("12 Aug 19", "%d %b %y") # %y=19 veya %Y=2019...
print ("\nG�n�n bi�emsiz tarihi: ", tarih2, "\n   Bi�emli tarih: ", tarih2.strftime ("%d-%m-%Y"), sep="") # strptime kullan�m�...

dizge = "2019-08-12T04:43:12"
print ("G�n�n tarih ve zaman�:", datetime.strptime (dizge, "%Y-%m-%dT%H:%M:%S") )

dizge = "17/4/1957 2:03:29 PM"
tarih3 = datetime.strptime (dizge, "%d/%m/%Y %I:%M:%S %p")
print ("Dizgesel tarih: ", dizge, "\n   Bi�emli strptime tarih: ", tarih3, sep="")
print ("-"*46)
#----------------------------------------------------------------------------------------------------

print ("\nDo�rudan parse'la dizgeyi tarihe �evirme:", parse ("Mon Aug 12 05:05:53 2019"))
print ("Dolayl� datetime.strptime'la dizgeyi tarihe �evirme:", datetime.strptime ("Mon Aug 12 05:05:53 2019", "%a %b %d %H:%M:%S %Y") )



"""��kt�:
>python p_32704.py
Datetime tipli tarih: 2019-08-12 01:01:01<class 'datetime.datetime'>
Dizge tipli tarih: 2019-08-12 01:01:01<class 'str'>

Datetime tarihin bi�emlisi: [Gun-Ay-Yil: 12-08-2019]
K�sa ismen haftan�n g�n�: Mon
Uzun ismen haftan�n g�n�: Monday
Rakamen haftan�n g�n�: 1
T�rk�e uzun ismen haftan�n g�n�: Pazartesi

Rakamen ay�n g�n�: 12
K�sa ismen ay: Aug
Uzun ismen ay: August
Rakamen ay: 08
T�rk�e uzun ismen ay: A�ustos
------------------------------------------

G�n�n bi�emsiz tarihi: 2019-08-12 00:00:00
   Bi�emli tarih: 12-08-2019
G�n�n tarih ve zaman�: 2019-08-12 04:43:12
Dizgesel tarih: 17/4/1957 2:03:29 PM
   Bi�emli strptime tarih: 1957-04-17 14:03:29
----------------------------------------------

Do�rudan parse'la dizgeyi tarihe �evirme: 2019-08-12 05:05:53
Dolayl� datetime.strptime'la dizgeyi tarihe �evirme: 2019-08-12 05:05:53
"""