# coding:iso-8859-9 T�rk�e
# p_14901.py: Enaz bir pass metodlu soyut s�n�f� arg�manlayan somut s�n�f nesnesi �rne�i.

class SoyutS�n�f: # 1-2 soyut/pass metod i�eren sahte soyut s�n�f...
    def soyutMetod (self): pass # Y�r�tmesiz soyut metod...
    def somutMetod (self): print ("Ben her i�leminizi yapar�m abi!..")

class SomutS�n�f (SoyutS�n�f): pass # Soyut s�n�fa mirasl� somut s�n�f...

a = SoyutS�n�f() # Soyut s�n�f olsayd� tiplenemezdi, hata verirdi...
b = SomutS�n�f()

a.soyutMetod()
a.somutMetod()

b.soyutMetod()
b.somutMetod()



"""��kt�:
>python p_14901.py
Ben her i�leminizi yapar�m abi!..
Ben her i�leminizi yapar�m abi!..
"""