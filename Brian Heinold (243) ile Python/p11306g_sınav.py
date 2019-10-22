# coding:iso-8859-9 Türkçe

def sırala1 (L1):
    L1.sort()
    return L1

def sıralıAra (L, ad):
    for i in range (len (L)):
        if ad.lower() in str (L[i]).lower(): return "EVET, endeks: " + str (i)
    return "HAYIR"

def ortalamalıAra (L, ad):
    alt = 0
    üst = len (L) - 1
    orta = (üst - alt) // 2
    if ad in str (L[len(L)-1]).lower(): return "EVET, endeks: " + str (len (L)-1)
    while True:
        aranan = str (L[orta]).lower()
        if ad in aranan: return "EVET, endeks: " + str (orta)
        elif üst-alt == 1 and ad not in str (L[orta+1]).lower(): return "HAYIR"
        else:
            if ad > aranan[2:aranan.index (";")]: alt = orta
            else: üst = orta
        orta = alt + (üst-alt)//2

L = [satır.strip() for satır in open ("öğrenci2.txt")]
for i in range (len (L)):
    k = str (L[i])
    k = k.replace ("\t", "; ")
    L[i] = [k]
    
from pprint import pprint
print (len (L), " kişilik ORİJİNAL öğrenci dosyası listesi:\n", "-"*44, sep="")
pprint (L)

print()
print (len (L), " kişilik, ad'a göre A-->Z SIRALI öğrenci dosyası listesi:\n", "-"*59, sep="")
pprint (sırala1 (L))

"""
print()
print (len (L), " kişilik, ad'a göre ters Z-->A SIRALI öğrenci dosyası listesi:\n", "-"*64, sep="")
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
isim = input ("Listede bulmak istediğin öğrencinin TAM ad ve soyadını girin: ")
if isim == "":
    shuffle (L1)
    isim = str (L1[0])
    print ("Listeden seçilen tesadüfi isim:", isim)

print ("\nAradığınız [", isim, "] isimli öğrenci listede mevcut mu? ", sıralıAra (L, isim), sep="")

print ("\nAradığınız [", isim, "] isimli öğrenci listede mevcut mu? ", ortalamalıAra (L, isim.lower()), sep="")
