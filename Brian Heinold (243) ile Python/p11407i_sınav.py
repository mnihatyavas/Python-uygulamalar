# coding:iso-8859-9 T�rk�e

class Poker:
    def __init__ (self):
        self.kartlar = []
        for tak�m in ["Kupa", "Karo", "Ma�a", "Sinek"]:
            for say� in range (2, 15): self.kartlar.append ((tak�m, say�))

    def sonrakiKart (self): return self.kartlar.pop (0)
    def kartKald�M� (self): return len (self.kartlar) > 0
    def ebat (self): return len (self.kartlar)
    def kar��t�r (self): shuffle (self.kartlar)

def g�ster (n):
    adlar = ['O�lan', 'K�z', 'Papaz', 'As']
    for i in range (n):
        if deste.kartlar[i][1] <= 10: print ("{:2d}.kart: {}-{}" .format ((i+1), deste.kartlar[i][0], deste.kartlar[i][1]) )
        else: print ("{:2d}.kart: {}-{}" .format ((i+1), deste.kartlar[i][0], adlar[deste.kartlar[i][1]-11]) )

def royal_fla� (L1):
    if L1[0][0] == L1[1][0] == L1[2][0] == L1[3][0] == L1[4][0] == "Kupa" and\
        (L1[0][1] == 10 and L1[1][1] == 11 and L1[2][1] == 12 and L1[3][1] == 13 and L1[4][1] == 14):
        return True
    return False

def seri_fla� (L1):
    if L1[0][0] == L1[1][0] == L1[2][0] == L1[3][0] == L1[4][0] and\
        (L1[0][1]+1 == L1[1][1] and L1[1][1]+1 == L1[2][1] and L1[2][1]+1 == L1[3][1] and L1[3][1]+1 == L1[4][1]):
        return True
    return False

def d�rtl� (L2):
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

def ��l� (L2):
    if L2[0][0] == L2[1][0] == L2[2][0] or L2[1][0] == L2[2][0] == L2[3][0] or L2[2][0] == L2[3][0] == L2[4][0]:
        return True
    return False

def d�per (L2):
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
#print ("S�ral� kartlar:\n", "-"*17, sep=""); g�ster (deste.ebat())

while not input ("\nEnt:"): # Yal�n Ent'siz veri giri�inde k�rar...
    deste.kar��t�r()
    g�ster (5)
    el1 = el2 = []; sonu� = eniyiBeklenti = ""
    for i in range (5):
        el1 = el1 + [deste.sonrakiKart()]
        el2 = el2 + [(el1[i][1], el1[i][0])]
    el1.sort(); el2.sort()
    if royal_fla� (el1):
        sonu� = "[Royal Fla�]"; eniyiBeklenti = " ve kart almaz."
    elif seri_fla� (el1):
        sonu� = "[Seri Fla�]"; eniyiBeklenti = " ve kart almaz."
    elif d�rtl� (el2):
        sonu� = "[D�rtl�]"; eniyiBeklenti = " ve kart almaz."
    elif full (el2):
        sonu� = "[F�l]"; eniyiBeklenti = " ve kart almaz."
    elif renk (el1):
        sonu� = "[Renk]"; eniyiBeklenti = " ve kart almaz."
    elif seri (el2):
        sonu� = "[Seri]"; eniyiBeklenti = " ve kart almaz."
    elif ��l� (el2):
        sonu� = "[��l�]"; eniyiBeklenti = ", 2 kart al�r ve d�rtl� veya f�l umar."
    elif d�per (el2):
        sonu� = "[D�per]"; eniyiBeklenti = ", 1 kart al�r ve f�l umar."
    elif per (el2):
        sonu� = "[Per]"; eniyiBeklenti = ", 3 kart al�r ve d�per, ��l�, d�rtl� veya f�l umar."
    else: sonu� = "[Tek]"; eniyiBeklenti = ", 1 kartla renk veya seriye bakar yoksa bu elden ��kar."

    print ("Poker elimde: ", sonu�, " var", eniyiBeklenti, sep="")
    deste = Poker()
