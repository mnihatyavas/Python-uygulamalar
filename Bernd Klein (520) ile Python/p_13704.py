# coding:iso-8859-9
# p_13704.py: Sınıf argümanlı fonksiyon, sınıfın init tipleri ve fonksiyon metodları örneği.

def selam (argümanNesnesi):
    print ("Merhaba, benim adım " + argümanNesnesi.ad + "!")

class Robot: pass

x = Robot()
x.ad = "Robot Ali"

selam (x) # Argümanı sınıf olan ve sınıf özelliğini yansıtan fonksiyon...
#-------------------------------------------------------------------------------------------------

class Robot: selamlaşma = selam

x = Robot()
x.ad = "Robot Ali"

Robot.selamlaşma (x) # Fonksiyon işleten sınıf metodunun özellik yansıtması...
x.ad = "Robot Muhammed Ali"
x.selamlaşma() # Bir üstekiyle aynıdır...
print ("-"*75, "\n", sep="")
#-------------------------------------------------------------------------------------------------

class Robot:
    def __init__ (self, adı = None):
        self.ad = adı
        print ("\n==>Sınıf fonksiyonu, metoddur.\nSınıf nesnesinin her yaratılımasında otomatik işletilen metod 'init'dir.\n'init' metodu sınıfın tip değişkenlerini barındırır.")

    def selamlaşma (self):
        if self.ad: print ("Merhaba, benim adım " + self.ad + "!")
        else: print ("Merhaba, ben henüz adı konulmamış bir robotum!")

x = Robot()
x.selamlaşma()
y = Robot ("Robot Ali")
y.selamlaşma()
z = Robot ("Robot Muhammed Ali")
z.selamlaşma()

"""Çıktı:
>python p_13704.py
Merhaba, benim adım Robot Ali!
Merhaba, benim adım Robot Ali!
Merhaba, benim adım Robot Muhammed Ali!
---------------------------------------------------------------------------

==>Sınıf fonksiyonu, metoddur.
Sınıf nesnesinin her yaratılımasında otomatik işletilen metod 'init'dir.
'init' metodu sınıfın tip değişkenlerini barındırır.
Merhaba, ben henüz adı konulmamış bir robotum!

==>Sınıf fonksiyonu, metoddur.
Sınıf nesnesinin her yaratılımasında otomatik işletilen metod 'init'dir.
'init' metodu sınıfın tip değişkenlerini barındırır.
Merhaba, benim adım Robot Ali!

==>Sınıf fonksiyonu, metoddur.
Sınıf nesnesinin her yaratılımasında otomatik işletilen metod 'init'dir.
'init' metodu sınıfın tip değişkenlerini barındırır.
Merhaba, benim adım Robot Muhammed Ali!
"""