# coding:iso-8859-9 T�rk�e

class Ebeveyn:
    def __init__ (self, a): self.a = a
    def metod1 (self): print ((self.a + " ")*2)
    def metod2 (self): print (self.a + '..')

class �ocuk (Ebeveyn):
    def __init__ (self, a, b):
        self.a = a
        self.b = b
    def metod1 (self): print ((self.a + " ")*7)
    def metod3 (self): print (self.a + " " + self.b)

anne = Ebeveyn ('Merhaba, yavrum!')
�ocuk = �ocuk ('Merhaba, anneci�im!', 'Bay bay!')

print ('Ebeveyn metod-1:'); anne.metod1()
print ('\nEbeveyn metod-2:'); anne.metod2()

print ('\n�ocuk metod-1:'); �ocuk.metod1()
print ('\n�ocuk metod-2:'); �ocuk.metod2()
print ('\n�ocuk metod-3:'); �ocuk.metod3()
