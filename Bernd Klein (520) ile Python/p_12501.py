# coding:iso-8859-9 Türkçe
# p_12501.py: İçiçe fonksiyonların işletilme kuralları örneği.

def sonrası (x): return x+1

sonraki = sonrası # Fonksiyona başka bir ad daha atayalım...

print ("10'dan sonrası:", sonrası (10) )

del sonrası # İlk fonksiyon adını silelim...
try: print ("10'dan sonrası:", sonrası (10) ) # Fonksiyon 1.adla artık çağrılamaz...
except Exception as ist: print ("HATA:", ist)

print ("\n10'dan sonrası:", sonraki (10) ) # Fonksiyon 2.adla hala mevcuttur...
print ("-"*70)
#-----------------------------------------İçiçe fonksiyonlar--------------------------------------

def fonk1():
    def fonk2():
        print ("\nMerhaba, ben fonk2()'yim")
        print ("Beni çağırdığınız için teşekkürler")
    print ("\nSelam, ben fonk1()'im")
    print ("Ve şimdi de fonk2()'yi çağırıyorum:")
    fonk2()
    print ("\nVe tekrar fonk1()'e çıktım")

fonk1()
print ("-"*70, "\n")
#--------------------------------------------------------------------------------------------------------

from random import random, randint

def selsiyüs (d):
    def selsiyüstenfahrenhayta (x): return 9 * x / 5 + 32
    return str (d) + " selsiyüs = " + str (selsiyüstenfahrenhayta (d) ) + " fahrenhayt derecedir."

ısı = randint (-273, 1000) + random()
print (selsiyüs (ısı))


"""Çıktı:
>python p_12501.py
10'dan sonrası: 11
HATA: name 'sonrası' is not defined

10'dan sonrası: 11
----------------------------------------------------------------------

Selam, ben fonk1()'im
Ve şimdi de fonk2()'yi çağırıyorum:

Merhaba, ben fonk2()'yim
Beni çağırdığınız için teşekkürler

Ve tekrar fonk1()'e çıktım
----------------------------------------------------------------------

-164.33449116905786 selsiyüs = -263.80208410430413 fahrenhayt derecedir.
"""