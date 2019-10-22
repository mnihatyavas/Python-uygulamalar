# coding:iso-8859-9 T�rk�e

def s�rala1 (L1):
    L1.sort()
    return L1

def s�ral�Ara (L, ad):
    for i in range (len (L)):
        if ad.lower() in str (L[i]).lower(): return "EVET, endeks: " + str (i)
    return "HAYIR"

def ortalamal�Ara (L, ad):
    alt = 0
    �st = len (L) - 1
    orta = (�st - alt) // 2
    if ad in str (L[len(L)-1]).lower(): return "EVET, endeks: " + str (len (L)-1)
    while True:
        aranan = str (L[orta]).lower()
        if ad in aranan: return "EVET, endeks: " + str (orta)
        elif �st-alt == 1 and ad not in str (L[orta+1]).lower(): return "HAYIR"
        else:
            if ad > aranan[2:aranan.index (";")]: alt = orta
            else: �st = orta
        orta = alt + (�st-alt)//2

L = [sat�r.strip() for sat�r in open ("��renci2.txt")]
for i in range (len (L)):
    k = str (L[i])
    k = k.replace ("\t", "; ")
    L[i] = [k]
    
from pprint import pprint
print (len (L), " ki�ilik OR�J�NAL ��renci dosyas� listesi:\n", "-"*44, sep="")
pprint (L)

print()
print (len (L), " ki�ilik, ad'a g�re A-->Z SIRALI ��renci dosyas� listesi:\n", "-"*59, sep="")
pprint (s�rala1 (L))

"""
print()
print (len (L), " ki�ilik, ad'a g�re ters Z-->A SIRALI ��renci dosyas� listesi:\n", "-"*64, sep="")
L.reverse()
pprint (L)
"""

print()
L1 = []
for k in L:
    k = str (k)
    L1 = L1 + [k[2:k.index (";")]]
#pprint (L1)

from random import shuffle
isim = input ("Listede bulmak istedi�in ��rencinin TAM ad ve soyad�n� girin: ")
if isim == "":
    shuffle (L1)
    isim = str (L1[0])
    print ("Listeden se�ilen tesad�fi isim:", isim)

print ("\nArad���n�z [", isim, "] isimli ��renci listede mevcut mu? ", s�ral�Ara (L, isim), sep="")

print ("\nArad���n�z [", isim, "] isimli ��renci listede mevcut mu? ", ortalamal�Ara (L, isim.lower()), sep="")
