# coding:iso-8859-9 T�rk�e

""" Alttaki "dilim.txt" dosyas�n� yaratt�ktan sonra bu k�s�m art�k gereksiz olur...
dilimNo = 1
L = [sat�r.strip().split (" ") for sat�r in open ("zamanDilimleri.txt")]
dosya = open ("dilim.txt", "w")
try:
    for k in L:
        print (dilimNo, k[0], k[1], file=dosya)
        dilimNo +=1
except Exception: print()
dosya.close()
"""
L = [sat�r.strip().split (" ") for sat�r in open ("dilim.txt")]

from random import randint
from pprint import pprint

print ("D�nya Saal Dilimleri Listesi:\n", "-"*75, sep="")
pprint (L)
no1 = 0
while not (0 < no1 < 598):
    try: no1 = int (eval (input ("\n�lk zaman dilimi no'sunu girin: ")))
    except Exception: no1 = randint (1, 597)
zaman1 = input (str (no1) + ":" + L[no1-1][1] + "; zaman� [00:00am] girin: ")
saat1 = zaman1[:zaman1.index (":")]
dakika1 = zaman1[zaman1.index (":")+1:zaman1.index (":")+3]
ap1 = zaman1[-2:]

if L[no1-1][2] == "Z": saatFark�1 = 0
elif L[no1-1][2][0] == "+": saatFark�1 = int (L[no1-1][2][1:3])*60 + int (L[no1-1][2][-2:])
else: saatFark�1 = - (int (L[no1-1][2][1:3])*60 + int (L[no1-1][2][-2:]))

no2 = 0
while not (0 < no2 < 598):
    try: no2 = int (eval (input ("\n�kinci zaman dilimi no'sunu girin: ")))
    except Exception: no2 = randint (1, 597)

if L[no2-1][2] == "Z": saatFark�2 = 0
elif L[no2-1][2][0] == "+": saatFark�2 = int (L[no2-1][2][1:3])*60 + int (L[no2-1][2][-2:])
else: saatFark�2 = - (int (L[no2-1][2][1:3])*60 + int (L[no2-1][2][-2:]))

ap2 = ap1
zaman2 = int (saat1)*60 + int (dakika1) - (saatFark�1 - saatFark�2)
if zaman2 < 0:
    if ap1 == "am": ap2 = "pm"
    else: ap2 = "am"
    zaman2 = 12*60 + zaman2
if zaman2 >= 12*60:
    if ap1 == "am": ap2 = "pm"
    else: ap2 = "am"
    zaman2 = zaman2 - 12*60

print (no1, ":", L[no1-1][1], ", saat fark� ", L[no1-1][2], "'da saat: ", zaman1, "\n==>",
    no2, ":", L[no2-1][1], ", saat fark� ", L[no2-1][2], "'da saat: ", zaman2//60, ":", zaman2%60, ap2, sep="")

