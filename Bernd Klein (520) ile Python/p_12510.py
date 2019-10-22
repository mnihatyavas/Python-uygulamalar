# coding:iso-8859-9 T�rk�e
# p_12510.py: Dekorat�rl� @ fonksiyon ve s�n�f�n�n kar��la�t�r�lmas� �rne�i.

def dekorat�r1 (f):
    def yard�mc� (x):
        print (f.__name__ + " adl� fonksiyonu dekore ediyorum")
        f (x)
    return yard�mc�

@dekorat�r1
def fonk (a): print (a, "mutlak say�s�n�n karek�k�:", abs (a**(1/2)) )

print ("Karek�k i�lemini ola�an dekorat�r fonksiyonuyla yap�yorum==>")
t�ple = (-1.25, 2, -45.89, 9, 0)
for (i, j) in enumerate (t�ple):
    print ("\n", i+1, ": ", sep="", end="")
    fonk (j)
print ("-"*75, "\n")
#---------------------------------------------------------------------------------------------------------

class dekorat�r2:
    def __init__ (self, f): self.f1 = f
    def __call__ (self, b):
        print (self.f1.__name__ + " adl� fonksiyonu dekore ediyorum")
        self.f1 (b)

@dekorat�r2
def fonk1 (a): print (a, "mutlak say�s�n�n karek�k�:", abs (a**(1/2)) )

print ("�imdi de ayn� i�lemi dekorat�r s�n�f�yla ger�ekle�tiriyorum==>")
for (i, j) in enumerate (t�ple):
    print ("\n", i+1, ": ", sep="", end="")
    fonk1 (j)



"""��kt�:
>python p_12510.py
Karek�k i�lemini ola�an dekorat�r fonksiyonuyla yap�yorum==>

1:fonk adl� fonksiyonu dekore ediyorum
-1.25 mutlak say�s�n�n karek�k�: 1.118033988749895

2:fonk adl� fonksiyonu dekore ediyorum
2 mutlak say�s�n�n karek�k�: 1.4142135623730951

3:fonk adl� fonksiyonu dekore ediyorum
-45.89 mutlak say�s�n�n karek�k�: 6.774215821775979

4:fonk adl� fonksiyonu dekore ediyorum
9 mutlak say�s�n�n karek�k�: 3.0

5:fonk adl� fonksiyonu dekore ediyorum
0 mutlak say�s�n�n karek�k�: 0.0
---------------------------------------------------------------------------

�imdi de ayn� i�lemi dekorat�r s�n�f�yla ger�ekle�tiriyorum==>

1:fonk1 adl� fonksiyonu dekore ediyorum
-1.25 mutlak say�s�n�n karek�k�: 1.118033988749895

2:fonk1 adl� fonksiyonu dekore ediyorum
2 mutlak say�s�n�n karek�k�: 1.4142135623730951

3:fonk1 adl� fonksiyonu dekore ediyorum
-45.89 mutlak say�s�n�n karek�k�: 6.774215821775979

4:fonk1 adl� fonksiyonu dekore ediyorum
9 mutlak say�s�n�n karek�k�: 3.0

5:fonk1 adl� fonksiyonu dekore ediyorum
0 mutlak say�s�n�n karek�k�: 0.0
"""