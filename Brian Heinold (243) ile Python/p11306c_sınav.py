# coding:iso-8859-9 Türkçe

def eşleşme (k1, k2):
    if len (k1) > len (k2): k1, k2 = k2, k1
    sayaç = 0
    for i in range (len (k1)):
        if k1[i] == k2[i]: sayaç +=1
    return sayaç

def endeks (h, L1):
    L = []
    for i in range (len (L1)):
        for j in range (len (str (L1[i]))):
            if h == str (L1[i])[j].lower(): L = L + [(i, j)]
    return L

def sıralıMı (L):
    L1 = L.copy()
    L1.sort()
    return L == L1

def kontrol (kelime, L):
    for i in range (len (L)):
        sayaç = 0
        if len (kelime) == len (str (L[i])):
            for j in range (len (kelime)):
                if kelime[j] != str (L[i])[j]: sayaç +=1
        if sayaç == 1: print (kelime, "-->", L[i])

L = [satır.strip() for satır in open ("sorular.txt")]
from pprint import pprint
pprint (L)

print()
for i in range (len (L)-1):
    s1 = str (L[i])
    s2 = str (L[i+1])
    print (s1, "\n", s2, "\nKarakter eşleşme sayısı = ", eşleşme (s1, s2), "\n", sep="")

pprint (L)
alfabe = "abcçdefgğhıijklmnoöpqrsştuüvwxyz"
for i in range (len (alfabe)):
    L1 = endeks (alfabe[i], L)
    print ("\n", alfabe[i], " harfinin bulunduğu konumlar==>\n", L1, ", ve sayısı: ", len (L1), "\n", sep="")

print()
from random import random
for k in L:
    L1 = list (k);
    if random() >= 0.5: L1.sort()
    print ("".join (L1).strip(), " {Sıralı mı? ", sıralıMı (L1), "}\n", sep="")

print()
L1 = L2 = []
for satır in L: L1 = L1 + satır.lower().split (" ")
L1.sort()
L2 = L2 + [L1[0]]
for i in range (len (L1)-1):
    if L1[i] != L1[i+1]: L2 = L2 + [L1[i+1]]
print ("Uzunlukları aynı, tek karakteri farklı kelimeler:")
for k in L2: kontrol (k, L2)
