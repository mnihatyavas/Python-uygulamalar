# coding:iso-8859-9 T�rk�e

import calendar
from random import randint

aylar = ["Ocak", "�ubat", "Mart", "Nisan", "May�s", "Haziran", "Temmuz", "A�ustos", "Eyl�l", "Ekim", "Kas�m", "Aral�k"]
g�nler1 = ["Pt", "Sa", "�a", "Pe", "Cu", "Ct", "Pa"]
g�nler2 = ["Pazartesi", "Sal�", "�ar�amba", "Per�embe", "Cuma", "Cumartesi", "Pazar"]

try: y�l = int (eval (input ("Takvim tamsay� y�l�n� girin: ")))
except Exception: y�l = 2018

try: ay = int (eval (input ("Takvim tamsay� ay�n� [1-12] girin: ")))
except Exception: ay = randint (1, 12)
if 12 < ay < 1: ay = randint (1, 12)

try: g�n = int (eval (input ("Takvim tamsay� haftan�n g�n�n� [1:Pzt-7:Pz] girin: ")))
except Exception: g�n = randint (1, 7)
if 7 < g�n < 1: g�n = randint (1, 7)
print ("\n<", y�l, ">y�l�n�n <", aylar[ay-1], "> ay� takvimi:\n", "-"*36, sep="" )
ayl�kMetinTakvimi = calendar.TextCalendar (g�n-1) # calendar.MONDAY == 1
ayl�kHtmlTakvimi = calendar.HTMLCalendar (g�n-1)
dosya = open ("mny1.html", "w")
dizge = ayl�kMetinTakvimi.formatmonth (y�l, ay)
print (dizge) # Ay'l�k takvimleri haz�r formatl� bir b�t�n olarak yazar...
print (ayl�kHtmlTakvimi.formatmonth (y�l, ay), file=dosya)
dosya.close()
print ("HTML formatl� takvim i�in mny1.html dosyas�n� i�letin")
#----------------------------------------------------------------------------------------

print ("\nS�f�rlar ilk PAZARTES�'nden �nceki ve aysonu haftas� tamamlayanlar�d�r.\n", "-"*71, sep="")
print (" " * ((20 - (len (aylar[ay-1]) + len (str (y�l)) + 2 )) // 2 ), aylar[ay-1], y�l)
i = g�n-1
while True:
    print (g�nler1 [i], end=" ")
    i +=1
    if i >= 7: i = 0
    if i == g�n-1: break
print ()
j = 0
for i in ayl�kMetinTakvimi.itermonthdays (y�l, ay):
    j +=1
    print ("{:2d}" .format (i), end=" ") # Ay'�n g�nler1i belirledi�imiz formatla tek tek yazd�r�l�r...
    if j%7 == 0: print()
#----------------------------------------------------------------------------------------

i = 0
print ("\nAy Adlar� (�ngilizce ve T�rk�e):\n", "-"*32, sep="")
for ayAd� in calendar.month_name:
    if ayAd� == "": continue
    print ("{:>10s} <{:02d}> {}" .format (ayAd�, i+1, aylar[i]) )
    i +=1
#----------------------------------------------------------------------------------------

i = 0
print ("\nG�n Adlar� (�ngilizce ve T�rk�e):\n", "-"*33, sep="")
for g�nAd� in calendar.day_name:
    print ("{:>10s} <{}> {}" .format (g�nAd�, i+1, g�nler2[i]) )
    i +=1
#----------------------------------------------------------------------------------------

print ("\nGirili [", y�l, "-", g�nler2[g�n-1], "] g�n�n�n her aydaki 2.tekrar tarihleri:\n", "-"*62, sep="")
for i in range (1, 13):
    takvim = calendar.monthcalendar (y�l, i)
    hafta1 = takvim [0]
    hafta2 = takvim [1]
    hafta3 = takvim [2]
    if hafta1 [g�n-1] != 0: # �rn: g�n = calendar.MONDAY
        arananG�n = hafta2 [g�n-1]
    else: arananG�n = hafta3 [g�n-1]
    print ("{:>10s} <{:02d}> {}" .format (calendar.month_name[i], arananG�n, aylar[i-1]))
