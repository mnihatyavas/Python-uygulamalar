# coding:iso-8859-9 T�rk�e

from random import randint
from random import shuffle
L = ["Almanya", "Avusturya", "�ngiltere", "Japonya", "Amerika", "Kanada", "Brezilya", "Hindistan", "Rusya", "Kazakistan", "Ukrayna", "T�rkiye", "Hollanda", "Tayland", "Singapur", "Yunanistan", "�talya", "Bel�ika", "Honkong", "�spanya"]
L.sort()
shuffle (L)
print ("Eldeki", len (L), "adet �lkeler listesi==>\n", L)
�lke = str (L[randint (0, len (L)-1)])
g�ster = "-" * len (�lke)
g�ster = list (g�ster)
print ("".join (g�ster))
for i in range (len (g�ster)-1, -1, -1):
    print()
    harf = input (str (i+1) + ". tahmin harfinizi girin: ")
    if len (harf) > 1: harf = harf[0]
    for j in range (len (�lke)):
        if �lke[j] == harf: g�ster[j] = harf
    print ("".join (g�ster))
    if "-" not in g�ster: print ("\nBravo:", �lke); break
else: print ("\n5 tahminde bilemedi�iniz �lke ad�:", �lke, "idi.")