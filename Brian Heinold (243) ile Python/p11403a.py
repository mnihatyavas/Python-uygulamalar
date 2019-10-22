# coding:iso-8859-9 Türkçe

class Ebeveyn:
    def __init__ (self, a): self.a = a
    def metod1 (self): print ((self.a + " ")*2)
    def metod2 (self): print (self.a + '..')

class Çocuk (Ebeveyn):
    def __init__ (self, a, b):
        self.a = a
        self.b = b
    def metod1 (self): print ((self.a + " ")*7)
    def metod3 (self): print (self.a + " " + self.b)

anne = Ebeveyn ('Merhaba, yavrum!')
çocuk = Çocuk ('Merhaba, anneciğim!', 'Bay bay!')

print ('Ebeveyn metod-1:'); anne.metod1()
print ('\nEbeveyn metod-2:'); anne.metod2()

print ('\nÇocuk metod-1:'); çocuk.metod1()
print ('\nÇocuk metod-2:'); çocuk.metod2()
print ('\nÇocuk metod-3:'); çocuk.metod3()
