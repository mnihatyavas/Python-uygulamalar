# coding:iso-8859-9 Türkçe
# p_12505.py: Aynı dekoratörde farklı fonksiyonlar, hazır fonksiyonlar ve farklı sayıda argümanlar örneği.

def dekoratörüm (fonksiyon):
    def argümansal_fonksiyon_ambalajlayıcısı (x):
        print()
        print (fonksiyon.__name__ + " adlı fonksiyonu çağırmadan önce")
        sonuç = fonksiyon (x)
        print (sonuç)
        print (fonksiyon.__name__ + " adlı fonksiyonu çağırdıktan sonra")
    return argümansal_fonksiyon_ambalajlayıcısı

# Artık dekoratörüm her farklı adlı (argüman) fonksiyonla çağrılabilir...
@dekoratörüm
def bir_sonrası (n): return str (n) + "+1=" + str (n + 1)

@dekoratörüm
def karesi (n): return str (n) + "^2=" + str (n**2)

@dekoratörüm
def karekökü (n): return str (n) + "^(1/2)=" + str (n**(1/2))

bir_sonrası (10)
karesi (9)
karekökü (88)
print ("_"*75, "\n")
#---------------------------------------------------------------------------------------------------

from math import sin, cos, pi

print ("import hazır tanımlı fonksiyonlar @'siz, ve atamayla çağrılmalıdır!")
sinüs = dekoratörüm (sin)
#kosinüs = dekoratörüm (cos)

for derece in range (0, 361, 15):
    radyan = derece * pi / 180 
    print ("\nsin(", derece, ")=", sep="", end="")
    sinüs (radyan)
print ("_"*75, "\n")
#---------------------------------------------------------------------------------------------------

from random import random, randint, choice

def dekoratör (f):
    def ambalajcı (*a, **b): # Argümansız veya çoklu argümanlı olabilir...
        print()
        print (f.__name__ + " adlı değişken argümansal fonksiyon çağrılmadan önce")
        sonuç = f (*a, **b)
        print (sonuç)
        print (f.__name__ + " adlı değişken argümansal fonksiyon çağrıldıktan sonra")
    return ambalajcı

print ("\nArtık ambalajcı değişken sayılı argümanla da çağrılabilmektedir:")
küsüratlı = dekoratör (random)
tamsayılı = dekoratör (randint)
tercihli = dekoratör (choice)

print ("[0->1] arası tesadüfi sayı (argümansız):", end=""); küsüratlı ()
print ("\n[-100->100] arası tesadüfi sayı (2 argümanlı):", end=""); tamsayılı (-100, 100)
print ("\n[-1000->1000] arası 100 adet choice sayı (100 argümanlı):", end=""); tercihli ([randint (-1000, 1000) for i in range (100)] )



"""Çıktı:
>python p_12505.py

bir_sonrası adlı fonksiyonu çağırmadan önce
10+1=11
bir_sonrası adlı fonksiyonu çağırdıktan sonra

karesi adlı fonksiyonu çağırmadan önce
9^2=81
karesi adlı fonksiyonu çağırdıktan sonra

karekökü adlı fonksiyonu çağırmadan önce
88^(1/2)=9.38083151964686
karekökü adlı fonksiyonu çağırdıktan sonra
___________________________________________________________________________

import hazır tanımlı fonksiyonlar @'siz, ve atamayla çağrılmalıdır!

sin(0)=
sin adlı fonksiyonu çağırmadan önce
0.0
sin adlı fonksiyonu çağırdıktan sonra

sin(15)=
sin adlı fonksiyonu çağırmadan önce
0.25881904510252074
sin adlı fonksiyonu çağırdıktan sonra

sin(30)=
sin adlı fonksiyonu çağırmadan önce
0.49999999999999994
sin adlı fonksiyonu çağırdıktan sonra

sin(45)=
sin adlı fonksiyonu çağırmadan önce
0.7071067811865475
sin adlı fonksiyonu çağırdıktan sonra

sin(60)=
sin adlı fonksiyonu çağırmadan önce
0.8660254037844386
sin adlı fonksiyonu çağırdıktan sonra

sin(75)=
sin adlı fonksiyonu çağırmadan önce
0.9659258262890683
sin adlı fonksiyonu çağırdıktan sonra

sin(90)=
sin adlı fonksiyonu çağırmadan önce
1.0
sin adlı fonksiyonu çağırdıktan sonra

sin(105)=
sin adlı fonksiyonu çağırmadan önce
0.9659258262890683
sin adlı fonksiyonu çağırdıktan sonra

sin(120)=
sin adlı fonksiyonu çağırmadan önce
0.8660254037844387
sin adlı fonksiyonu çağırdıktan sonra

sin(135)=
sin adlı fonksiyonu çağırmadan önce
0.7071067811865476
sin adlı fonksiyonu çağırdıktan sonra

sin(150)=
sin adlı fonksiyonu çağırmadan önce
0.49999999999999994
sin adlı fonksiyonu çağırdıktan sonra

sin(165)=
sin adlı fonksiyonu çağırmadan önce
0.258819045102521
sin adlı fonksiyonu çağırdıktan sonra

sin(180)=
sin adlı fonksiyonu çağırmadan önce
1.2246467991473532e-16
sin adlı fonksiyonu çağırdıktan sonra

sin(195)=
sin adlı fonksiyonu çağırmadan önce
-0.25881904510252035
sin adlı fonksiyonu çağırdıktan sonra

sin(210)=
sin adlı fonksiyonu çağırmadan önce
-0.5000000000000001
sin adlı fonksiyonu çağırdıktan sonra

sin(225)=
sin adlı fonksiyonu çağırmadan önce
-0.7071067811865475
sin adlı fonksiyonu çağırdıktan sonra

sin(240)=
sin adlı fonksiyonu çağırmadan önce
-0.8660254037844384
sin adlı fonksiyonu çağırdıktan sonra

sin(255)=
sin adlı fonksiyonu çağırmadan önce
-0.9659258262890683
sin adlı fonksiyonu çağırdıktan sonra

sin(270)=
sin adlı fonksiyonu çağırmadan önce
-1.0
sin adlı fonksiyonu çağırdıktan sonra

sin(285)=
sin adlı fonksiyonu çağırmadan önce
-0.9659258262890682
sin adlı fonksiyonu çağırdıktan sonra

sin(300)=
sin adlı fonksiyonu çağırmadan önce
-0.8660254037844386
sin adlı fonksiyonu çağırdıktan sonra

sin(315)=
sin adlı fonksiyonu çağırmadan önce
-0.7071067811865477
sin adlı fonksiyonu çağırdıktan sonra

sin(330)=
sin adlı fonksiyonu çağırmadan önce
-0.5000000000000004
sin adlı fonksiyonu çağırdıktan sonra

sin(345)=
sin adlı fonksiyonu çağırmadan önce
-0.2588190451025207
sin adlı fonksiyonu çağırdıktan sonra

sin(360)=
sin adlı fonksiyonu çağırmadan önce
-2.4492935982947064e-16
sin adlı fonksiyonu çağırdıktan sonra
___________________________________________________________________________


Artık ambalajcı değişken sayılı argümanla da çağrılabilmektedir:
[0->1] arası tesadüfi sayı (argümansız):
random adlı değişken argümansal fonksiyon çağrılmadan önce
0.8830365377014282
random adlı değişken argümansal fonksiyon çağrıldıktan sonra

[-100->100] arası tesadüfi sayı (2 argümanlı):
randint adlı değişken argümansal fonksiyon çağrılmadan önce
-73
randint adlı değişken argümansal fonksiyon çağrıldıktan sonra

[-1000->1000] arası 100 adet choice sayı (100 argümanlı):
choice adlı değişken argümansal fonksiyon çağrılmadan önce
-789
choice adlı değişken argümansal fonksiyon çağrıldıktan sonra
"""