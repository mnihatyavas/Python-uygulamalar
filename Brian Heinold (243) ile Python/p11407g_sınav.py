# coding:iso-8859-9 Türkçe

class Deste ():
    def __init__ (self):
        self.kartlar = []
        for takım in ['Kupa', 'Karo', 'Maça', 'Sinek']:
            for sayı in range (2, 15): self.kartlar.append ((takım, sayı))

    def __str__ (self):
        adlar = ['Oğlan', 'Kız', 'Papaz', 'As']
        if self.sayı <= 10: return '{} {}'.format (self.takım, self.sayı)
        else: return '{} {}'.format (self.takım, adlar[self.sayı - 11])

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
        print (kart1, ">", kart2, "==> İlk oyuncu kazanır ve toplam kartı:", len (L1))
    elif int (kart1[1]) < int (kart2[1]):
        L2 = L2 + [(kart2[0], kart2[1])]
        L2 = L2 + [(kart1[0], kart1[1])]
        print (kart1, "<", kart2, "==> İkinci oyuncu kazanır ve toplam kartı:", len (L2))
    else: print (kart1, "=", kart2, "==> Berabere ve kartlar çöpe")
print ("OYUN BİTTİ, ve elde kalan kart sayıları:", len (L1), len (L2) )

