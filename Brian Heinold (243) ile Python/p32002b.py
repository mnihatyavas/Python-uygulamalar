# coding:iso-8859-9 Türkçe

import calendar
# Referans: www.python.org==> Lib/calendar.py

aylar = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]

try: yıl = int (eval (input ("(-/+) Tamsayı yılı girin: ")))
except Exception: yıl = 2018

print ("\n[", yıl, "] yılının her ayının ilk PAZARTESİ günleri:\n", "="*48, sep="")
for ay in range (1, 13):
    takvim = calendar.monthcalendar (yıl, ay)
    hafta1 = takvim[0]
    hafta2 = takvim[1]
    if hafta1 [calendar.MONDAY] != 0: arananGün = hafta1[calendar.MONDAY]
    else: arananGün = hafta2[calendar.MONDAY]
    print ("{:>10s} {} {}" .format (calendar.month_name[ay], arananGün, aylar[ay-1]) )
