# coding:iso-8859-9 Türkçe

class Ürün:
    def __init__ (self):
        self.ad = "Dolmakalem"
        self.adet = 1000
        self.fiyat = 5.75

    def fiyat_al (self, miktar):
        if miktar < 10: print ("{} adet ürün, tanesi {:.2f} TL'den toplam: {:,.2f} TL'dir" .format (miktar, self.fiyat, miktar*self.fiyat))
        elif miktar < 100: print ("{} adet ürün, tanesi {:.2f} TL'den toplam: {:,.2f} TL'dir" .format (miktar, self.fiyat/1.10, miktar*self.fiyat/1.10))
        else: print ("{} adet ürün, tanesi {:.2f} TL'den toplam: {:,.2f} TL'dir" .format (miktar, self.fiyat/1.25, miktar*self.fiyat/1.25))

    def satış_gerçekleştir (self, miktar):
        if self.adet < miktar:
            print ("Stoğumuzu güncelleyinceye dek en fazla alabileceğiniz miktar:", self.adet, "adettir.")
            return
        if miktar < 10: print ("{} adet ürünü, tanesi {:.2f} TL'den toplam: {:,.2f} TL'ye satın aldınız" .format (miktar, self.fiyat, miktar*self.fiyat))
        elif miktar < 100: print ("{} adet ürünü, tanesi {:.2f} TL'den toplam: {:,.2f} TL'ye satın aldınız" .format (miktar, self.fiyat/1.10, miktar*self.fiyat/1.10))
        else: print ("{} adet ürünü, tanesi {:.2f} TL'den toplam: {:,.2f} TL'ye satın aldınız" .format (miktar, self.fiyat/1.25, miktar*self.fiyat/1.25))
        self.adet -= miktar

from random import randint
alışveriş = Ürün()
sayı = ""
while sayı != 0:
    try: sayı = abs (int (eval (input ("\nKaç adet dolmakalem almayı düşünüyorsunuz: "))))
    except Exception:
        if alışveriş.adet >= 1: sayı = randint (1, alışveriş.adet)
        else: sayı = 0
    print()
    if sayı == 0:
        print ("Güle güle, tekrar bekleriz efendim!")
        break
    alışveriş.fiyat_al (sayı)

    cevap = ""
    while not (cevap == "e" or cevap == "h"): cevap = input ("Peki bu fiyat teklifi üzerinden alış gerçekleştirecek misiniz: ").lower()
    print()
    alışveriş.satış_gerçekleştir (sayı)
