# coding:iso-8859-9 T�rk�e

class Ebeveyn:
    def __init__ (self, a): self.a = a
    def yaz (self): print (self.a, end=" ")

class �ocuk (Ebeveyn):
    def __init__ (self, a, b):
        Ebeveyn.__init__ (self, a)
        self.b = b
    def yaz (self):
        Ebeveyn.yaz (self)
        print (self.b)

anne = Ebeveyn ("Merhaba, yavrum!")
�ocuk = �ocuk ("Merhaba, anneci�im!", "Bye bye!")

anne.yaz(); print()
�ocuk.yaz()