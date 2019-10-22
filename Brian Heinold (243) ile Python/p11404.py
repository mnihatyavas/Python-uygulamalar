# coding:iso-8859-9 T�rk�e

class Vanti:
    def __init__ (self, tak�m, say�):
        self.tak�m = tak�m
        self.say� = say�
    def __str__ (self):
        adlar = ['O�lan', 'K�z', 'Papaz', 'As']
        if self.say� <= 10: return '{} {}'.format (self.tak�m, self.say�)
        else: return '{} {}'.format (self.tak�m, adlar[self.say� - 11])

from random import shuffle

class Vanti_grubu:
    def __init__ (self, kartlar = []): self.kartlar = kartlar
    def sonrakiKart (self): return self.kartlar.pop (0)
    def kartKald�M� (self): return len (self.kartlar) > 0
    def ebat (self): return len (self.kartlar)
    def kar��t�r (self): shuffle (self.kartlar)

class Standart_deste (Vanti_grubu):
    def __init__ (self):
        self.kartlar = []
        for tak�m in ['Kupa', 'Karo', 'Ma�a', 'Sinek']:
            for say� in range (2, 15): self.kartlar.append (Vanti (tak�m, say�))

"""
class Pinochle_deste (Vanti_grubu):
    def __init__ (self):
        self.kartlar = []
        for tak�m in ['Kupa', 'Karo', 'Ma�a', 'Sinek']:
            for say� in range (9, 15): self.kartlar.append (Vanti (tak�m, say�))
"""

deste = Standart_deste()
print ("Dizili Deste:\n","-"*20, sep="")
for i in range (len (deste.kartlar) ): print ((i+1), ".kart: ", deste.kartlar[i], sep="")
deste.kar��t�r()
print ("\nKar�l� Deste:\n","-"*20, sep="")
for i in range (len (deste.kartlar) ): print ((i+1), ".kart: ", deste.kartlar[i], sep="")

yeniKart = deste.sonrakiKart()
print()
print ('==> ', yeniKart, sep="")
tahmin = input ("Bir sonraki �ekece�in kart y�ksek (y) mi, d���k (d) m�?: ").lower()
ard���kTutturma = 0
while (tahmin == 'y' or tahmin == 'd'):
    if not deste.kartKald�M�():
        deste = Standart_deste()
        deste.shuffle()
    eskiKart = yeniKart
    yeniKart = deste.sonrakiKart()
    print ('==> ', yeniKart, sep="")
    if (tahmin == 'y' and yeniKart.say� > eskiKart.say� or\
            tahmin == 'd' and yeniKart.say� < eskiKart.say�):
        ard���kTutturma = ard���kTutturma + 1
        print ("Bravo! Arka arkaya ", ard���kTutturma, ".isabetli tahminin!", sep="")
    elif (tahmin == 'y' and yeniKart.say� < eskiKart.say� or\
            tahmin == 'd' and yeniKart.say� > eskiKart.say�):
        ard���kTutturma = 0
        print ('YANLI�, s�f�rland�n!')
    else: print ('E�itlik var.')

    tahmin = input ("\nBir sonraki �ekece�in kart y�ksek (y) mi, d���k (d) m�?: ").lower()
