# coding:iso-8859-9 Türkçe

from random import randint
from math import trunc

azami=abs (trunc (eval (input ("Tek zarı kaç kez atmak istersin: "))))
toplam=0
for i in range (azami):
    toplam +=randint (1,6)
if toplam !=0: print (azami, "kez attığınız tek zarın toplamı", toplam, "ve ortalaması da", round (toplam/azami, 2))
print()
asal=abs (trunc (eval (input ("Asal sayı kontrolü değerini girin: "))))
bayrak=0
for i in range (2, asal):
    if asal % i == 0: bayrak=1; break
if not bayrak and asal != 0: print (asal, "bir asal sayıdır (sadece 1 ve kendisine bölünür).")
elif bayrak: print (asal, "bir asal sayı değildir (1 ve kendisi dışında da böleni vardır).")
print()
enbüyük=enküçük=0
sayı=abs (trunc (eval (input ("Kaç tesadüfi sayı üretelim [0->1000]: "))))
for i in range (sayı):
    enbüyük = randint (-1000, 1000)
    if enküçük > enbüyük: enküçük = enbüyük
print (sayı, "tesadüfi tamsayının enküçüğü:", enküçük, "ve enbüyüğü de:", enbüyük)
