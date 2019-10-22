# coding:iso-8859-9 T�rk�e
# p_14903.py: Soyut s�n�f� arg�manlayan somut s�n�f�n esge�me metodlar� ve ekstra somut metodu �rne�i.

from abc import ABC, abstractmethod

class SoyutS�n�f (ABC):
    @abstractmethod
    def soyutMetod1 (self): print ("\nPass ge�mek zorunda de�ilim!..")
    @abstractmethod
    def soyutMetod2 (self): print ("\nPass ge�meyip bir �eyler yapal�m!..")

class SomutS�n�f (SoyutS�n�f):
    def soyutMetod1 (self):
        super().soyutMetod1()
        print ("Soyut metod-1 i�lemini ilave i�lemle zenginle�tirelim!..")
    def soyutMetod2 (self):
        super().soyutMetod2()
        print ("Soyut metod-2 i�lemini ekstra i�lemle zenginle�tirelim!..")
    def somutMetod (self):
        print ("\n�lla sadece miraslanan soyut s�n�f�n soyut metodlar� esge�mesiyle yetinmeyelim!..")

a = SomutS�n�f()

a.soyutMetod1()
a.soyutMetod2()
a.somutMetod()



"""��kt�:
>python p_14903.py
Pass ge�mek zorunda de�ilim!..
Soyut metod-1 i�lemini ilave i�lemle zenginle�tirelim!..

Pass ge�meyip bir �eyler yapal�m!..
Soyut metod-2 i�lemini ekstra i�lemle zenginle�tirelim!..

�lla sadece miraslanan soyut s�n�f�n soyut metodlar� esge�mesiyle yetinmeyelim!..
"""