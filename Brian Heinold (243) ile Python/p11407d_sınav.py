# coding:iso-8859-9 Türkçe

class Zaman:
    def __init__ (self, z): self.z = z

    def gün (self):
        gn = self.z//(60*60*24)
        self.z = self.z % (60*60*24)
        return gn

    def saat (self):
        st = self.z//(60*60)
        self.z = self.z % (60*60)
        return st

    def dakika (self):
        dk = self.z//60
        self.z = self.z % 60
        return dk

from random import randint

# input için (366*24*60*60-1) girebilirsiniz, fazlasını değil...
try: sayı = abs (int (eval (input ("Saniye cinsinden bir sayı girin: "))))
except Exception: sayı = randint (1, 366*24*60*60-1)
if sayı > 31622399: sayı = 31622399

zaman = Zaman (sayı)

print ("\nGirdiğiniz {:,d} saniye = {} gün, {} saat, {} dakika ve {} saniye'dir."\
    .format (sayı, zaman.gün(), zaman.saat(), zaman.dakika(), zaman.z) )
