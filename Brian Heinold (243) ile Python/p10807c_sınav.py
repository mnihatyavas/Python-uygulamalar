# coding:iso-8859-9 T�rk�e

L1 = ["Fransa'n�n ba�kenti?", "�talya'n�n ba�kenti?", "T�rkiye'nin ba�kenti?", "Yunanistan'�n ba�kenti?", "�ran'�n ba�kenti?", "G�rcistan'�n ba�kenti?", "�ngiltere'nin ba�kenti?", "Almanya'n�n ba�kenti?", "Japonya'n�n ba�kenti?", "Kazakistan'�n ba�kenti?"]
L2 = ["Paris", "Roma", "Ankara", "Atina", "Tahran", "Tiblis", "Londra", "Berlin", "Tokyo", "Astana"]
L3 = [0,1,2,3,4,5,6,7,8,9]

from random import randint, shuffle, choice
shuffle (L3)
saya� = 0
for i in range (5):
    if input (L1[L3[i]] + " ").lower() == L2[L3[i]].lower(): saya� +=1
print ("Sorulan 5 sorudan", saya�, "adetini do�ru cevaplad�n�z ve notunuz:", saya�*100/5)

L1 = ["ibne", "orospu", "g�t", "am", "sik", "ossur", "s��", "bok"]
dizge = input ("\n��inde 'ibne, orospu, g�t, am, sik, bok, ossur, s��' kelimeli metin girin: ").lower()
if len (dizge) == 0: dizge = "G�t�n� am�n� sikti�imin s��t���m�n ossuruklu ibne orospu �ocu�u!".lower()
for kelime in L1: dizge = dizge.replace (kelime, "*"*len (kelime))
print ("Sans�rl� metnimiz:", dizge)
print()
kelime = choice (L2)
print (kelime, "kelimesinin", len (kelime)*2, "adet anagram�: ", end="")
for i in range (len (kelime)*2):
    L1 = list (kelime.lower())
    shuffle (L1)
    kelime = "".join (L1)
    print (kelime[0].upper(), kelime[1:], sep="", end=" ")
print()
dizge = input ("\nGe�erli [(090-)551-555-94-64] bir telefon no girin: ")
if len (dizge) == 0: dizge = "090-551-555-94-64"
kontrol = True
L1 = dizge.split ("-")
if len (L1) == 5: kontrol = (len (L1[0]) == 3 and len (L1[1]) == 3 and len (L1[2]) == 3 and len (L1[3]) == 2 and len (L1[4]) == 2)
elif len (L1) == 4: kontrol = (len (L1[0]) == 3 and len (L1[1]) == 3 and len (L1[2]) == 2 and len (L1[3]) == 2)
else: kontrol = False
if kontrol:
    dizge = dizge.replace ("-", "")
    for i in range (len (dizge)):
        kontrol = dizge[i].isdigit()
        if not kontrol: break
print ("Girdi�iniz telefon numaras�n�n ge�erlili�i:", kontrol)
