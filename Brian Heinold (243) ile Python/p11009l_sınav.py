# coding:iso-8859-9 T�rk�e

print ("[1901->2099] aras�ndaki toplam g�n say�s�: {:,d}" .format ( (3000-1901)*365 + (3000-1900) // 4))
L = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

print()
y�l1 = y�l2 = 0
while not (1900 < y�l1 < 3000):
    try: g�n1, ay1, y�l1 = eval (input ("�lk g�n, ay, y�l'� girin: "))
    except Exception: g�n1, ay1, y�l1 = 1, 1, 2001
while not (y�l1 < y�l2 < 3000):
    try: g�n2, ay2, y�l2 = eval (input ("�kinci g�n, ay, y�l'� girin: "))
    except Exception: g�n2, ay2, y�l2 = 31, 12, 2018

g�nToplam� = 365 - (L[ay1-1] + g�n1) + (y�l2 - (y�l1 + 1)) * 365 + (y�l2 - (y�l1 + 1)) // 4 + (L[ay2-1] + g�n2)
if (y�l2 - y�l1) < 4 and y�l2 % 4 == 0 and ay2 > 2: g�nToplam� +=1
print ("{:02d}/{:02d}/{:4d} ile {:02d}/{:02d}/{:4d} aras�nda toplam: {:,d} g�n vard�r." .format (g�n1, ay1, y�l1, g�n2, ay2, y�l2, g�nToplam�) )
