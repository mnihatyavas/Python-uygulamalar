# coding:iso-8859-9 T�rk�e
# p_10401.pt: Girilen say� alt�ndaki iki tamsay� kareleri karek�k�n� di�erbir tamsay�ya e�itleme �rne�i.

from math import sqrt

n = abs (int (eval (input ("Bir pozitif tamsay� girin [4-->]: "))))

print ("Bu say� alt�nda hangi 2 say�n�n kareleri toplam�n�n karek�k� 3.say�ya e�ittir?\n", "-"*78, sep="")
for a in range (1, n+1):
    for b in range (a, n+1):
        cKare = a**2 + b**2
        c = int (sqrt (cKare))
        if cKare == c**2: print (a, b, c)


"""��kt�:
>python p_10401.py
Bir pozitif tamsay� girin [4-->]: -0.15
Bu say� alt�nda hangi 2 say�n�n kareleri toplam�n�n karek�k� 3.say�ya e�ittir?
------------------------------------------------------------------------------

>python p_10401.py  ** TEKRAR **
Bir pozitif tamsay� girin [4-->]: 21
Bu say� alt�nda hangi 2 say�n�n kareleri toplam�n�n karek�k� 3.say�ya e�ittir?
------------------------------------------------------------------------------
3 4 5
5 12 13
6 8 10
8 15 17
9 12 15
12 16 20
15 20 25
20 21 29
"""