# coding:iso-8859-9 T�rk�e

from random import randint
from math import *

kere = abs (trunc (eval (input ("Ka� kere denemek istersin [2,10000]: "))))
if kere < 2: kere = 2
if kere > 10000: kere = 10000
kazand�1=kaybetti1=kazand�2=kaybetti2=de�i�tirdi=de�i�tirmedi=0
for i in range (kere):
    hediyeli_kap� = randint (1,3)
    misafir = randint (1,3)
    if hediyeli_kap�==1:
        if misafir==1:
            if randint (0,1): kaybetti1+=1; de�i�tirdi+=1 # misafir de�i�tirdi
            else: kazand�2+=1; de�i�tirmedi+=1
        else:
           if randint (0,1): kazand�1+=1; de�i�tirdi+=1 # misafir de�i�tirdi
           else: kaybetti2+=1; de�i�tirmedi+=1
    elif hediyeli_kap�==2:
        if misafir==2:
            if randint (0,1): kaybetti1+=1; de�i�tirdi+=1 # misafir de�i�tirdi
            else: kazand�2+=1; de�i�tirmedi+=1
        else:
            if randint (0,1): kazand�1+=1; de�i�tirdi+=1 # misafir de�i�tirdi
            else: kaybetti2+=1; de�i�tirmedi+=1
    else: # hediyeli_kap�==3:
        if misafir==3:
            if randint (0,1): kaybetti1+=1; de�i�tirdi+=1 # misafir de�i�tirdi
            else: kazand�2+=1; de�i�tirmedi+=1
        else:
            if randint (0,1): kazand�1+=1; de�i�tirdi+=1 # misafir de�i�tirdi
            else: kaybetti2+=1; de�i�tirmedi+=1

print (kere, "oyunda", de�i�tirdi, round ((de�i�tirdi/kere)*100, 2),
    " % kez de�i�tirdi;", kazand�1, round ((kazand�1/de�i�tirdi)*100, 2),
    "% kere kazand�", kaybetti1, round ((kaybetti1/de�i�tirdi)*100, 2),
    "% kere kaybetti")
print (kere, "oyunda", de�i�tirmedi, round ((de�i�tirmedi/kere)*100, 2),
    "% kez de�i�tirmedi;", kazand�2, round ((kazand�2/de�i�tirmedi)*100, 2),
    "% kere kazand�", kaybetti2, round ((kaybetti2/de�i�tirmedi)*100, 2),
    "% kere kaybetti")
