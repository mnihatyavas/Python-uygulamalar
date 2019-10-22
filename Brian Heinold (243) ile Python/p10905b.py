#coding:iso-8859-9 Türkçe

from random import randint
tesadüfi = randint (0,100)
kere=tahmin = alt = 0
üst = 100
for i in range (10):
    if tahmin > alt:
        try:
            tahmin = eval (input ("Tahmininiz (" + str (tahmin - (üst - alt)//2) + "): "))
            if tahmin > üst or tahmin < alt:
                tahmin = randint (alt, üst)
        except Exception: tahmin -= (üst - alt)//2
    else:
        try:
            tahmin = eval (input ("Tahmininiz (" + str (tahmin + (üst - alt)//2) + "): "))
            if tahmin > üst or tahmin < alt:
                tahmin = randint (alt, üst)
        except Exception: tahmin += (üst - alt)//2
    kere +=1
    if tahmin < tesadüfi: print (kere, ": DAHA YÜKSEK [", tahmin, "->", üst, "] GİR", sep=""); alt = tahmin
    elif tahmin > tesadüfi: print (kere, ": DAHA DÜŞÜK [", alt, "->", tahmin, "] GİR", sep=""); üst = tahmin
    else: print ("BRAVO! ", kere, '.tahminde ', tesadüfi, "'yi buldunuz.", sep=""); break

else: print ('\nMaalesef KAYBETTİNİZ. Doğru tahmin', tesadüfi, "olmalıydı!")
