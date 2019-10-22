# coding:iso-8859-9 Türkçe

class VantiGrubu:
    def __init__ (self):
        self.kartlar = []
        for takım in ['Kupa', 'Sinek']:
            for sayı in range (2, 11): self.kartlar.append ((takım, sayı))

    def sonrakiKart (self): return self.kartlar.pop (0)
    def kartKaldıMı (self): return len (self.kartlar) > 0
    def ebat (self): return len (self.kartlar)
    def karıştır (self): shuffle (self.kartlar)

def göster():
    for i in range (uz):
        print ("{:2d}.kart: {}-{}" .format ((i+1), deste.kartlar[i][0], deste.kartlar[i][1]) )

from random import shuffle
deste = VantiGrubu()
uz = deste.ebat()
print ("Sıralı kartlar:\n", "-"*17, sep="")
göster()

print ("\nKarılı kartlar:\n", "-"*17, sep="")
deste.karıştır()
göster()

print ("\n-->Toplam kart sayısı:", deste.ebat() )
print ("Karılı destenin üstünden dağıtılan 1.kart:", deste.sonrakiKart(), "\n-->Kalan kart sayısı:", deste.ebat() )
print ("Karılı destenin üstünden dağıtılan 2.kart:", deste.sonrakiKart(), "\n-->Kalan kart sayısı:", deste.ebat() )
print ("Karılı destenin üstünden dağıtılan 3.kart:", deste.sonrakiKart(), "\n-->Kalan kart sayısı:", deste.ebat() )
