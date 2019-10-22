# coding:iso-8859-9 T�rk�e

from math import sin, pi, pow, cos
from random import randint, random
from functools import reduce
from operator import add, mul

dizge = "Kapsaml� listeden �nce Python map fonksiyonunu kullanmaktayd�."
print ("Dizgemiz: [", dizge, "]", sep="")

L = list (map (len, dizge.split()))
print ("\nMap ile dizgedeki kelimelerin uzunluklar� listesi:", L)

L = [len (kelime) for kelime in dizge.split()]
print ("\nKapsaml� listelemeyle dizgedeki kelimelerin uzunluklar� listesi:", L)

L = list (map (sin, (radyan for radyan in (0, pi/4, pi/2, 3*pi/4, pi, 5*pi/4, 3*pi/2, 7*pi/4) ) ))
print ("\nMap ile 0,45,..270 derece/radyan'�n sin�s'leri: ", end="")
for i in range (len (L)): print (round (L[i], 2), end="  ")

L = list (map (pow, [randint(0,50)+random() for i in range(10)], [randint(-50,50)+random() for i in range(10)]))
print ("\n\nMap ile (0->50)^(-50->50) geli�ig�zel pow say�s� �retimi:", L)
#------------------------------------------------------------------------------------------

dizge = "Kapsaml� listeden �nce, Python �artl� liste �retimini filter fonksiyonuyla ger�ekle�tirmekteydi."
print ("\nDizgemiz", dizge)

L = list (filter (lambda x: len (x) > 6, dizge.split()))
print ("\nFilter ile dizgedeki 6'den uzun kelimelerin listesi:", L)

L = [kelime for kelime in dizge.split() if len (kelime) > 6]
print ("\nKapsaml� listeyle dizgedeki 6'den uzun kelimelerin listesi:", L)

L = list (filter (lambda x: abs (cos(x)) >= 0.75, [cos (a*pi/180) for a in range (0, 360, 10)] ))
# Lambda, kapsaml� isabetinde olmad�; 0.65 filtresi i�in 0.75 istiyor?..
print ("\nFilter ile dizgedeki -0.65->0.65 cos de�erleri listesi:", L)

L = [cos (a*pi/180) for a in range (0, 360, 10) if -0.65 <= cos(a*pi/180) <= 0.65]
print ("\nKapsaml� listeyle dizgedeki -0.65->0.65 cos de�erleri listesi:", L)
#------------------------------------------------------------------------------------------

L = [cos (a*pi/180) for a in range (0, 360, 10)]
saya� = 0
for d in L:
    if abs (d) <=.65: saya� +=1
print ("\n-0.65 <= cos(x) <= +0.65 d�ng�l� liste elemanlar� say�s�: ", saya�)
print ("-0.65 <= cos(x) <= +0.65 kapsaml� liste elemanlar� say�s�: ", len ([cos (a*pi/180) for a in range (0, 360, 10) if abs (cos(a*pi/180)) <= 0.65]) )
#------------------------------------------------------------------------------------------

toplam = 0
for i in range (1,101): toplam +=i
print ("\n1->100 say�n�n d�ng�l� toplam�:", toplam)
print ("\n1->100 say�n�n reduce ve lambda'l� toplam�:", reduce (lambda x,y: x+y, range (1,101)) )

print ("1->100 say�n�n reduce ve add'li toplam�:", reduce (add, range (1,101)) )

print()
n = randint (0,50)
print (n, "say�s�n�n reduce ve lambda'l� fakt�riyeli:", reduce (lambda x, y: x * y, range (1, n+1)) )

print (n, "say�s�n�n reduce ve mul'l� fakt�riyeli:", reduce (mul, range (1, n+1)) )
