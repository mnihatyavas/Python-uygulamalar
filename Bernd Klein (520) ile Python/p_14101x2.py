# coding:iso-8859-9 T�rk�e
# p_14101x2.py: Takvim s�n�f� metodlar�yla g�n�n art�ky�l kontroll� bir ilerletilmesi ana/alt-�rne�i.

class Takvim (object): # Takvim s�n�f� gg/aa/yyyy takvimini y�r�t�r...
    aylar = (31,28,31,30,31,30,31,31,30,31,30,31)
    yerelTarih = "�ngiliz"

    @staticmethod
    def art�kY�l (y�l):
        """ 
        y�l%400 == 0 ise art�k y�ld�r...
        y�l%400 != 0 and y�l%100 == 0 ise art�k y�l de�ildir...
        y�l%4 == 0 and y�l%100 != 0 ise art�k y�ld�r...
        T�m di�er y�llar genel y�ld�r, yani art�k y�l de�ildir...
        """
        if not y�l % 4 == 0: return False
        elif not y�l % 100 == 0: return True
        elif not y�l % 400 == 0: return False
        else: return True

    def __init__ (self, g, a, y): self.takvimiKur (g, a, y) # public/genel...
    def takvimiKur (self, g, a, y): # g,a,y tamsay� ve y 4 rakaml� olmal�d�r...
        if type (g) == int and type (a) == int and type (y) == int:
            self.__g�n = g # private/�zel...
            self.__ay = a
            self.__y�l = y
        else: raise TypeError ("gg,aa, yyyy tamsay� olmal�d�r!")
    def __str__ (self):
        if Takvim.yerelTarih == "�ngiliz": # gg/aa/yyyy
            return "{0:02d}/{1:02d}/{2:4d}" .format (self.__g�n, self.__ay, self.__y�l)
        else: # aa/gg/yyyy
            # Amerikan tarih tarz�d�r...
            return "{0:02d}/{1:02d}/{2:4d}".format (self.__ay, self.__g�n, self.__y�l)
    def ilerlet (self): # Tarihi/g�n� bir art�r�r...
        ayG�nleri = Takvim.aylar [self.__ay - 1]
        if self.__ay == 2 and Takvim.art�kY�l (self.__y�l): ayG�nleri +=1
        if self.__g�n == ayG�nleri:
            self.__g�n = 1
            if self.__ay == 12:
                self.__ay = 1
                self.__y�l +=1
            else: self.__ay +=1
        else: self.__g�n +=1


if __name__ == "__main__":
    x = Takvim (31, 12, 2016)
    print (x, end=" ")
    x.ilerlet()
    print ("==>bir g�n sonras�:", x)

    print ("\n2016 bir art�k y�ld�r:")
    x = Takvim (28, 2, 2016)
    print (x, end=" ")
    x.ilerlet()
    print ("==>bir g�n sonras�:", x)

    x = Takvim (28, 2, 2019)
    print (x, end=" ")
    x.ilerlet()
    print ("==>bir g�n sonras�:", x)

    print ("\n1900 art�k y�l de�ildir, 100'e b�l�n�r ama 400'e de�il:")
    x = Takvim (28, 2, 1900)
    print (x, end=" ")
    x.ilerlet()
    print ("==>bir g�n sonras�:", x)

    print ("\n2000 art�k y�ld�r, (100'e ve) 400'e b�l�n�r:")
    x = Takvim (28, 2, 2000)
    print (x, end=" ")
    x.ilerlet()
    print ("==>bir g�n sonras�:", x)

    print ("\nAmerikan tarih tarz�na d�nelim:")
    Takvim.yerelTarih = "Amerikan"
    x.ilerlet()
    print ("Bir g�n sonras�:", x)  

"""��kt�:
>python p_14101x2.py
31/12/2016 ==>bir g�n sonras�: 01/01/2017

2016 bir art�k y�ld�r:
28/02/2016 ==>bir g�n sonras�: 29/02/2016
28/02/2019 ==>bir g�n sonras�: 01/03/2019

1900 art�k y�l de�ildir, 100'e b�l�n�r ama 400'e de�il:
28/02/1900 ==>bir g�n sonras�: 01/03/1900

2000 art�k y�ld�r, (100'e ve) 400'e b�l�n�r:
28/02/2000 ==>bir g�n sonras�: 29/02/2000

Amerikan tarih tarz�na d�nelim:
Bir g�n sonras�: 03/01/2000
"""