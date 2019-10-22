# coding:iso-8859-9 Türkçe

class Poker:
    def __init__ (self):
        self.kartlar = []
        for takım in ["Kupa", "Karo", "Maça", "Sinek"]:
            for sayı in range (2, 15): self.kartlar.append ((takım, sayı))

    def sonrakiKart (self): return self.kartlar.pop (0)
    def kartKaldıMı (self): return len (self.kartlar) > 0
    def ebat (self): return len (self.kartlar)
    def karıştır (self): shuffle (self.kartlar)

def göster (n):
    adlar = ['Oğlan', 'Kız', 'Papaz', 'As']
    for i in range (n):
        if deste.kartlar[i][1] <= 10: print ("{:2d}.kart: {}-{}" .format ((i+1), deste.kartlar[i][0], deste.kartlar[i][1]) )
        else: print ("{:2d}.kart: {}-{}" .format ((i+1), deste.kartlar[i][0], adlar[deste.kartlar[i][1]-11]) )

def royal_flaş (L1):
    if L1[0][0] == L1[1][0] == L1[2][0] == L1[3][0] == L1[4][0] == "Kupa" and\
        (L1[0][1] == 10 and L1[1][1] == 11 and L1[2][1] == 12 and L1[3][1] == 13 and L1[4][1] == 14):
        return True
    return False

def seri_flaş (L1):
    if L1[0][0] == L1[1][0] == L1[2][0] == L1[3][0] == L1[4][0] and\
        (L1[0][1]+1 == L1[1][1] and L1[1][1]+1 == L1[2][1] and L1[2][1]+1 == L1[3][1] and L1[3][1]+1 == L1[4][1]):
        return True
    return False

def dörtlü (L2):
    if L2[0][0] == L2[1][0] == L2[2][0] == L2[3][0] or\
        L2[1][0] == L2[2][0] == L2[3][0] == L2[4][0]:
        return True
    return False

def full (L2):
    if (L2[0][0] == L2[1][0] == L2[2][0] and L2[3][0] == L2[4][0]) or\
        (L2[0][0] == L2[1][0] and L2[2][0] == L2[3][0] == L2[4][0]):
        return True
    return False

def renk (L1):
    if L1[0][0] == L1[1][0] == L1[2][0] == L1[3][0] == L1[4][0]:
        return True
    return False

def seri (L2):
    if L2[0][0]+1 == L2[1][0] and L2[1][0]+1 == L2[2][0] and L2[2][0]+1 == L2[3][0] and L2[3][0]+1 == L2[4][0]:
        return True
    return False

def üçlü (L2):
    if L2[0][0] == L2[1][0] == L2[2][0] or L2[1][0] == L2[2][0] == L2[3][0] or L2[2][0] == L2[3][0] == L2[4][0]:
        return True
    return False

def döper (L2):
    if (L2[0][0] == L2[1][0] and (L2[2][0] == L2[3][0] or L2[3][0] == L2[4][0])) or\
        (L2[1][0] == L2[2][0] and L2[3][0] == L2[4][0]):
        return True
    return False

def per (L2):
    for i in range (4):
        if L2[i][0] == L2[i+1][0]: return True
    return False

from random import shuffle

deste = Poker()
#print ("Sıralı kartlar:\n", "-"*17, sep=""); göster (deste.ebat())

while not input ("\nEnt:"): # Yalın Ent'siz veri girişinde kırar...
    deste.karıştır()
    göster (5)
    el1 = el2 = []; sonuç = eniyiBeklenti = ""
    for i in range (5):
        el1 = el1 + [deste.sonrakiKart()]
        el2 = el2 + [(el1[i][1], el1[i][0])]
    el1.sort(); el2.sort()
    if royal_flaş (el1):
        sonuç = "[Royal Flaş]"; eniyiBeklenti = " ve kart almaz."
    elif seri_flaş (el1):
        sonuç = "[Seri Flaş]"; eniyiBeklenti = " ve kart almaz."
    elif dörtlü (el2):
        sonuç = "[Dörtlü]"; eniyiBeklenti = " ve kart almaz."
    elif full (el2):
        sonuç = "[Fûl]"; eniyiBeklenti = " ve kart almaz."
    elif renk (el1):
        sonuç = "[Renk]"; eniyiBeklenti = " ve kart almaz."
    elif seri (el2):
        sonuç = "[Seri]"; eniyiBeklenti = " ve kart almaz."
    elif üçlü (el2):
        sonuç = "[Üçlü]"; eniyiBeklenti = ", 2 kart alır ve dörtlü veya fûl umar."
    elif döper (el2):
        sonuç = "[Döper]"; eniyiBeklenti = ", 1 kart alır ve fûl umar."
    elif per (el2):
        sonuç = "[Per]"; eniyiBeklenti = ", 3 kart alır ve döper, üçlü, dörtlü veya fûl umar."
    else: sonuç = "[Tek]"; eniyiBeklenti = ", 1 kartla renk veya seriye bakar yoksa bu elden çıkar."

    print ("Poker elimde: ", sonuç, " var", eniyiBeklenti, sep="")
    deste = Poker()
