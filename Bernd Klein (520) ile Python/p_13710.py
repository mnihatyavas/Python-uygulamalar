# coding:iso-8859-9
# p_13710.py: Sınıf-içi al-koy metodlarla özel özelliklerinin değerlerini değiştirme örneği.

class Robot:
    def __init__ (self, adı=None, yılı=2018):
        self.__ad = adı
        self.__yıl = yılı
    def selamla (self):
        if self.__ad: print ("Selam, benim adım Robot " + self.__ad + "!")
        else: print ("Selam, ben henüz adı konulmamış bir Robotum!")
    def adKoy (self, adı): self.__ad = adı
    def adAl (self): return self.__ad
    def yılKoy (self, yılı): self.__yıl = yılı
    def yılAl (self): return self.__yıl
    def __str__ (self): return "Robotun Adı: " + self.__ad + ", İmalat Tarihi: " +  str (self.__yıl)


if __name__ == "__main__":
    x = Robot ("Mahmut Nihat", 19570417)
    y = Robot ("Muhammed Ali", 20000101)
    z = Robot ("Zeliha Nihal", 19550807)
    q = Robot ()

    print ("__özel sınıf tip değişkenlerine setter-getter/koyucu-alıcı metodlarla erişilebilir.\n")
    for rbt in [x, y, z, q]:
        rbt.selamla()
        if rbt.adAl() == "Muhammed Ali": rbt.yılKoy (20190425)
        print ("Benim imalat tarihim " + str (rbt.yılAl()) + "'dir!\n")

"""Çıktı:
>python p_13710.py
__özel sınıf tip değişkenlerine setter-getter/koyucu-alıcı metodlarla erişilebilir.

Selam, benim adım Robot Mahmut Nihat!
Benim imalat tarihim 19570417'dir!

Selam, benim adım Robot Muhammed Ali!
Benim imalat tarihim 20190425'dir!

Selam, benim adım Robot Zeliha Nihal!
Benim imalat tarihim 19550807'dir!

Selam, ben henüz adı konulmamış bir Robotum!
Benim imalat tarihim 2018'dir!
"""