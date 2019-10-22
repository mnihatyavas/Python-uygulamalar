# coding:iso-8859-9 Türkçe
# p_12502.py: Parametrik ve içiçe fonksiyonların birlikte işletilmesi örneği.

def fonk1():
    print ("\nSelam, ben parametrik fonksiyon fonk1()'im")
    print ("Beni çağırdığınız için teşekkürler")
    
def fonk2 (fonksiyon):
    print ("Merhaba, ben fonk2(fonksiyon)'yim")
    print ("Ve şimdi parametrik fonksiyon'umu çağıracağım:")
    fonksiyon()
    print ("\nVe tekrar fonk2(fonksiyon)'ye devam ediyoruz")
    print ("Ha, bu arada parametrik fonksiyon'umun adı: ", fonksiyon.__name__, "()'dir", sep="")

fonk2 (fonk1)
print ("-"*70, "\n")
#---------------------------------------------------------------------------------------------------------

from math import sin, cos, pi

def fonk (f):
    def radyan (a): return a*pi/180
    print (f.__name__ + " fonksiyonu parametre olarak fonk(f)'a geçti")
    for x in range (0, 361, 30): print ("{}({}) = {:.2f}" .format (f.__name__, x, f (radyan (x)) ) )
    print()

fonk (sin)
fonk (cos)


"""Çıktı:
>python p_12502.py
Merhaba, ben fonk2(fonksiyon)'yim
Ve şimdi parametrik fonksiyon'umu çağıracağım:

Selam, ben parametrik fonksiyon fonk1()'im
Beni çağırdığınız için teşekkürler

Ve tekrar fonk2(fonksiyon)'ye devam ediyoruz
Ha, bu arada parametrik fonksiyon'umun adı: fonk1()'dir
----------------------------------------------------------------------

sin fonksiyonu parametre olarak fonk(f)'a geçti
sin(0) = 0.00
sin(30) = 0.50
sin(60) = 0.87
sin(90) = 1.00
sin(120) = 0.87
sin(150) = 0.50
sin(180) = 0.00
sin(210) = -0.50
sin(240) = -0.87
sin(270) = -1.00
sin(300) = -0.87
sin(330) = -0.50
sin(360) = -0.00

cos fonksiyonu parametre olarak fonk(f)'a geçti
cos(0) = 1.00
cos(30) = 0.87
cos(60) = 0.50
cos(90) = 0.00
cos(120) = -0.50
cos(150) = -0.87
cos(180) = -1.00
cos(210) = -0.87
cos(240) = -0.50
cos(270) = -0.00
cos(300) = 0.50
cos(330) = 0.87
cos(360) = 1.00
"""