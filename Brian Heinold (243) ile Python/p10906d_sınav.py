# coding:iso-8859-9 T�rk�e

L = input ("Ayn�/farkl� kelimeler girin: ").lower().split (" ")
L.sort()
saya� = 0
for i in range (len (L) - 1):
    if L[i] == L[i+1]: saya� +=1
print (L, "\nListede birbiriyle ayn� olan kelime say�s�:", saya�)

from random import randint
saya� = 0
j = randint (0, len (L) - 1)
kelime = list (L[j])
kelime.sort()
for i in range (len (kelime) - 1):
    if kelime[i] == kelime[i+1]: saya� +=1
print ("Tesad�fi se�ilen [", L[j], "=", "".join (kelime), "] kelimesinde ayn� harf say�s�: ", saya�, " adettir.", sep="")

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
    print ("�oklu kelimesi ve harfi olmayan kelimeler:", L)
    print ("�oklu kelimesi ve harfi olmayan tesad�fi tek bir kelime:",  L[randint (0, len (L)-1)])