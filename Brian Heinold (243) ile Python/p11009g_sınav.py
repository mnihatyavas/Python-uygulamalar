# coding:iso-8859-9 Türkçe

L1 = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
L2 = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
L3 = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

from random import randint
ay=gün=0
while not (0 < ay < 13):
    try: ay = abs (eval (input ("Ay [1->12] girin: ")))
    except Exception: ay = randint (1, 12)
while not (0 < gün < 32):
    try: gün = abs (eval (input ("Gün [1->31] girin: ")))
    except Exception: gün = randint (1, 31)

if ay == 1 and gün > 31: gün = 31
elif ay == 2 and gün > 28: gün = 28
elif ay == 3 and gün > 31: gün = 31
elif ay == 4 and gün > 30: gün = 30
elif ay == 5 and gün > 31: gün = 31
elif ay == 6 and gün > 30: gün = 30
elif ay == 7 and gün > 31: gün = 31
elif ay == 8 and gün > 31: gün = 31
elif ay == 9 and gün > 30: gün = 30
elif ay == 10 and gün > 31: gün = 31
elif ay == 11 and gün > 30: gün = 30
elif ay == 12 and gün > 31: gün = 31

toplamGün = L3[ay-1] + gün
print ("\nGirilen günün tarihi: {:02d}/{:02d}/2018\n{:s} ayı ve {} günü\nYılın {:03d}.günü" .format (gün, ay, L1[ay-1], L2[(toplamGün % 7)-1], toplamGün) )