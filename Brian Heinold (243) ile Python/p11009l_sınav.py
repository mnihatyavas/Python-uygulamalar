# coding:iso-8859-9 Türkçe

print ("[1901->2099] arasındaki toplam gün sayısı: {:,d}" .format ( (3000-1901)*365 + (3000-1900) // 4))
L = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

print()
yıl1 = yıl2 = 0
while not (1900 < yıl1 < 3000):
    try: gün1, ay1, yıl1 = eval (input ("İlk gün, ay, yıl'ı girin: "))
    except Exception: gün1, ay1, yıl1 = 1, 1, 2001
while not (yıl1 < yıl2 < 3000):
    try: gün2, ay2, yıl2 = eval (input ("İkinci gün, ay, yıl'ı girin: "))
    except Exception: gün2, ay2, yıl2 = 31, 12, 2018

günToplamı = 365 - (L[ay1-1] + gün1) + (yıl2 - (yıl1 + 1)) * 365 + (yıl2 - (yıl1 + 1)) // 4 + (L[ay2-1] + gün2)
if (yıl2 - yıl1) < 4 and yıl2 % 4 == 0 and ay2 > 2: günToplamı +=1
print ("{:02d}/{:02d}/{:4d} ile {:02d}/{:02d}/{:4d} arasında toplam: {:,d} gün vardır." .format (gün1, ay1, yıl1, gün2, ay2, yıl2, günToplamı) )
