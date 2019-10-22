# coding:iso-8859-9 T�rk�e

class �r�n:
    def __init__ (self):
        self.ad = "Dolmakalem"
        self.adet = 1000
        self.fiyat = 5.75

    def fiyat_al (self, miktar):
        if miktar < 10: print ("{} adet �r�n, tanesi {:.2f} TL'den toplam: {:,.2f} TL'dir" .format (miktar, self.fiyat, miktar*self.fiyat))
        elif miktar < 100: print ("{} adet �r�n, tanesi {:.2f} TL'den toplam: {:,.2f} TL'dir" .format (miktar, self.fiyat/1.10, miktar*self.fiyat/1.10))
        else: print ("{} adet �r�n, tanesi {:.2f} TL'den toplam: {:,.2f} TL'dir" .format (miktar, self.fiyat/1.25, miktar*self.fiyat/1.25))

    def sat��_ger�ekle�tir (self, miktar):
        if self.adet < miktar:
            print ("Sto�umuzu g�ncelleyinceye dek en fazla alabilece�iniz miktar:", self.adet, "adettir.")
            return
        if miktar < 10: print ("{} adet �r�n�, tanesi {:.2f} TL'den toplam: {:,.2f} TL'ye sat�n ald�n�z" .format (miktar, self.fiyat, miktar*self.fiyat))
        elif miktar < 100: print ("{} adet �r�n�, tanesi {:.2f} TL'den toplam: {:,.2f} TL'ye sat�n ald�n�z" .format (miktar, self.fiyat/1.10, miktar*self.fiyat/1.10))
        else: print ("{} adet �r�n�, tanesi {:.2f} TL'den toplam: {:,.2f} TL'ye sat�n ald�n�z" .format (miktar, self.fiyat/1.25, miktar*self.fiyat/1.25))
        self.adet -= miktar

from random import randint
al��veri� = �r�n()
say� = ""
while say� != 0:
    try: say� = abs (int (eval (input ("\nKa� adet dolmakalem almay� d���n�yorsunuz: "))))
    except Exception:
        if al��veri�.adet >= 1: say� = randint (1, al��veri�.adet)
        else: say� = 0
    print()
    if say� == 0:
        print ("G�le g�le, tekrar bekleriz efendim!")
        break
    al��veri�.fiyat_al (say�)

    cevap = ""
    while not (cevap == "e" or cevap == "h"): cevap = input ("Peki bu fiyat teklifi �zerinden al�� ger�ekle�tirecek misiniz: ").lower()
    print()
    al��veri�.sat��_ger�ekle�tir (say�)
