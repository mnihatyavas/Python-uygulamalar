# coding:iso-8859-9 T�rk�e
# p_12501.py: ��i�e fonksiyonlar�n i�letilme kurallar� �rne�i.

def sonras� (x): return x+1

sonraki = sonras� # Fonksiyona ba�ka bir ad daha atayal�m...

print ("10'dan sonras�:", sonras� (10) )

del sonras� # �lk fonksiyon ad�n� silelim...
try: print ("10'dan sonras�:", sonras� (10) ) # Fonksiyon 1.adla art�k �a�r�lamaz...
except Exception as ist: print ("HATA:", ist)

print ("\n10'dan sonras�:", sonraki (10) ) # Fonksiyon 2.adla hala mevcuttur...
print ("-"*70)
#-----------------------------------------��i�e fonksiyonlar--------------------------------------

def fonk1():
    def fonk2():
        print ("\nMerhaba, ben fonk2()'yim")
        print ("Beni �a��rd���n�z i�in te�ekk�rler")
    print ("\nSelam, ben fonk1()'im")
    print ("Ve �imdi de fonk2()'yi �a��r�yorum:")
    fonk2()
    print ("\nVe tekrar fonk1()'e ��kt�m")

fonk1()
print ("-"*70, "\n")
#--------------------------------------------------------------------------------------------------------

from random import random, randint

def selsiy�s (d):
    def selsiy�stenfahrenhayta (x): return 9 * x / 5 + 32
    return str (d) + " selsiy�s = " + str (selsiy�stenfahrenhayta (d) ) + " fahrenhayt derecedir."

�s� = randint (-273, 1000) + random()
print (selsiy�s (�s�))


"""��kt�:
>python p_12501.py
10'dan sonras�: 11
HATA: name 'sonras�' is not defined

10'dan sonras�: 11
----------------------------------------------------------------------

Selam, ben fonk1()'im
Ve �imdi de fonk2()'yi �a��r�yorum:

Merhaba, ben fonk2()'yim
Beni �a��rd���n�z i�in te�ekk�rler

Ve tekrar fonk1()'e ��kt�m
----------------------------------------------------------------------

-164.33449116905786 selsiy�s = -263.80208410430413 fahrenhayt derecedir.
"""