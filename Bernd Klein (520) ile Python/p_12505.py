# coding:iso-8859-9 T�rk�e
# p_12505.py: Ayn� dekorat�rde farkl� fonksiyonlar, haz�r fonksiyonlar ve farkl� say�da arg�manlar �rne�i.

def dekorat�r�m (fonksiyon):
    def arg�mansal_fonksiyon_ambalajlay�c�s� (x):
        print()
        print (fonksiyon.__name__ + " adl� fonksiyonu �a��rmadan �nce")
        sonu� = fonksiyon (x)
        print (sonu�)
        print (fonksiyon.__name__ + " adl� fonksiyonu �a��rd�ktan sonra")
    return arg�mansal_fonksiyon_ambalajlay�c�s�

# Art�k dekorat�r�m her farkl� adl� (arg�man) fonksiyonla �a�r�labilir...
@dekorat�r�m
def bir_sonras� (n): return str (n) + "+1=" + str (n + 1)

@dekorat�r�m
def karesi (n): return str (n) + "^2=" + str (n**2)

@dekorat�r�m
def karek�k� (n): return str (n) + "^(1/2)=" + str (n**(1/2))

bir_sonras� (10)
karesi (9)
karek�k� (88)
print ("_"*75, "\n")
#---------------------------------------------------------------------------------------------------

from math import sin, cos, pi

print ("import haz�r tan�ml� fonksiyonlar @'siz, ve atamayla �a�r�lmal�d�r!")
sin�s = dekorat�r�m (sin)
#kosin�s = dekorat�r�m (cos)

for derece in range (0, 361, 15):
    radyan = derece * pi / 180 
    print ("\nsin(", derece, ")=", sep="", end="")
    sin�s (radyan)
print ("_"*75, "\n")
#---------------------------------------------------------------------------------------------------

from random import random, randint, choice

def dekorat�r (f):
    def ambalajc� (*a, **b): # Arg�mans�z veya �oklu arg�manl� olabilir...
        print()
        print (f.__name__ + " adl� de�i�ken arg�mansal fonksiyon �a�r�lmadan �nce")
        sonu� = f (*a, **b)
        print (sonu�)
        print (f.__name__ + " adl� de�i�ken arg�mansal fonksiyon �a�r�ld�ktan sonra")
    return ambalajc�

print ("\nArt�k ambalajc� de�i�ken say�l� arg�manla da �a�r�labilmektedir:")
k�s�ratl� = dekorat�r (random)
tamsay�l� = dekorat�r (randint)
tercihli = dekorat�r (choice)

print ("[0->1] aras� tesad�fi say� (arg�mans�z):", end=""); k�s�ratl� ()
print ("\n[-100->100] aras� tesad�fi say� (2 arg�manl�):", end=""); tamsay�l� (-100, 100)
print ("\n[-1000->1000] aras� 100 adet choice say� (100 arg�manl�):", end=""); tercihli ([randint (-1000, 1000) for i in range (100)] )



"""��kt�:
>python p_12505.py

bir_sonras� adl� fonksiyonu �a��rmadan �nce
10+1=11
bir_sonras� adl� fonksiyonu �a��rd�ktan sonra

karesi adl� fonksiyonu �a��rmadan �nce
9^2=81
karesi adl� fonksiyonu �a��rd�ktan sonra

karek�k� adl� fonksiyonu �a��rmadan �nce
88^(1/2)=9.38083151964686
karek�k� adl� fonksiyonu �a��rd�ktan sonra
___________________________________________________________________________

import haz�r tan�ml� fonksiyonlar @'siz, ve atamayla �a�r�lmal�d�r!

sin(0)=
sin adl� fonksiyonu �a��rmadan �nce
0.0
sin adl� fonksiyonu �a��rd�ktan sonra

sin(15)=
sin adl� fonksiyonu �a��rmadan �nce
0.25881904510252074
sin adl� fonksiyonu �a��rd�ktan sonra

sin(30)=
sin adl� fonksiyonu �a��rmadan �nce
0.49999999999999994
sin adl� fonksiyonu �a��rd�ktan sonra

sin(45)=
sin adl� fonksiyonu �a��rmadan �nce
0.7071067811865475
sin adl� fonksiyonu �a��rd�ktan sonra

sin(60)=
sin adl� fonksiyonu �a��rmadan �nce
0.8660254037844386
sin adl� fonksiyonu �a��rd�ktan sonra

sin(75)=
sin adl� fonksiyonu �a��rmadan �nce
0.9659258262890683
sin adl� fonksiyonu �a��rd�ktan sonra

sin(90)=
sin adl� fonksiyonu �a��rmadan �nce
1.0
sin adl� fonksiyonu �a��rd�ktan sonra

sin(105)=
sin adl� fonksiyonu �a��rmadan �nce
0.9659258262890683
sin adl� fonksiyonu �a��rd�ktan sonra

sin(120)=
sin adl� fonksiyonu �a��rmadan �nce
0.8660254037844387
sin adl� fonksiyonu �a��rd�ktan sonra

sin(135)=
sin adl� fonksiyonu �a��rmadan �nce
0.7071067811865476
sin adl� fonksiyonu �a��rd�ktan sonra

sin(150)=
sin adl� fonksiyonu �a��rmadan �nce
0.49999999999999994
sin adl� fonksiyonu �a��rd�ktan sonra

sin(165)=
sin adl� fonksiyonu �a��rmadan �nce
0.258819045102521
sin adl� fonksiyonu �a��rd�ktan sonra

sin(180)=
sin adl� fonksiyonu �a��rmadan �nce
1.2246467991473532e-16
sin adl� fonksiyonu �a��rd�ktan sonra

sin(195)=
sin adl� fonksiyonu �a��rmadan �nce
-0.25881904510252035
sin adl� fonksiyonu �a��rd�ktan sonra

sin(210)=
sin adl� fonksiyonu �a��rmadan �nce
-0.5000000000000001
sin adl� fonksiyonu �a��rd�ktan sonra

sin(225)=
sin adl� fonksiyonu �a��rmadan �nce
-0.7071067811865475
sin adl� fonksiyonu �a��rd�ktan sonra

sin(240)=
sin adl� fonksiyonu �a��rmadan �nce
-0.8660254037844384
sin adl� fonksiyonu �a��rd�ktan sonra

sin(255)=
sin adl� fonksiyonu �a��rmadan �nce
-0.9659258262890683
sin adl� fonksiyonu �a��rd�ktan sonra

sin(270)=
sin adl� fonksiyonu �a��rmadan �nce
-1.0
sin adl� fonksiyonu �a��rd�ktan sonra

sin(285)=
sin adl� fonksiyonu �a��rmadan �nce
-0.9659258262890682
sin adl� fonksiyonu �a��rd�ktan sonra

sin(300)=
sin adl� fonksiyonu �a��rmadan �nce
-0.8660254037844386
sin adl� fonksiyonu �a��rd�ktan sonra

sin(315)=
sin adl� fonksiyonu �a��rmadan �nce
-0.7071067811865477
sin adl� fonksiyonu �a��rd�ktan sonra

sin(330)=
sin adl� fonksiyonu �a��rmadan �nce
-0.5000000000000004
sin adl� fonksiyonu �a��rd�ktan sonra

sin(345)=
sin adl� fonksiyonu �a��rmadan �nce
-0.2588190451025207
sin adl� fonksiyonu �a��rd�ktan sonra

sin(360)=
sin adl� fonksiyonu �a��rmadan �nce
-2.4492935982947064e-16
sin adl� fonksiyonu �a��rd�ktan sonra
___________________________________________________________________________


Art�k ambalajc� de�i�ken say�l� arg�manla da �a�r�labilmektedir:
[0->1] aras� tesad�fi say� (arg�mans�z):
random adl� de�i�ken arg�mansal fonksiyon �a�r�lmadan �nce
0.8830365377014282
random adl� de�i�ken arg�mansal fonksiyon �a�r�ld�ktan sonra

[-100->100] aras� tesad�fi say� (2 arg�manl�):
randint adl� de�i�ken arg�mansal fonksiyon �a�r�lmadan �nce
-73
randint adl� de�i�ken arg�mansal fonksiyon �a�r�ld�ktan sonra

[-1000->1000] aras� 100 adet choice say� (100 arg�manl�):
choice adl� de�i�ken arg�mansal fonksiyon �a�r�lmadan �nce
-789
choice adl� de�i�ken arg�mansal fonksiyon �a�r�ld�ktan sonra
"""