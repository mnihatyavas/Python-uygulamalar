# coding:iso-8859-9 Türkçe
# p_14101x2.py: Takvim sınıfı metodlarıyla günün artıkyıl kontrollü bir ilerletilmesi ana/alt-örneği.

class Takvim (object): # Takvim sınıfı gg/aa/yyyy takvimini yürütür...
    aylar = (31,28,31,30,31,30,31,31,30,31,30,31)
    yerelTarih = "İngiliz"

    @staticmethod
    def artıkYıl (yıl):
        """ 
        yıl%400 == 0 ise artık yıldır...
        yıl%400 != 0 and yıl%100 == 0 ise artık yıl değildir...
        yıl%4 == 0 and yıl%100 != 0 ise artık yıldır...
        Tüm diğer yıllar genel yıldır, yani artık yıl değildir...
        """
        if not yıl % 4 == 0: return False
        elif not yıl % 100 == 0: return True
        elif not yıl % 400 == 0: return False
        else: return True

    def __init__ (self, g, a, y): self.takvimiKur (g, a, y) # public/genel...
    def takvimiKur (self, g, a, y): # g,a,y tamsayı ve y 4 rakamlı olmalıdır...
        if type (g) == int and type (a) == int and type (y) == int:
            self.__gün = g # private/özel...
            self.__ay = a
            self.__yıl = y
        else: raise TypeError ("gg,aa, yyyy tamsayı olmalıdır!")
    def __str__ (self):
        if Takvim.yerelTarih == "İngiliz": # gg/aa/yyyy
            return "{0:02d}/{1:02d}/{2:4d}" .format (self.__gün, self.__ay, self.__yıl)
        else: # aa/gg/yyyy
            # Amerikan tarih tarzıdır...
            return "{0:02d}/{1:02d}/{2:4d}".format (self.__ay, self.__gün, self.__yıl)
    def ilerlet (self): # Tarihi/günü bir artırır...
        ayGünleri = Takvim.aylar [self.__ay - 1]
        if self.__ay == 2 and Takvim.artıkYıl (self.__yıl): ayGünleri +=1
        if self.__gün == ayGünleri:
            self.__gün = 1
            if self.__ay == 12:
                self.__ay = 1
                self.__yıl +=1
            else: self.__ay +=1
        else: self.__gün +=1


if __name__ == "__main__":
    x = Takvim (31, 12, 2016)
    print (x, end=" ")
    x.ilerlet()
    print ("==>bir gün sonrası:", x)

    print ("\n2016 bir artık yıldır:")
    x = Takvim (28, 2, 2016)
    print (x, end=" ")
    x.ilerlet()
    print ("==>bir gün sonrası:", x)

    x = Takvim (28, 2, 2019)
    print (x, end=" ")
    x.ilerlet()
    print ("==>bir gün sonrası:", x)

    print ("\n1900 artık yıl değildir, 100'e bölünür ama 400'e değil:")
    x = Takvim (28, 2, 1900)
    print (x, end=" ")
    x.ilerlet()
    print ("==>bir gün sonrası:", x)

    print ("\n2000 artık yıldır, (100'e ve) 400'e bölünür:")
    x = Takvim (28, 2, 2000)
    print (x, end=" ")
    x.ilerlet()
    print ("==>bir gün sonrası:", x)

    print ("\nAmerikan tarih tarzına dönelim:")
    Takvim.yerelTarih = "Amerikan"
    x.ilerlet()
    print ("Bir gün sonrası:", x)  

"""Çıktı:
>python p_14101x2.py
31/12/2016 ==>bir gün sonrası: 01/01/2017

2016 bir artık yıldır:
28/02/2016 ==>bir gün sonrası: 29/02/2016
28/02/2019 ==>bir gün sonrası: 01/03/2019

1900 artık yıl değildir, 100'e bölünür ama 400'e değil:
28/02/1900 ==>bir gün sonrası: 01/03/1900

2000 artık yıldır, (100'e ve) 400'e bölünür:
28/02/2000 ==>bir gün sonrası: 29/02/2000

Amerikan tarih tarzına dönelim:
Bir gün sonrası: 03/01/2000
"""