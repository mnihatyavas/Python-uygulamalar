# coding:iso-8859-9
# p_13705.py: S�n�f nesnesi metodu, tip de�i�kenine de�er koyma ve alma �rne�i.

class Robot:
    def __init__ (self, ad� = None): self.ad = ad�
    def selamla�ma (self):
        if self.ad: print ("Merhaba, benim ad�m " + self.ad + "!")
        else: print ("Merhaba, ben hen�z ad� konmam�� bir robotum!")
    def adKoy (self, ad�): self.ad = ad�
    def adAl (self): return self.ad

x1 = Robot()
x1.selamla�ma()

x1.adKoy ("Robot Nihat")
x1.selamla�ma()

x2 = Robot()
x2.adKoy (x1.adAl() )
x2.selamla�ma()

x3 = Robot ("Robot Mahmut Nihat")
x3.selamla�ma()

print ("\nx1 robotunun ad�:", x1.adAl() )
print ("x2 robotunun ad�:", x2.adAl() )
print ("x3 robotunun ad�:", x3.adAl() )

"""��kt�:
>python p_13705.py
Merhaba, ben hen�z ad� konmam�� bir robotum!
Merhaba, benim ad�m Robot Nihat!
Merhaba, benim ad�m Robot Nihat!
Merhaba, benim ad�m Robot Mahmut Nihat!

x1 robotunun ad�: Robot Nihat
x2 robotunun ad�: Robot Nihat
x3 robotunun ad�: Robot Mahmut Nihat
"""