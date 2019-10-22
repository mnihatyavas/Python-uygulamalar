# coding:iso-8859-9 Türkçe

class Ebeveyn:
    def __init__ (self, a): self.a = a
    def yaz (self): print (self.a, end=" ")

class Çocuk (Ebeveyn):
    def __init__ (self, a, b):
        Ebeveyn.__init__ (self, a)
        self.b = b
    def yaz (self):
        Ebeveyn.yaz (self)
        print (self.b)

anne = Ebeveyn ("Merhaba, yavrum!")
çocuk = Çocuk ("Merhaba, anneciğim!", "Bye bye!")

anne.yaz(); print()
çocuk.yaz()