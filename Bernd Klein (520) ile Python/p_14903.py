# coding:iso-8859-9 Türkçe
# p_14903.py: Soyut sınıfı argümanlayan somut sınıfın esgeçme metodları ve ekstra somut metodu örneği.

from abc import ABC, abstractmethod

class SoyutSınıf (ABC):
    @abstractmethod
    def soyutMetod1 (self): print ("\nPass geçmek zorunda değilim!..")
    @abstractmethod
    def soyutMetod2 (self): print ("\nPass geçmeyip bir şeyler yapalım!..")

class SomutSınıf (SoyutSınıf):
    def soyutMetod1 (self):
        super().soyutMetod1()
        print ("Soyut metod-1 işlemini ilave işlemle zenginleştirelim!..")
    def soyutMetod2 (self):
        super().soyutMetod2()
        print ("Soyut metod-2 işlemini ekstra işlemle zenginleştirelim!..")
    def somutMetod (self):
        print ("\nİlla sadece miraslanan soyut sınıfın soyut metodları esgeçmesiyle yetinmeyelim!..")

a = SomutSınıf()

a.soyutMetod1()
a.soyutMetod2()
a.somutMetod()



"""Çıktı:
>python p_14903.py
Pass geçmek zorunda değilim!..
Soyut metod-1 işlemini ilave işlemle zenginleştirelim!..

Pass geçmeyip bir şeyler yapalım!..
Soyut metod-2 işlemini ekstra işlemle zenginleştirelim!..

İlla sadece miraslanan soyut sınıfın soyut metodları esgeçmesiyle yetinmeyelim!..
"""