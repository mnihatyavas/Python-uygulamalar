# coding:iso-8859-9 T�rk�e

from random import randint
from math import trunc

azami=abs (trunc (eval (input ("Tek zar� ka� kez atmak istersin: "))))
toplam=0
for i in range (azami):
    toplam +=randint (1,6)
if toplam !=0: print (azami, "kez att���n�z tek zar�n toplam�", toplam, "ve ortalamas� da", round (toplam/azami, 2))
print()
asal=abs (trunc (eval (input ("Asal say� kontrol� de�erini girin: "))))
bayrak=0
for i in range (2, asal):
    if asal % i == 0: bayrak=1; break
if not bayrak and asal != 0: print (asal, "bir asal say�d�r (sadece 1 ve kendisine b�l�n�r).")
elif bayrak: print (asal, "bir asal say� de�ildir (1 ve kendisi d���nda da b�leni vard�r).")
print()
enb�y�k=enk���k=0
say�=abs (trunc (eval (input ("Ka� tesad�fi say� �retelim [0->1000]: "))))
for i in range (say�):
    enb�y�k = randint (-1000, 1000)
    if enk���k > enb�y�k: enk���k = enb�y�k
print (say�, "tesad�fi tamsay�n�n enk�����:", enk���k, "ve enb�y��� de:", enb�y�k)
