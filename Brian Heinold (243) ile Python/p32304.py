# coding:iso-8859-9 Türkçe

from math import sin, pi, pow, cos
from random import randint, random
from functools import reduce
from operator import add, mul

dizge = "Kapsamlı listeden önce Python map fonksiyonunu kullanmaktaydı."
print ("Dizgemiz: [", dizge, "]", sep="")

L = list (map (len, dizge.split()))
print ("\nMap ile dizgedeki kelimelerin uzunlukları listesi:", L)

L = [len (kelime) for kelime in dizge.split()]
print ("\nKapsamlı listelemeyle dizgedeki kelimelerin uzunlukları listesi:", L)

L = list (map (sin, (radyan for radyan in (0, pi/4, pi/2, 3*pi/4, pi, 5*pi/4, 3*pi/2, 7*pi/4) ) ))
print ("\nMap ile 0,45,..270 derece/radyan'ın sinüs'leri: ", end="")
for i in range (len (L)): print (round (L[i], 2), end="  ")

L = list (map (pow, [randint(0,50)+random() for i in range(10)], [randint(-50,50)+random() for i in range(10)]))
print ("\n\nMap ile (0->50)^(-50->50) gelişigüzel pow sayısı üretimi:", L)
#------------------------------------------------------------------------------------------

dizge = "Kapsamlı listeden önce, Python şartlı liste üretimini filter fonksiyonuyla gerçekleştirmekteydi."
print ("\nDizgemiz", dizge)

L = list (filter (lambda x: len (x) > 6, dizge.split()))
print ("\nFilter ile dizgedeki 6'den uzun kelimelerin listesi:", L)

L = [kelime for kelime in dizge.split() if len (kelime) > 6]
print ("\nKapsamlı listeyle dizgedeki 6'den uzun kelimelerin listesi:", L)

L = list (filter (lambda x: abs (cos(x)) >= 0.75, [cos (a*pi/180) for a in range (0, 360, 10)] ))
# Lambda, kapsamlı isabetinde olmadı; 0.65 filtresi için 0.75 istiyor?..
print ("\nFilter ile dizgedeki -0.65->0.65 cos değerleri listesi:", L)

L = [cos (a*pi/180) for a in range (0, 360, 10) if -0.65 <= cos(a*pi/180) <= 0.65]
print ("\nKapsamlı listeyle dizgedeki -0.65->0.65 cos değerleri listesi:", L)
#------------------------------------------------------------------------------------------

L = [cos (a*pi/180) for a in range (0, 360, 10)]
sayaç = 0
for d in L:
    if abs (d) <=.65: sayaç +=1
print ("\n-0.65 <= cos(x) <= +0.65 döngülü liste elemanları sayısı: ", sayaç)
print ("-0.65 <= cos(x) <= +0.65 kapsamlı liste elemanları sayısı: ", len ([cos (a*pi/180) for a in range (0, 360, 10) if abs (cos(a*pi/180)) <= 0.65]) )
#------------------------------------------------------------------------------------------

toplam = 0
for i in range (1,101): toplam +=i
print ("\n1->100 sayının döngülü toplamı:", toplam)
print ("\n1->100 sayının reduce ve lambda'lı toplamı:", reduce (lambda x,y: x+y, range (1,101)) )

print ("1->100 sayının reduce ve add'li toplamı:", reduce (add, range (1,101)) )

print()
n = randint (0,50)
print (n, "sayısının reduce ve lambda'lı faktöriyeli:", reduce (lambda x, y: x * y, range (1, n+1)) )

print (n, "sayısının reduce ve mul'lı faktöriyeli:", reduce (mul, range (1, n+1)) )
