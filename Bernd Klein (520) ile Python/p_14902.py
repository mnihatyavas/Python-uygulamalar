# coding:iso-8859-9 Türkçe
# p_14902.py: Soyut sınıfın tüm soyut metodlarını esgeçen somut sınıf nesneleri örneği.

from abc import ABC, abstractmethod
# Python kütüphanesinde hazır abc.py, ABC/AbstractBaseClass: SoyutTemelSınıf
 
class SoyutSınıf (ABC): # Bir soyut metod içeren soyut sınıf...
    def __init__ (self, değer):
        self.değer = değer
        super().__init__()
    @abstractmethod
    def soyutMetod (self): pass
class SomutSınıf (SoyutSınıf): pass

# a = SoyutSınıf() ==> Soyut sınıf tiplenemez (TypeError)...
# b = SomutSınıf (42) ==> Soyut sınıfın tüm soyut metodlarını override/esgeçmeyen tipleme olmaz (TypeError)...

class SomutSınıf1 (SoyutSınıf):
    def soyutMetod (self): return self.değer**2
class SomutSınıf2 (SoyutSınıf):
    def soyutMetod (self): return self.değer**0.5

a = SomutSınıf1 (42)
b = SomutSınıf2 (42)

print ("42'nin karesi =", a.soyutMetod() )
print ("42'nin karekökü =", b.soyutMetod() )



"""Çıktı:
>python p_14902.py
42'nin karesi = 1764
42'nin karekökü = 6.48074069840786
"""