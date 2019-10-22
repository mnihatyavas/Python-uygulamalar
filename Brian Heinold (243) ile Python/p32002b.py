# coding:iso-8859-9 T�rk�e

import calendar
# Referans: www.python.org==> Lib/calendar.py

aylar = ["Ocak", "�ubat", "Mart", "Nisan", "May�s", "Haziran", "Temmuz", "A�ustos", "Eyl�l", "Ekim", "Kas�m", "Aral�k"]

try: y�l = int (eval (input ("(-/+) Tamsay� y�l� girin: ")))
except Exception: y�l = 2018

print ("\n[", y�l, "] y�l�n�n her ay�n�n ilk PAZARTES� g�nleri:\n", "="*48, sep="")
for ay in range (1, 13):
    takvim = calendar.monthcalendar (y�l, ay)
    hafta1 = takvim[0]
    hafta2 = takvim[1]
    if hafta1 [calendar.MONDAY] != 0: arananG�n = hafta1[calendar.MONDAY]
    else: arananG�n = hafta2[calendar.MONDAY]
    print ("{:>10s} {} {}" .format (calendar.month_name[ay], arananG�n, aylar[ay-1]) )
