# coding:iso-8859-9 Türkçe

from math import *
from random import randint

zaman1 = eval (input ("\n[0-->24] arası bir saat girin: "))
if zaman1 < 0: zaman1 = 0
if zaman1 > 24: zaman1 = 24
zaman2 = abs (eval (input ("\nKaç saat daha burada kalacaksın?: ")))
zaman3 = (zaman1 + zaman2 % 24) % 24
sembol =""
if zaman3 > 12: sembol = "pm"; zaman3 -= 12
else: sembol = "am"
print ("Buradan saat tam ", zaman3, ".00 ", sembol, "'de ayrılmalısınız!", sep="")
print()
# Açıklama gereği, şeker miktarı arama aralığı 150-200 ve
# x-y-z paylaşımları ilk toplam 150 adetten 29-25-21'den başlayabilir ve
# şeker miktarı aynıyken ş-5x=2 ve ş-6y=3 ve ş-7x=2 şartı sağlanmalı;
# ancak çözümü bulduktan sonra döngüleri tamamen break'lemeyi bilemedim!..
x1=y1=z1=şx=şy=şz= 0
for ş in range (150, 201):
    for x in range (29, 42):
        if (ş - 5*x == 2):
            if x==x1: continue
            x1=x
            print (ş, "x:", x);
            şx=ş
            if şz==şy and şy==şx: print ("TAMAM BULDUM, Şeker:", ş)
            break
        for y in range (25, 35):
            if (ş - 6*y == 3):
                if y==y1: continue
                y1=y
                print (ş, "y:", y)
                şy=ş
                if şz==şy and şy==şx: print ("TAMAM BULDUM, Şeker:", ş)
                break
            for z in range (21, 30):
                if (ş - 7*z == 2):
                    if z==z1: continue
                    z1=z
                    print (ş, "z:", z)
                    şz=ş
                    if şz==şy and şy==şx: print ("TAMAM BULDUM, Şeker:", ş)
                    break
print()
# Şeker'in genellenmesi denemesi...
azami = abs (trunc (eval (input ("Kavanozdaki azami şeker sayısını gir: "))))
z=y=9
x=7
buldum=False
for z in range (9, azami+1, 7):
    while y <= z:
        if y==z: break
        y +=6
    while x <= z:
        if x==z: break
        x +=5
    if z==y==x: buldum=True; break
if buldum: print ("Buldum; Kavanozdaki şeker sayısı:", x)
else: print ("Maalesef, şeker sayısını bulamadım!")
print()
kazandı=kaybetti=0
for i in range (10):
    puan = randint (1,2)
    if puan==2: kazandı +=1
    else: kaybetti +=1
print ("Oyuncunun bilgisayara karşı 10 rauntluk tavla oyunu sonucu==>")
print (kazandı, "kez kazandı ve", kaybetti, "kez kaybetti.")
print ("Oyuncu: ", end="")
if kazandı > kaybetti: print ("KAZANDI!")
elif kazandı < kaybetti:  print ("KAYBETTİ!")
else: print ("BERABERE KALDI!")
