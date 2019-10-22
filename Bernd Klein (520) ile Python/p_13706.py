# coding:iso-8859-9
# p_13706.py: S�n�f nesnesi metodlar�, �oklu tip de�i�kenlerine de�er atama ve okuma �rne�i.

class Robot:
    def __init__ (self, ad� = None, tarih = None):
        self.ad = ad�
        self.imalat = tarih
    def selamla�ma (self):
        if self.ad: print ("\nMerhaba, benim ad�m " + self.ad + "!")
        else: print ("Merhaba, ben hen�z ad� konmam�� bir robotum!")
        if self.imalat: print ("�malat tarihim: " + str (self.imalat) )
        else: print ("�malat tarihim maalesef bilinmiyor!")
    def adKoy (self, ad�): self.ad = ad�
    def adAl (self): return self.ad
    def tarihKoy (self, imalTarihi): self.imalat = imalTarihi
    def tarihAl (self): return self.imalat

x1 = Robot()
x1.selamla�ma()

x1.adKoy ("Robot Nihat")
x1.selamla�ma()

x3 = Robot ("Robot Mahmut Nihat", 19570417)
x3.selamla�ma()

"""��kt�:
>python p_13706.py
Merhaba, ben hen�z ad� konmam�� bir robotum!
�malat tarihim maalesef bilinmiyor!

Merhaba, benim ad�m Robot Nihat!
�malat tarihim maalesef bilinmiyor!

Merhaba, benim ad�m Robot Mahmut Nihat!
�malat tarihim: 19570417
"""