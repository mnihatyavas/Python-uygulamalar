# coding:iso-8859-9 T�rk�e
# p_30712c.py: 4 prensin son 4'� favori 11 amazon k�z adayla g�nbeg�n de�i�en a��rl�kla evlilik ihtimali �rne�i.

import random
import numpy as np
from time import process_time as pt

def a��rl�kl��rnekleme2 (listem, a��rl�klar�, k):
    se�ilenK�me = set()
    listem = list (listem)
    a��rl�klar� = list (a��rl�klar�)
    while len (se�ilenK�me) < k:
        se�ilen = a��rl�kl�Tercih (listem, a��rl�klar�)
        if se�ilen not in se�ilenK�me: se�ilenK�me.add (se�ilen)
        # Se�ilen tekrar se�ilmi�se k�meye eklenmez...
    return list (se�ilenK�me)

def a��rl�kl�Tercih (zarY�zleri, gelmeA��rl�klar�, kriptoluMu=True):
    if kriptoluMu: x = random.SystemRandom().random()
    else: x = np.random.random()
    gelmeY�zdeleriToplam� = [0] + list (np.cumsum (gelmeA��rl�klar�))
    endeks = ka��nc�Arada (x, gelmeY�zdeleriToplam�)
    return zarY�zleri[endeks]

def ka��nc�Arada (de�erim, b�l�mler, u�lar_1Mi=True):
    for i in range (0, len (b�l�mler)):
        if de�erim < b�l�mler[i]: return i-1 if u�lar_1Mi else i
    return -1 if u�lar_1Mi else len (b�l�mler)


amazonAdaylar = ["Airla", "Barbara", "Eos", "Glykeria", "Hanna", "Helen",
    "Agathangelos", "Iokaste", "Medousa", "Sofronia", "Andromeda"]
"""3 farkl� y�ntem i�lem s�resini gittikce k�salt�r...
de�i�enA��rl�klar = [1 / len (amazonAdaylar) for _ in range (len (amazonAdaylar))] # 11'i de e�it=1/11...

from fractions import Fraction
de�i�enA��rl�klar = [Fraction (1, 11) for _ in range (len (amazonAdaylar))]
"""
de�i�enA��rl�klar = np.full (11, 1 / len (amazonAdaylar))
PytheussesFavorileri = {"Iokaste", "Medousa", "Sofronia", "Andromeda"}

try: kere = abs (int (input ("Herg�n se�ilecek 4'l� �ekili� say�s� [1 000]? ")))
except: kere = 1000

saya� = 0
ihtimal = 1 / 330 # %03 (binde 3)...
ge�enG�nler = 0
fakt�r1 = 1 / 13 # Herg�n favori olmayan ilk yediliden d���lecek a��rl�k...
fakt�r2 = 1 / 12 # Herg�n favori son d�rtl�s�ne eklenecek a��rl�k...
ba�lat = pt()

print ("\nBa�lang�� a��rl�klar: %", [int (a * 10000) / 100 for a in de�i�enA��rl�klar])
while ihtimal < 0.9: # y�zde 90 (herg�n 1 d�ng�)...
    for i in range (kere): # �stenen, 1000 tesad�fi se�imden enaz 900 favori d�rtl� k�mesi ��kmas�...
        se�ilenD�rtl� = a��rl�kl��rnekleme2 (amazonAdaylar, de�i�enA��rl�klar, 4)
        if set (se�ilenD�rtl�) == PytheussesFavorileri: saya� += 1
    ihtimal = saya� / kere # ihtimal=900/1000: son...
    saya� = 0
    de�i�enA��rl�klar[:7] = [ a��r - a��r*fakt�r1 for a��r in de�i�enA��rl�klar[:7] ]
    de�i�enA��rl�klar[7:] = [ ihtimal + ihtimal*fakt�r2 for ihtimal in de�i�enA��rl�klar[7:] ]
    de�i�enA��rl�klar = [ a / sum (de�i�enA��rl�klar) for a in de�i�enA��rl�klar]
    ge�enG�nler += 1

print ("Sonu� a��rl�klar: %", [int (a * 10000) / 100 for a in de�i�enA��rl�klar])
print ("��lem s�resi (sn):", int ((pt() - ba�lat) * 100) / 100)
print ("Pytheusses'un %90 emin olabilmesi i�in ge�en g�n say�s�: ", ge�enG�nler)



"""��kt�:
>python p_30712c.py
Herg�n se�ilecek 4'l� �ekili� say�s� [1 000]? 1

Ba�lang�� a��rl�klar: % [9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09]
Sonu� a��rl�klar: % [3.72, 3.72, 3.72, 3.72, 3.72, 3.72, 3.72, 18.47, 18.47, 18.47, 18.47]
��lem s�resi (sn): 0.04
Pytheusses'un %90 emin olabilmesi i�in ge�en g�n say�s�:  10

>python p_30712c.py  ** TEKRAR **
Herg�n se�ilecek 4'l� �ekili� say�s� [1 000]? 10

Ba�lang�� a��rl�klar: % [9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09]
Sonu� a��rl�klar: % [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 23.94, 23.94, 23.94, 23.94]
��lem s�resi (sn): 0.98
Pytheusses'un %90 emin olabilmesi i�in ge�en g�n say�s�:  23

>python p_30712c.py  ** TEKRAR **
Herg�n se�ilecek 4'l� �ekili� say�s� [1 000]? 100

Ba�lang�� a��rl�klar: % [9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09]
Sonu� a��rl�klar: % [0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 24.74, 24.74, 24.74, 24.74]
��lem s�resi (sn): 6.13
Pytheusses'un %90 emin olabilmesi i�in ge�en g�n say�s�:  32

>python p_30712c.py  ** TEKRAR **
Herg�n se�ilecek 4'l� �ekili� say�s� [1 000]?

Ba�lang�� a��rl�klar: % [9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09]
Sonu� a��rl�klar: % [0.17, 0.17, 0.17, 0.17, 0.17, 0.17, 0.17, 24.69, 24.69, 24.69, 24.69]
��lem s�resi (sn): 44.19
Pytheusses'un %90 emin olabilmesi i�in ge�en g�n say�s�:  31
"""