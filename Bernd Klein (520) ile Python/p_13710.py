# coding:iso-8859-9
# p_13710.py: S�n�f-i�i al-koy metodlarla �zel �zelliklerinin de�erlerini de�i�tirme �rne�i.

class Robot:
    def __init__ (self, ad�=None, y�l�=2018):
        self.__ad = ad�
        self.__y�l = y�l�
    def selamla (self):
        if self.__ad: print ("Selam, benim ad�m Robot " + self.__ad + "!")
        else: print ("Selam, ben hen�z ad� konulmam�� bir Robotum!")
    def adKoy (self, ad�): self.__ad = ad�
    def adAl (self): return self.__ad
    def y�lKoy (self, y�l�): self.__y�l = y�l�
    def y�lAl (self): return self.__y�l
    def __str__ (self): return "Robotun Ad�: " + self.__ad + ", �malat Tarihi: " +  str (self.__y�l)


if __name__ == "__main__":
    x = Robot ("Mahmut Nihat", 19570417)
    y = Robot ("Muhammed Ali", 20000101)
    z = Robot ("Zeliha Nihal", 19550807)
    q = Robot ()

    print ("__�zel s�n�f tip de�i�kenlerine setter-getter/koyucu-al�c� metodlarla eri�ilebilir.\n")
    for rbt in [x, y, z, q]:
        rbt.selamla()
        if rbt.adAl() == "Muhammed Ali": rbt.y�lKoy (20190425)
        print ("Benim imalat tarihim " + str (rbt.y�lAl()) + "'dir!\n")

"""��kt�:
>python p_13710.py
__�zel s�n�f tip de�i�kenlerine setter-getter/koyucu-al�c� metodlarla eri�ilebilir.

Selam, benim ad�m Robot Mahmut Nihat!
Benim imalat tarihim 19570417'dir!

Selam, benim ad�m Robot Muhammed Ali!
Benim imalat tarihim 20190425'dir!

Selam, benim ad�m Robot Zeliha Nihal!
Benim imalat tarihim 19550807'dir!

Selam, ben hen�z ad� konulmam�� bir Robotum!
Benim imalat tarihim 2018'dir!
"""