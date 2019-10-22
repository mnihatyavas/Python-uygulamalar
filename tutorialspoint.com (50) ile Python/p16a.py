# coding:iso-8859-9 Türkçe
# Python 3 - Object Oriented

class İşgören:
    elemanSayısı = 0

    def __init__ (self, isim, maaş):
        self.isim = isim
        self.maaş = maaş
        İşgören.elemanSayısı += 1

    def işgöreniGöster (self):
        print ("İsim: ", self.isim,  "\n---Maaş: ", self.maaş)

# İşgören sınıfının 5 nesnesini yaratalım...
işgören1 = İşgören ("M.Nihat Yavaş", 2000)
işgören2 = İşgören ("M.Nedim Yavaş", 3000)
işgören3 = İşgören ("Nihal Yavaş Candan", 1000)
işgören4 = İşgören ("Hatice Yavaş Kaçar", 4000)
işgören5 = İşgören ("Songül Yavaş Göktürk", 7000)

işgören1.işgöreniGöster()
işgören2.işgöreniGöster()
işgören3.işgöreniGöster()
işgören4.işgöreniGöster()
işgören5.işgöreniGöster()

print ("\nToplam İşgören Sayısı: %d" % İşgören.elemanSayısı)

print()
print ("İşgören.__doc__:", İşgören.__doc__)
print ("İşgören.__name__:", İşgören.__name__)
print ("İşgören.__module__:", İşgören.__module__)
print ("İşgören.__bases__:", İşgören.__bases__)
print ("İşgören.__dict__:", İşgören.__dict__ )
