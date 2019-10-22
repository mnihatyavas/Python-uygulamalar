# coding:iso-8859-9 Türkçe

from random import randint
from random import shuffle
L = ["Almanya", "Avusturya", "İngiltere", "Japonya", "Amerika", "Kanada", "Brezilya", "Hindistan", "Rusya", "Kazakistan", "Ukrayna", "Türkiye", "Hollanda", "Tayland", "Singapur", "Yunanistan", "İtalya", "Belçika", "Honkong", "İspanya"]
L.sort()
shuffle (L)
print ("Eldeki", len (L), "adet ülkeler listesi==>\n", L)
ülke = str (L[randint (0, len (L)-1)])
göster = "-" * len (ülke)
göster = list (göster)
print ("".join (göster))
for i in range (len (göster)-1, -1, -1):
    print()
    harf = input (str (i+1) + ". tahmin harfinizi girin: ")
    if len (harf) > 1: harf = harf[0]
    for j in range (len (ülke)):
        if ülke[j] == harf: göster[j] = harf
    print ("".join (göster))
    if "-" not in göster: print ("\nBravo:", ülke); break
else: print ("\n5 tahminde bilemediğiniz ülke adı:", ülke, "idi.")