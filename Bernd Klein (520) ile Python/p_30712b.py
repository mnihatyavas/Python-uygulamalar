# coding:iso-8859-9 T�rk�e
# p_30712b.py: �ngilteredeki �niversitelere ��renci kay�tlar� �rne�i.

import random
import numpy as np
from collections import Counter

def ka��nc�Arada (de�erim, b�l�mler, u�lar_1Mi=True):
    for i in range (0, len (b�l�mler)):
        if de�erim < b�l�mler[i]: return i-1 if u�lar_1Mi else i
    return -1 if u�lar_1Mi else len (b�l�mler)

def a��rl�kl�Tercih (ibareler, gelmeA��rl�klar�, kriptoluMu=True):
    if kriptoluMu: x = random.SystemRandom().random()
    else: x = np.random.random()
    gelmeY�zdeleriToplam� = [0] + list (np.cumsum (gelmeA��rl�klar�))
    endeks = ka��nc�Arada (x, gelmeY�zdeleriToplam�)
    return ibareler[endeks]

def veridosyas�n���le (dosyaAd�):
    �niversiteler = []
    kay�tl�lar = []
    with open (dosyaAd�) as dosya:
        toplamKay�tl� = 0
        dosya.readline()
        for sat�r in dosya:
            �niversite, kay�tl� = sat�r.split (", ")
            �niversite = �niversite[1:-1]
            kay�tl� = eval (kay�tl�)
            kay�tl�lar.append (kay�tl�)
            �niversiteler.append (�niversite)
            toplamKay�tl� += kay�tl�
    return (�niversiteler, kay�tl�lar, toplamKay�tl�)


�niversiteler, kay�tl�lar, toplam��renci = veridosyas�n���le ("p_30712bx.txt")
say� = len (�niversiteler)
print ("�ngilteredeki toplam ", say�, " �niversite ve kay�tl� ��renci say�lar� d�k�m�:",
    "\n", "-"*70, sep="")
for i in range (say�):
    print ((i+1), ") ", �niversiteler[i], sep="", end=": ")
    print (kay�tl�lar[i])
print ("-"*70, "\nT�m �niversitelerdeki toplam ��renci say�s�: ", toplam��renci, sep="")

oranla�t�r�lanKay�tlar = [kay�tl� / toplam��renci for kay�tl� in kay�tl�lar]
# Hayali bir geli�ig�zel a��rl�kl� tercih kayd� yapal�m:
print ("\nA��rl�kl� tercih y�ntemiyle tesad�fi bir �niversite se�imi: ", a��rl�kl�Tercih (�niversiteler, oranla�t�r�lanKay�tlar), sep="")

try: toplam = abs (int (input ("\nToplam ka� farazi ��renciyi t�m �niversitelere a��rl�kl� kaydedelim [100 000]? ")))
except: toplam = 100000

orant�l�Kay�tlar = []
for i in range (toplam): orant�l�Kay�tlar.append (a��rl�kl�Tercih (�niversiteler, oranla�t�r�lanKay�tlar) )
#orant�l�Kay�tlar.sort() # �niversite adlar�n� a->z s�ralar...
say = Counter (orant�l�Kay�tlar)

print ("\n�ngilteredeki toplam ", say�, " �niversiteye ", toplam, " adet ��renci da��t�m�:", "\n", "-"*66, sep="")
i = 1
for a in say:
    print (i, ") ", a, ": ", say[a], sep="")
    i +=1



"""��kt�:
>python p_30712b.py
�ngilteredeki toplam 20 �niversite ve kay�tl� ��renci say�lar� d�k�m�:
----------------------------------------------------------------------
1) Open University in England: 123490
2) University of Manchester: 37925
3) University of Nottingham: 33270
4) Sheffield Hallam University: 33100
5) University of Birmingham: 32335
6) Manchester Metropolitan University: 32160
7) University of Leeds: 30975
8) Cardiff University: 30180
9) University of South Wales: 29195
10) University College London: 28430
11) King's College London: 27645
12) University of Edinburgh: 27625
13) Northumbria University: 27565
14) University of Glasgow: 27390
15) University of Plymouth: 27203
16) Coventry University: 27002
17) University of the West of England: 26734
18) University of Central Lancashire: 26265
19) Nottingham Trent University: 26221
20) University of Sheffield: 25908
----------------------------------------------------------------------
T�m �niversitelerdeki toplam ��renci say�s�: 680618

A��rl�kl� tercih y�ntemiyle tesad�fi bir �niversite se�imi: Nottingham Trent University

Toplam ka� farazi ��renciyi t�m �niversitelere a��rl�kl� kaydedelim [100 000]?

�ngilteredeki toplam 20 �niversiteye 100000 adet ��renci da��t�m�:
------------------------------------------------------------------
1) King's College London: 4111
2) Cardiff University: 4362
3) University of the West of England: 3956
4) University of South Wales: 4295
5) Sheffield Hallam University: 4941
6) University of Sheffield: 3712
7) University of Manchester: 5637
8) University College London: 4261
9) Open University in England: 17981
10) University of Plymouth: 3955
11) Northumbria University: 4045
12) University of Birmingham: 4728
13) University of Central Lancashire: 3810
14) University of Edinburgh: 4018
15) University of Nottingham: 5009
16) University of Glasgow: 3972
17) Manchester Metropolitan University: 4739
18) Coventry University: 3981
19) Nottingham Trent University: 3889
20) University of Leeds: 4598
"""