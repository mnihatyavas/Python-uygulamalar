# coding:iso-8859-9 T�rk�e
# Python 3 - Object Oriented

class ��g�ren:
    elemanSay�s� = 0

    def __init__ (self, isim, maa�):
        self.isim = isim
        self.maa� = maa�
        ��g�ren.elemanSay�s� += 1

    def i�g�reniG�ster (self):
        print ("�sim: ", self.isim,  "\n---Maa�: ", self.maa�)

# ��g�ren s�n�f�n�n 5 nesnesini yaratal�m...
i�g�ren1 = ��g�ren ("M.Nihat Yava�", 2000)
i�g�ren2 = ��g�ren ("M.Nedim Yava�", 3000)
i�g�ren3 = ��g�ren ("Nihal Yava� Candan", 1000)
i�g�ren4 = ��g�ren ("Hatice Yava� Ka�ar", 4000)
i�g�ren5 = ��g�ren ("Song�l Yava� G�kt�rk", 7000)

i�g�ren1.i�g�reniG�ster()
i�g�ren2.i�g�reniG�ster()
i�g�ren3.i�g�reniG�ster()
i�g�ren4.i�g�reniG�ster()
i�g�ren5.i�g�reniG�ster()

print ("\nToplam ��g�ren Say�s�: %d" % ��g�ren.elemanSay�s�)

print()
print ("��g�ren.__doc__:", ��g�ren.__doc__)
print ("��g�ren.__name__:", ��g�ren.__name__)
print ("��g�ren.__module__:", ��g�ren.__module__)
print ("��g�ren.__bases__:", ��g�ren.__bases__)
print ("��g�ren.__dict__:", ��g�ren.__dict__ )
