# coding:iso-8859-9 T�rk�e
# p_14902.py: Soyut s�n�f�n t�m soyut metodlar�n� esge�en somut s�n�f nesneleri �rne�i.

from abc import ABC, abstractmethod
# Python k�t�phanesinde haz�r abc.py, ABC/AbstractBaseClass: SoyutTemelS�n�f
 
class SoyutS�n�f (ABC): # Bir soyut metod i�eren soyut s�n�f...
    def __init__ (self, de�er):
        self.de�er = de�er
        super().__init__()
    @abstractmethod
    def soyutMetod (self): pass
class SomutS�n�f (SoyutS�n�f): pass

# a = SoyutS�n�f() ==> Soyut s�n�f tiplenemez (TypeError)...
# b = SomutS�n�f (42) ==> Soyut s�n�f�n t�m soyut metodlar�n� override/esge�meyen tipleme olmaz (TypeError)...

class SomutS�n�f1 (SoyutS�n�f):
    def soyutMetod (self): return self.de�er**2
class SomutS�n�f2 (SoyutS�n�f):
    def soyutMetod (self): return self.de�er**0.5

a = SomutS�n�f1 (42)
b = SomutS�n�f2 (42)

print ("42'nin karesi =", a.soyutMetod() )
print ("42'nin karek�k� =", b.soyutMetod() )



"""��kt�:
>python p_14902.py
42'nin karesi = 1764
42'nin karek�k� = 6.48074069840786
"""