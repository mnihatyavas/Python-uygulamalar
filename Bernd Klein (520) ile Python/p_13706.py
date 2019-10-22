# coding:iso-8859-9
# p_13706.py: Sınıf nesnesi metodları, çoklu tip değişkenlerine değer atama ve okuma örneği.

class Robot:
    def __init__ (self, adı = None, tarih = None):
        self.ad = adı
        self.imalat = tarih
    def selamlaşma (self):
        if self.ad: print ("\nMerhaba, benim adım " + self.ad + "!")
        else: print ("Merhaba, ben henüz adı konmamış bir robotum!")
        if self.imalat: print ("İmalat tarihim: " + str (self.imalat) )
        else: print ("İmalat tarihim maalesef bilinmiyor!")
    def adKoy (self, adı): self.ad = adı
    def adAl (self): return self.ad
    def tarihKoy (self, imalTarihi): self.imalat = imalTarihi
    def tarihAl (self): return self.imalat

x1 = Robot()
x1.selamlaşma()

x1.adKoy ("Robot Nihat")
x1.selamlaşma()

x3 = Robot ("Robot Mahmut Nihat", 19570417)
x3.selamlaşma()

"""Çıktı:
>python p_13706.py
Merhaba, ben henüz adı konmamış bir robotum!
İmalat tarihim maalesef bilinmiyor!

Merhaba, benim adım Robot Nihat!
İmalat tarihim maalesef bilinmiyor!

Merhaba, benim adım Robot Mahmut Nihat!
İmalat tarihim: 19570417
"""