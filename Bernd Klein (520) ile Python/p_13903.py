# coding:iso-8859-9 T�rk�e
# p_13903.py: S�n�f init genel �zellikleri ve metod-i�i kullan�lan �zel de�i�kenleri �rne�i.

class Robot:
    def __init__ (self, ad�, y�l�, fizi�i = 0.5, psikolojisi = 0.5):
        self.ad = ad�
        self.y�l = y�l�
        self.__fizik = fizi�i
        self.__psikoloji = psikolojisi

    #@property
    def durum (self):
        toplam = self.__fizik + self.__psikoloji
        if toplam <= -1: return "Perperi�an hissediyorum!"
        elif toplam <= 0: return "K�t� hissediyorum!"
        elif toplam <= 0.5: return "Daha iyi olabilirdi!"
        elif toplam <= 1: return "Fena de�ilim gibi!"
        else: return "Muhte�emim!" 


if __name__ == "__main__":
    x = Robot ("Muhammed Ali", 20190428, 0.2, 0.4)
    y = Robot ("Mahmut Nihat", 19570417, -0.4, 0.3)
    z = Robot ("Zeliha Candan", 19550810, 1.2, 1.3)
    q = Robot ("Canan Candan", 19740115, -1.2, -1.3)

    print ("Ben " + str (x.y�l) + " do�umlu robot " + x.ad + "'yim. Bug�nk� durumum: " + x.durum())
    print ("Ben " + str (y.y�l) + " do�umlu robot " + y.ad + "'�m. Bug�nk� durumum: " + y.durum())
    print ("Ben " + str (z.y�l) + " do�umlu robot " + z.ad + "'�m. Bug�nk� durumum: " + z.durum())
    print ("Ben " + str (q.y�l) + " do�umlu robot " + q.ad + "'�m. Bug�nk� durumum: " + q.durum())
    # @property kullan�ld���nda "x.durum()" metodu yerine "x.durum" �zelli�i gelmelidir...



"""��kt�:
>python p_13903.py
Ben 20190428 do�umlu robot Muhammed Ali'yim. Bug�nk� durumum: Fena de�ilim gibi!
Ben 19570417 do�umlu robot Mahmut Nihat'�m. Bug�nk� durumum: K�t� hissediyorum!
Ben 19550810 do�umlu robot Zeliha Candan'�m. Bug�nk� durumum: Muhte�emim!
Ben 19740115 do�umlu robot Canan Candan'�m. Bug�nk� durumum: Perperi�an hissediyorum!
"""