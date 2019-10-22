# coding:iso-8859-9
# p_13705.py: Sınıf nesnesi metodu, tip değişkenine değer koyma ve alma örneği.

class Robot:
    def __init__ (self, adı = None): self.ad = adı
    def selamlaşma (self):
        if self.ad: print ("Merhaba, benim adım " + self.ad + "!")
        else: print ("Merhaba, ben henüz adı konmamış bir robotum!")
    def adKoy (self, adı): self.ad = adı
    def adAl (self): return self.ad

x1 = Robot()
x1.selamlaşma()

x1.adKoy ("Robot Nihat")
x1.selamlaşma()

x2 = Robot()
x2.adKoy (x1.adAl() )
x2.selamlaşma()

x3 = Robot ("Robot Mahmut Nihat")
x3.selamlaşma()

print ("\nx1 robotunun adı:", x1.adAl() )
print ("x2 robotunun adı:", x2.adAl() )
print ("x3 robotunun adı:", x3.adAl() )

"""Çıktı:
>python p_13705.py
Merhaba, ben henüz adı konmamış bir robotum!
Merhaba, benim adım Robot Nihat!
Merhaba, benim adım Robot Nihat!
Merhaba, benim adım Robot Mahmut Nihat!

x1 robotunun adı: Robot Nihat
x2 robotunun adı: Robot Nihat
x3 robotunun adı: Robot Mahmut Nihat
"""