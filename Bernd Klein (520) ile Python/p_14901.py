# coding:iso-8859-9 Türkçe
# p_14901.py: Enaz bir pass metodlu soyut sınıfı argümanlayan somut sınıf nesnesi örneği.

class SoyutSınıf: # 1-2 soyut/pass metod içeren sahte soyut sınıf...
    def soyutMetod (self): pass # Yürütmesiz soyut metod...
    def somutMetod (self): print ("Ben her işleminizi yaparım abi!..")

class SomutSınıf (SoyutSınıf): pass # Soyut sınıfa miraslı somut sınıf...

a = SoyutSınıf() # Soyut sınıf olsaydı tiplenemezdi, hata verirdi...
b = SomutSınıf()

a.soyutMetod()
a.somutMetod()

b.soyutMetod()
b.somutMetod()



"""Çıktı:
>python p_14901.py
Ben her işleminizi yaparım abi!..
Ben her işleminizi yaparım abi!..
"""