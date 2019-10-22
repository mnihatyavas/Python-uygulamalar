# coding:iso-8859-9 Türkçe

L = input ("Aynı/farklı kelimeler girin: ").lower().split (" ")
L.sort()
sayaç = 0
for i in range (len (L) - 1):
    if L[i] == L[i+1]: sayaç +=1
print (L, "\nListede birbiriyle aynı olan kelime sayısı:", sayaç)

from random import randint
sayaç = 0
j = randint (0, len (L) - 1)
kelime = list (L[j])
kelime.sort()
for i in range (len (kelime) - 1):
    if kelime[i] == kelime[i+1]: sayaç +=1
print ("Tesadüfi seçilen [", L[j], "=", "".join (kelime), "] kelimesinde aynı harf sayısı: ", sayaç, " adettir.", sep="")

i = 0
while i < len (L) - 1:
    if len (L) > 1 and L[i] == L[i+1]: del L[i]
    else: i +=1
i = 0
while i < len (L):
    kelime = list (L[i])
    kelime.sort()
    for j in range (len (kelime)-1):
        if kelime[j] == kelime[j+1]: del L[i]; break
    else: i +=1
if len (L):
    print ("Çoklu kelimesi ve harfi olmayan kelimeler:", L)
    print ("Çoklu kelimesi ve harfi olmayan tesadüfi tek bir kelime:",  L[randint (0, len (L)-1)])