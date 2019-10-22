# coding:iso-8859-9 Türkçe
# p_13903.py: Sınıf init genel özellikleri ve metod-içi kullanılan özel değişkenleri örneği.

class Robot:
    def __init__ (self, adı, yılı, fiziği = 0.5, psikolojisi = 0.5):
        self.ad = adı
        self.yıl = yılı
        self.__fizik = fiziği
        self.__psikoloji = psikolojisi

    #@property
    def durum (self):
        toplam = self.__fizik + self.__psikoloji
        if toplam <= -1: return "Perperişan hissediyorum!"
        elif toplam <= 0: return "Kötü hissediyorum!"
        elif toplam <= 0.5: return "Daha iyi olabilirdi!"
        elif toplam <= 1: return "Fena değilim gibi!"
        else: return "Muhteşemim!" 


if __name__ == "__main__":
    x = Robot ("Muhammed Ali", 20190428, 0.2, 0.4)
    y = Robot ("Mahmut Nihat", 19570417, -0.4, 0.3)
    z = Robot ("Zeliha Candan", 19550810, 1.2, 1.3)
    q = Robot ("Canan Candan", 19740115, -1.2, -1.3)

    print ("Ben " + str (x.yıl) + " doğumlu robot " + x.ad + "'yim. Bugünkü durumum: " + x.durum())
    print ("Ben " + str (y.yıl) + " doğumlu robot " + y.ad + "'ım. Bugünkü durumum: " + y.durum())
    print ("Ben " + str (z.yıl) + " doğumlu robot " + z.ad + "'ım. Bugünkü durumum: " + z.durum())
    print ("Ben " + str (q.yıl) + " doğumlu robot " + q.ad + "'ım. Bugünkü durumum: " + q.durum())
    # @property kullanıldığında "x.durum()" metodu yerine "x.durum" özelliği gelmelidir...



"""Çıktı:
>python p_13903.py
Ben 20190428 doğumlu robot Muhammed Ali'yim. Bugünkü durumum: Fena değilim gibi!
Ben 19570417 doğumlu robot Mahmut Nihat'ım. Bugünkü durumum: Kötü hissediyorum!
Ben 19550810 doğumlu robot Zeliha Candan'ım. Bugünkü durumum: Muhteşemim!
Ben 19740115 doğumlu robot Canan Candan'ım. Bugünkü durumum: Perperişan hissediyorum!
"""