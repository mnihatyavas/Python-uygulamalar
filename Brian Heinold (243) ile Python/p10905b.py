#coding:iso-8859-9 T�rk�e

from random import randint
tesad�fi = randint (0,100)
kere=tahmin = alt = 0
�st = 100
for i in range (10):
    if tahmin > alt:
        try:
            tahmin = eval (input ("Tahmininiz (" + str (tahmin - (�st - alt)//2) + "): "))
            if tahmin > �st or tahmin < alt:
                tahmin = randint (alt, �st)
        except Exception: tahmin -= (�st - alt)//2
    else:
        try:
            tahmin = eval (input ("Tahmininiz (" + str (tahmin + (�st - alt)//2) + "): "))
            if tahmin > �st or tahmin < alt:
                tahmin = randint (alt, �st)
        except Exception: tahmin += (�st - alt)//2
    kere +=1
    if tahmin < tesad�fi: print (kere, ": DAHA Y�KSEK [", tahmin, "->", �st, "] G�R", sep=""); alt = tahmin
    elif tahmin > tesad�fi: print (kere, ": DAHA D���K [", alt, "->", tahmin, "] G�R", sep=""); �st = tahmin
    else: print ("BRAVO! ", kere, '.tahminde ', tesad�fi, "'yi buldunuz.", sep=""); break

else: print ('\nMaalesef KAYBETT�N�Z. Do�ru tahmin', tesad�fi, "olmal�yd�!")
