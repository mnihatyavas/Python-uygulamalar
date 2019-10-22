# coding:iso-8859-9 T�rk�e
# p_11501.py: while d�ng�l� say� toplam�, klavye veri giri�i ve gizli say� tahmini �rne�i.

son = 2019
toplam = 0
saya� = 1957

while saya� <= son:
    toplam = toplam + saya�
    saya� +=1

print ("1957'den {}'e kadar olan say�lar�n toplam�: {}'dir." .format (son, toplam) )
#-----------------------------------------------------------------------------------------------------

import sys

sys.stdout.write ("\nKlavyeden bir�eyler girin: ")
dizge = ""

while 1: # True
    krk = sys.stdin.read(1)
    dizge = dizge + krk
    if krk == '\n': break

sys.stderr.write ("Girdi�iniz karakterler:" + dizge)
#-----------------------------------------------------------------------------------------------------

import random

say� = int (random.random()*1000) + 1
tahmin = saya� = 0

while tahmin != say�:
    try: tahmin = int (input ("\nGizli say� ka� [0-1000]? "))
    except: tahmin = int (random.random()*1000) + 1
    saya� +=1
    if tahmin > 0:
        if tahmin > say�: print ("Tahmininiz b�y�k oldu")
        elif tahmin < say�: print ("Tahmininiz k���k oldu")
    else:
        sys.stderr.write ("Maalesef oyunu sonland�rmadan ayr�l�yorsunuz!")
        break

else: sys.stdout.write ("Tebrikler, gizli say�y� "+ str (saya�) + " kerede bildiniz!")


"""��kt�:
>python p_11501.py
1957'den 2019'e kadar olan say�lar�n toplam�: 125244'dir.

Klavyeden bir�eyler girin: M.Nihat Yava�
Girdi�iniz karakterler:M.Nihat Yava�

Gizli say� ka� [0-1000]? 500
Tahmininiz k���k oldu

Gizli say� ka� [0-1000]? 750
Tahmininiz b�y�k oldu

Gizli say� ka� [0-1000]? 625
Tahmininiz k���k oldu

Gizli say� ka� [0-1000]? 690
Tahmininiz k���k oldu

Gizli say� ka� [0-1000]? 720
Tahmininiz b�y�k oldu

Gizli say� ka� [0-1000]? 700
Tahmininiz b�y�k oldu

Gizli say� ka� [0-1000]? 694
Tahmininiz k���k oldu

Gizli say� ka� [0-1000]? 698
Tebrikler, gizli say�y� 8 kerede bildiniz!
"""