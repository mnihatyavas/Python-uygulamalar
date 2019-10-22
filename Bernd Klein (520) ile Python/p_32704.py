#coding:iso-8859-9 Türkçe
# p_32704.py: Dizgeyi strftime, strptime ve parse ile biçemleme örneği.

from datetime import datetime, timedelta
from dateutil.parser import parse

tarih1 = datetime (2019, 8, 12)
tarih1 += timedelta (0, 3661)

print ("Datetime tipli tarih: ", tarih1, type (tarih1),
    "\nDizge tipli tarih: ", str (tarih1), type (str (tarih1)), sep="") # str kullanımı...
#----------------------------------------------------------------------------------------------------

günler = ["Pazar", "Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi"]
print ("\nDatetime tarihin biçemlisi:", tarih1.strftime ("[Gun-Ay-Yil: %d-%m-%Y]") ) # strftime kullanımı...
print ("Kısa ismen haftanın günü: " + tarih1.strftime ('%a') )
print ("Uzun ismen haftanın günü: " + tarih1.strftime ('%A') )
print ("Rakamen haftanın günü: " + tarih1.strftime ('%w') ) # 0-->6
print ("Türkçe uzun ismen haftanın günü: " + günler [eval (tarih1.strftime ('%w'))] )
#----------------------------------------------------------------------------------------------------

aylar = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
print ("\nRakamen ayın günü:", tarih1.strftime ('%d') )
print ("Kısa ismen ay:", tarih1.strftime ('%b') )
print ("Uzun ismen ay:", tarih1.strftime ('%B') )
print ("Rakamen ay:", tarih1.strftime ('%m') ) # 1-->12
if eval (tarih1.strftime ('%m')[0]): ay = eval (tarih1.strftime ('%m')) - 1
else: ay = eval (tarih1.strftime ('%m')[1]) - 1
print ("Türkçe uzun ismen ay:", aylar [ay] )
print ("-"*42)
#----------------------------------------------------------------------------------------------------

tarih2 = datetime.strptime ("12 Aug 19", "%d %b %y") # %y=19 veya %Y=2019...
print ("\nGünün biçemsiz tarihi: ", tarih2, "\n   Biçemli tarih: ", tarih2.strftime ("%d-%m-%Y"), sep="") # strptime kullanımı...

dizge = "2019-08-12T04:43:12"
print ("Günün tarih ve zamanı:", datetime.strptime (dizge, "%Y-%m-%dT%H:%M:%S") )

dizge = "17/4/1957 2:03:29 PM"
tarih3 = datetime.strptime (dizge, "%d/%m/%Y %I:%M:%S %p")
print ("Dizgesel tarih: ", dizge, "\n   Biçemli strptime tarih: ", tarih3, sep="")
print ("-"*46)
#----------------------------------------------------------------------------------------------------

print ("\nDoğrudan parse'la dizgeyi tarihe çevirme:", parse ("Mon Aug 12 05:05:53 2019"))
print ("Dolaylı datetime.strptime'la dizgeyi tarihe çevirme:", datetime.strptime ("Mon Aug 12 05:05:53 2019", "%a %b %d %H:%M:%S %Y") )



"""Çıktı:
>python p_32704.py
Datetime tipli tarih: 2019-08-12 01:01:01<class 'datetime.datetime'>
Dizge tipli tarih: 2019-08-12 01:01:01<class 'str'>

Datetime tarihin biçemlisi: [Gun-Ay-Yil: 12-08-2019]
Kısa ismen haftanın günü: Mon
Uzun ismen haftanın günü: Monday
Rakamen haftanın günü: 1
Türkçe uzun ismen haftanın günü: Pazartesi

Rakamen ayın günü: 12
Kısa ismen ay: Aug
Uzun ismen ay: August
Rakamen ay: 08
Türkçe uzun ismen ay: Ağustos
------------------------------------------

Günün biçemsiz tarihi: 2019-08-12 00:00:00
   Biçemli tarih: 12-08-2019
Günün tarih ve zamanı: 2019-08-12 04:43:12
Dizgesel tarih: 17/4/1957 2:03:29 PM
   Biçemli strptime tarih: 1957-04-17 14:03:29
----------------------------------------------

Doğrudan parse'la dizgeyi tarihe çevirme: 2019-08-12 05:05:53
Dolaylı datetime.strptime'la dizgeyi tarihe çevirme: 2019-08-12 05:05:53
"""