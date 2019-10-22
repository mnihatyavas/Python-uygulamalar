# coding:iso-8859-9 T�rk�e

class Zaman:
    def __init__ (self, z): self.z = z

    def g�n (self):
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

# input i�in (366*24*60*60-1) girebilirsiniz, fazlas�n� de�il...
try: say� = abs (int (eval (input ("Saniye cinsinden bir say� girin: "))))
except Exception: say� = randint (1, 366*24*60*60-1)
if say� > 31622399: say� = 31622399

zaman = Zaman (say�)

print ("\nGirdi�iniz {:,d} saniye = {} g�n, {} saat, {} dakika ve {} saniye'dir."\
    .format (say�, zaman.g�n(), zaman.saat(), zaman.dakika(), zaman.z) )
