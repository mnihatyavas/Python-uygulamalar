# coding:iso-8859-9 T�rk�e

from random import randint
from math import trunc

# Virg�llerle ayr�k 2 ayr� veri giri� y�ntemi
a, b = eval (input ('Virg�llerle ayr�k 2 say� girin: '))
if a<b: a,b=b,a # (k���k/b�y�k) kontrols�z, bi�imsiz sonu�lar �retebiliyor...
print (a, "+", b, "=", a+b)
print (a, "-", b, "=", a-b)
print (a, "*", b, "=", a*b)
print (a, "/", b, "=", a/b)
""" Her 2 say�n�n da negatif olmas� durumunda, sonucun pozitif ve 
s�f�rdan b�y�k ��kmas�n� isterseniz negatif k����� �ste alabilirsiniz:
Yani e�er a=-5, b=-15 ise a, b'den b�y�k oldu�u halde
print (b, "/", a, "=", b/a)
ifadesi sonucu +3 yans�t�r
"""
print (a, "^", b, "=", a**b)
print (a, "%", b, "=", a%b)
print (a, "y�zde", b, "= %", (a-b)/b*100)

""" �oklu yorum sat�r�
     Program ad�: Tek ve �ok sat�rl� python yorumlar�
     Kodlayan: M.Nihat Yava�
     Tarih: 29.09.2018-23:23 """

""" veya
�oklu yorum sat�r�
Program ad�: Tek ve �ok sat�rl� python yorumlar�
Kodlayan: M.Nihat Yava�
Tarih: 29.09.2018-23:23
"""
��kt�=""" veya
�oklu yorum sat�r�
Program ad�: Tek ve �ok sat�rl� python yorumlar�
Kodlayan: M.Nihat Yava�
Tarih: 29.09.2018-23:23
"""