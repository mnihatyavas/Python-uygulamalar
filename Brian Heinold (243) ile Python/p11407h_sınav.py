# coding:iso-8859-9 T�rk�e

class VantiGrubu:
    def __init__ (self):
        self.kartlar = []
        for tak�m in ['Kupa', 'Sinek']:
            for say� in range (2, 11): self.kartlar.append ((tak�m, say�))

    def sonrakiKart (self): return self.kartlar.pop (0)
    def kartKald�M� (self): return len (self.kartlar) > 0
    def ebat (self): return len (self.kartlar)
    def kar��t�r (self): shuffle (self.kartlar)

def g�ster():
    for i in range (uz):
        print ("{:2d}.kart: {}-{}" .format ((i+1), deste.kartlar[i][0], deste.kartlar[i][1]) )

from random import shuffle
deste = VantiGrubu()
uz = deste.ebat()
print ("S�ral� kartlar:\n", "-"*17, sep="")
g�ster()

print ("\nKar�l� kartlar:\n", "-"*17, sep="")
deste.kar��t�r()
g�ster()

print ("\n-->Toplam kart say�s�:", deste.ebat() )
print ("Kar�l� destenin �st�nden da��t�lan 1.kart:", deste.sonrakiKart(), "\n-->Kalan kart say�s�:", deste.ebat() )
print ("Kar�l� destenin �st�nden da��t�lan 2.kart:", deste.sonrakiKart(), "\n-->Kalan kart say�s�:", deste.ebat() )
print ("Kar�l� destenin �st�nden da��t�lan 3.kart:", deste.sonrakiKart(), "\n-->Kalan kart say�s�:", deste.ebat() )
