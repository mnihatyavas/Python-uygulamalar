# coding:iso-8859-9 T�rk�e

sonu� = 0
say� = fark = a = 1
while say�:
    try: say� = abs (eval (input ("Karek�k� bulunacak say�y� girin [0:��k]: ")))
    except Exception: say� = 5
    while fark > 1e-10:
        sonu� = (a + say� / a) / 2
        fark = abs (sonu� - a)
        a = sonu�
    break
if say�: print (say�, "say�s�n�n karek�k�:", sonu�)
