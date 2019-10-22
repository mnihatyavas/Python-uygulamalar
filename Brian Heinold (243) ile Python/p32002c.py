# coding:iso-8859-9 Türkçe

import calendar
from random import randint

aylar = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
günler1 = ["Pt", "Sa", "Ça", "Pe", "Cu", "Ct", "Pa"]
günler2 = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]

try: yıl = int (eval (input ("Takvim tamsayı yılını girin: ")))
except Exception: yıl = 2018

try: ay = int (eval (input ("Takvim tamsayı ayını [1-12] girin: ")))
except Exception: ay = randint (1, 12)
if 12 < ay < 1: ay = randint (1, 12)

try: gün = int (eval (input ("Takvim tamsayı haftanın gününü [1:Pzt-7:Pz] girin: ")))
except Exception: gün = randint (1, 7)
if 7 < gün < 1: gün = randint (1, 7)
print ("\n<", yıl, ">yılının <", aylar[ay-1], "> ayı takvimi:\n", "-"*36, sep="" )
aylıkMetinTakvimi = calendar.TextCalendar (gün-1) # calendar.MONDAY == 1
aylıkHtmlTakvimi = calendar.HTMLCalendar (gün-1)
dosya = open ("mny1.html", "w")
dizge = aylıkMetinTakvimi.formatmonth (yıl, ay)
print (dizge) # Ay'lık takvimleri hazır formatlı bir bütün olarak yazar...
print (aylıkHtmlTakvimi.formatmonth (yıl, ay), file=dosya)
dosya.close()
print ("HTML formatlı takvim için mny1.html dosyasını işletin")
#----------------------------------------------------------------------------------------

print ("\nSıfırlar ilk PAZARTESİ'nden önceki ve aysonu haftası tamamlayanlarıdır.\n", "-"*71, sep="")
print (" " * ((20 - (len (aylar[ay-1]) + len (str (yıl)) + 2 )) // 2 ), aylar[ay-1], yıl)
i = gün-1
while True:
    print (günler1 [i], end=" ")
    i +=1
    if i >= 7: i = 0
    if i == gün-1: break
print ()
j = 0
for i in aylıkMetinTakvimi.itermonthdays (yıl, ay):
    j +=1
    print ("{:2d}" .format (i), end=" ") # Ay'ın günler1i belirlediğimiz formatla tek tek yazdırılır...
    if j%7 == 0: print()
#----------------------------------------------------------------------------------------

i = 0
print ("\nAy Adları (İngilizce ve Türkçe):\n", "-"*32, sep="")
for ayAdı in calendar.month_name:
    if ayAdı == "": continue
    print ("{:>10s} <{:02d}> {}" .format (ayAdı, i+1, aylar[i]) )
    i +=1
#----------------------------------------------------------------------------------------

i = 0
print ("\nGün Adları (İngilizce ve Türkçe):\n", "-"*33, sep="")
for günAdı in calendar.day_name:
    print ("{:>10s} <{}> {}" .format (günAdı, i+1, günler2[i]) )
    i +=1
#----------------------------------------------------------------------------------------

print ("\nGirili [", yıl, "-", günler2[gün-1], "] gününün her aydaki 2.tekrar tarihleri:\n", "-"*62, sep="")
for i in range (1, 13):
    takvim = calendar.monthcalendar (yıl, i)
    hafta1 = takvim [0]
    hafta2 = takvim [1]
    hafta3 = takvim [2]
    if hafta1 [gün-1] != 0: # Örn: gün = calendar.MONDAY
        arananGün = hafta2 [gün-1]
    else: arananGün = hafta3 [gün-1]
    print ("{:>10s} <{:02d}> {}" .format (calendar.month_name[i], arananGün, aylar[i-1]))
