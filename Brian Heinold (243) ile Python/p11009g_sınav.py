# coding:iso-8859-9 T�rk�e

L1 = ["Ocak", "�ubat", "Mart", "Nisan", "May�s", "Haziran", "Temmuz", "A�ustos", "Eyl�l", "Ekim", "Kas�m", "Aral�k"]
L2 = ["Pazartesi", "Sal�", "�ar�amba", "Per�embe", "Cuma", "Cumartesi", "Pazar"]
L3 = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

from random import randint
ay=g�n=0
while not (0 < ay < 13):
    try: ay = abs (eval (input ("Ay [1->12] girin: ")))
    except Exception: ay = randint (1, 12)
while not (0 < g�n < 32):
    try: g�n = abs (eval (input ("G�n [1->31] girin: ")))
    except Exception: g�n = randint (1, 31)

if ay == 1 and g�n > 31: g�n = 31
elif ay == 2 and g�n > 28: g�n = 28
elif ay == 3 and g�n > 31: g�n = 31
elif ay == 4 and g�n > 30: g�n = 30
elif ay == 5 and g�n > 31: g�n = 31
elif ay == 6 and g�n > 30: g�n = 30
elif ay == 7 and g�n > 31: g�n = 31
elif ay == 8 and g�n > 31: g�n = 31
elif ay == 9 and g�n > 30: g�n = 30
elif ay == 10 and g�n > 31: g�n = 31
elif ay == 11 and g�n > 30: g�n = 30
elif ay == 12 and g�n > 31: g�n = 31

toplamG�n = L3[ay-1] + g�n
print ("\nGirilen g�n�n tarihi: {:02d}/{:02d}/2018\n{:s} ay� ve {} g�n�\nY�l�n {:03d}.g�n�" .format (g�n, ay, L1[ay-1], L2[(toplamG�n % 7)-1], toplamG�n) )