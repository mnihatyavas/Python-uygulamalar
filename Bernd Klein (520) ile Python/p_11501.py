# coding:iso-8859-9 Türkçe
# p_11501.py: while döngülü sayı toplamı, klavye veri girişi ve gizli sayı tahmini örneği.

son = 2019
toplam = 0
sayaç = 1957

while sayaç <= son:
    toplam = toplam + sayaç
    sayaç +=1

print ("1957'den {}'e kadar olan sayıların toplamı: {}'dir." .format (son, toplam) )
#-----------------------------------------------------------------------------------------------------

import sys

sys.stdout.write ("\nKlavyeden birşeyler girin: ")
dizge = ""

while 1: # True
    krk = sys.stdin.read(1)
    dizge = dizge + krk
    if krk == '\n': break

sys.stderr.write ("Girdiğiniz karakterler:" + dizge)
#-----------------------------------------------------------------------------------------------------

import random

sayı = int (random.random()*1000) + 1
tahmin = sayaç = 0

while tahmin != sayı:
    try: tahmin = int (input ("\nGizli sayı kaç [0-1000]? "))
    except: tahmin = int (random.random()*1000) + 1
    sayaç +=1
    if tahmin > 0:
        if tahmin > sayı: print ("Tahmininiz büyük oldu")
        elif tahmin < sayı: print ("Tahmininiz küçük oldu")
    else:
        sys.stderr.write ("Maalesef oyunu sonlandırmadan ayrılıyorsunuz!")
        break

else: sys.stdout.write ("Tebrikler, gizli sayıyı "+ str (sayaç) + " kerede bildiniz!")


"""Çıktı:
>python p_11501.py
1957'den 2019'e kadar olan sayıların toplamı: 125244'dir.

Klavyeden birşeyler girin: M.Nihat Yavaş
Girdiğiniz karakterler:M.Nihat Yavaş

Gizli sayı kaç [0-1000]? 500
Tahmininiz küçük oldu

Gizli sayı kaç [0-1000]? 750
Tahmininiz büyük oldu

Gizli sayı kaç [0-1000]? 625
Tahmininiz küçük oldu

Gizli sayı kaç [0-1000]? 690
Tahmininiz küçük oldu

Gizli sayı kaç [0-1000]? 720
Tahmininiz büyük oldu

Gizli sayı kaç [0-1000]? 700
Tahmininiz büyük oldu

Gizli sayı kaç [0-1000]? 694
Tahmininiz küçük oldu

Gizli sayı kaç [0-1000]? 698
Tebrikler, gizli sayıyı 8 kerede bildiniz!
"""