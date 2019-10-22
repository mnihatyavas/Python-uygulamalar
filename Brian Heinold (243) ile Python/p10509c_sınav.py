# coding:iso-8859-9 Türkçe

from random import randint
from math import *

kere = abs (trunc (eval (input ("Kaç kere denemek istersin [2,10000]: "))))
if kere < 2: kere = 2
if kere > 10000: kere = 10000
kazandı1=kaybetti1=kazandı2=kaybetti2=değiştirdi=değiştirmedi=0
for i in range (kere):
    hediyeli_kapı = randint (1,3)
    misafir = randint (1,3)
    if hediyeli_kapı==1:
        if misafir==1:
            if randint (0,1): kaybetti1+=1; değiştirdi+=1 # misafir değiştirdi
            else: kazandı2+=1; değiştirmedi+=1
        else:
           if randint (0,1): kazandı1+=1; değiştirdi+=1 # misafir değiştirdi
           else: kaybetti2+=1; değiştirmedi+=1
    elif hediyeli_kapı==2:
        if misafir==2:
            if randint (0,1): kaybetti1+=1; değiştirdi+=1 # misafir değiştirdi
            else: kazandı2+=1; değiştirmedi+=1
        else:
            if randint (0,1): kazandı1+=1; değiştirdi+=1 # misafir değiştirdi
            else: kaybetti2+=1; değiştirmedi+=1
    else: # hediyeli_kapı==3:
        if misafir==3:
            if randint (0,1): kaybetti1+=1; değiştirdi+=1 # misafir değiştirdi
            else: kazandı2+=1; değiştirmedi+=1
        else:
            if randint (0,1): kazandı1+=1; değiştirdi+=1 # misafir değiştirdi
            else: kaybetti2+=1; değiştirmedi+=1

print (kere, "oyunda", değiştirdi, round ((değiştirdi/kere)*100, 2),
    " % kez değiştirdi;", kazandı1, round ((kazandı1/değiştirdi)*100, 2),
    "% kere kazandı", kaybetti1, round ((kaybetti1/değiştirdi)*100, 2),
    "% kere kaybetti")
print (kere, "oyunda", değiştirmedi, round ((değiştirmedi/kere)*100, 2),
    "% kez değiştirmedi;", kazandı2, round ((kazandı2/değiştirmedi)*100, 2),
    "% kere kazandı", kaybetti2, round ((kaybetti2/değiştirmedi)*100, 2),
    "% kere kaybetti")
