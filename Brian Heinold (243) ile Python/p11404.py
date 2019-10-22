# coding:iso-8859-9 Türkçe

class Vanti:
    def __init__ (self, takım, sayı):
        self.takım = takım
        self.sayı = sayı
    def __str__ (self):
        adlar = ['Oğlan', 'Kız', 'Papaz', 'As']
        if self.sayı <= 10: return '{} {}'.format (self.takım, self.sayı)
        else: return '{} {}'.format (self.takım, adlar[self.sayı - 11])

from random import shuffle

class Vanti_grubu:
    def __init__ (self, kartlar = []): self.kartlar = kartlar
    def sonrakiKart (self): return self.kartlar.pop (0)
    def kartKaldıMı (self): return len (self.kartlar) > 0
    def ebat (self): return len (self.kartlar)
    def karıştır (self): shuffle (self.kartlar)

class Standart_deste (Vanti_grubu):
    def __init__ (self):
        self.kartlar = []
        for takım in ['Kupa', 'Karo', 'Maça', 'Sinek']:
            for sayı in range (2, 15): self.kartlar.append (Vanti (takım, sayı))

"""
class Pinochle_deste (Vanti_grubu):
    def __init__ (self):
        self.kartlar = []
        for takım in ['Kupa', 'Karo', 'Maça', 'Sinek']:
            for sayı in range (9, 15): self.kartlar.append (Vanti (takım, sayı))
"""

deste = Standart_deste()
print ("Dizili Deste:\n","-"*20, sep="")
for i in range (len (deste.kartlar) ): print ((i+1), ".kart: ", deste.kartlar[i], sep="")
deste.karıştır()
print ("\nKarılı Deste:\n","-"*20, sep="")
for i in range (len (deste.kartlar) ): print ((i+1), ".kart: ", deste.kartlar[i], sep="")

yeniKart = deste.sonrakiKart()
print()
print ('==> ', yeniKart, sep="")
tahmin = input ("Bir sonraki çekeceğin kart yüksek (y) mi, düşük (d) mü?: ").lower()
ardışıkTutturma = 0
while (tahmin == 'y' or tahmin == 'd'):
    if not deste.kartKaldıMı():
        deste = Standart_deste()
        deste.shuffle()
    eskiKart = yeniKart
    yeniKart = deste.sonrakiKart()
    print ('==> ', yeniKart, sep="")
    if (tahmin == 'y' and yeniKart.sayı > eskiKart.sayı or\
            tahmin == 'd' and yeniKart.sayı < eskiKart.sayı):
        ardışıkTutturma = ardışıkTutturma + 1
        print ("Bravo! Arka arkaya ", ardışıkTutturma, ".isabetli tahminin!", sep="")
    elif (tahmin == 'y' and yeniKart.sayı < eskiKart.sayı or\
            tahmin == 'd' and yeniKart.sayı > eskiKart.sayı):
        ardışıkTutturma = 0
        print ('YANLIŞ, sıfırlandın!')
    else: print ('Eşitlik var.')

    tahmin = input ("\nBir sonraki çekeceğin kart yüksek (y) mi, düşük (d) mü?: ").lower()
