# coding:iso-8859-9 T�rk�e

from math import *
from random import randint

zaman1 = eval (input ("\n[0-->24] aras� bir saat girin: "))
if zaman1 < 0: zaman1 = 0
if zaman1 > 24: zaman1 = 24
zaman2 = abs (eval (input ("\nKa� saat daha burada kalacaks�n?: ")))
zaman3 = (zaman1 + zaman2 % 24) % 24
sembol =""
if zaman3 > 12: sembol = "pm"; zaman3 -= 12
else: sembol = "am"
print ("Buradan saat tam ", zaman3, ".00 ", sembol, "'de ayr�lmal�s�n�z!", sep="")
print()
# A��klama gere�i, �eker miktar� arama aral��� 150-200 ve
# x-y-z payla��mlar� ilk toplam 150 adetten 29-25-21'den ba�layabilir ve
# �eker miktar� ayn�yken �-5x=2 ve �-6y=3 ve �-7x=2 �art� sa�lanmal�;
# ancak ��z�m� bulduktan sonra d�ng�leri tamamen break'lemeyi bilemedim!..
x1=y1=z1=�x=�y=�z= 0
for � in range (150, 201):
    for x in range (29, 42):
        if (� - 5*x == 2):
            if x==x1: continue
            x1=x
            print (�, "x:", x);
            �x=�
            if �z==�y and �y==�x: print ("TAMAM BULDUM, �eker:", �)
            break
        for y in range (25, 35):
            if (� - 6*y == 3):
                if y==y1: continue
                y1=y
                print (�, "y:", y)
                �y=�
                if �z==�y and �y==�x: print ("TAMAM BULDUM, �eker:", �)
                break
            for z in range (21, 30):
                if (� - 7*z == 2):
                    if z==z1: continue
                    z1=z
                    print (�, "z:", z)
                    �z=�
                    if �z==�y and �y==�x: print ("TAMAM BULDUM, �eker:", �)
                    break
print()
# �eker'in genellenmesi denemesi...
azami = abs (trunc (eval (input ("Kavanozdaki azami �eker say�s�n� gir: "))))
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
if buldum: print ("Buldum; Kavanozdaki �eker say�s�:", x)
else: print ("Maalesef, �eker say�s�n� bulamad�m!")
print()
kazand�=kaybetti=0
for i in range (10):
    puan = randint (1,2)
    if puan==2: kazand� +=1
    else: kaybetti +=1
print ("Oyuncunun bilgisayara kar�� 10 rauntluk tavla oyunu sonucu==>")
print (kazand�, "kez kazand� ve", kaybetti, "kez kaybetti.")
print ("Oyuncu: ", end="")
if kazand� > kaybetti: print ("KAZANDI!")
elif kazand� < kaybetti:  print ("KAYBETT�!")
else: print ("BERABERE KALDI!")
