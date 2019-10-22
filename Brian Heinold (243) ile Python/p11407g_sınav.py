# coding:iso-8859-9 T�rk�e

class Deste ():
    def __init__ (self):
        self.kartlar = []
        for tak�m in ['Kupa', 'Karo', 'Ma�a', 'Sinek']:
            for say� in range (2, 15): self.kartlar.append ((tak�m, say�))

    def __str__ (self):
        adlar = ['O�lan', 'K�z', 'Papaz', 'As']
        if self.say� <= 10: return '{} {}'.format (self.tak�m, self.say�)
        else: return '{} {}'.format (self.tak�m, adlar[self.say� - 11])

deste = Deste()
uz = len (deste.kartlar)
#for i in range (uz): print ((i+1), ".kart: ", deste.kartlar[i], sep="")

from random import shuffle
shuffle (deste.kartlar)
#for i in range (uz): print ((i+1), ".kart: ", deste.kartlar[i], sep="")

L1 = [deste.kartlar[i] for i in range (uz//2)]
L2 = [deste.kartlar[i] for i in range (uz//2, uz)]
#for i in range (len (L1)): print ((i+1), ".kart: ", L1[i][0], "-", L1[i][1], sep="")
#for i in range (len (L2)): print ((i+1), ".kart: ", L2[i][0], "-", L2[i][1], sep="")

while len (L1) > 0 and len (L2) > 0 and not input ("Devam: [Ent]"):
    kart1 = L1.pop (0)
    kart2 = L2.pop (0)
    #print (kart1[1], kart2[1])
    if int (kart1[1]) > int (kart2[1]):
        L1 = L1 + [(kart1[0], kart1[1])]
        L1 = L1 + [(kart2[0], kart2[1])]
        print (kart1, ">", kart2, "==> �lk oyuncu kazan�r ve toplam kart�:", len (L1))
    elif int (kart1[1]) < int (kart2[1]):
        L2 = L2 + [(kart2[0], kart2[1])]
        L2 = L2 + [(kart1[0], kart1[1])]
        print (kart1, "<", kart2, "==> �kinci oyuncu kazan�r ve toplam kart�:", len (L2))
    else: print (kart1, "=", kart2, "==> Berabere ve kartlar ��pe")
print ("OYUN B�TT�, ve elde kalan kart say�lar�:", len (L1), len (L2) )

