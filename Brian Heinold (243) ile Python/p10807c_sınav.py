# coding:iso-8859-9 Türkçe

L1 = ["Fransa'nın başkenti?", "İtalya'nın başkenti?", "Türkiye'nin başkenti?", "Yunanistan'ın başkenti?", "İran'ın başkenti?", "Gürcistan'ın başkenti?", "İngiltere'nin başkenti?", "Almanya'nın başkenti?", "Japonya'nın başkenti?", "Kazakistan'ın başkenti?"]
L2 = ["Paris", "Roma", "Ankara", "Atina", "Tahran", "Tiblis", "Londra", "Berlin", "Tokyo", "Astana"]
L3 = [0,1,2,3,4,5,6,7,8,9]

from random import randint, shuffle, choice
shuffle (L3)
sayaç = 0
for i in range (5):
    if input (L1[L3[i]] + " ").lower() == L2[L3[i]].lower(): sayaç +=1
print ("Sorulan 5 sorudan", sayaç, "adetini doğru cevapladınız ve notunuz:", sayaç*100/5)

L1 = ["ibne", "orospu", "göt", "am", "sik", "ossur", "sıç", "bok"]
dizge = input ("\nİçinde 'ibne, orospu, göt, am, sik, bok, ossur, sıç' kelimeli metin girin: ").lower()
if len (dizge) == 0: dizge = "Götünü amını siktiğimin sıçtığımın ossuruklu ibne orospu çocuğu!".lower()
for kelime in L1: dizge = dizge.replace (kelime, "*"*len (kelime))
print ("Sansürlü metnimiz:", dizge)
print()
kelime = choice (L2)
print (kelime, "kelimesinin", len (kelime)*2, "adet anagramı: ", end="")
for i in range (len (kelime)*2):
    L1 = list (kelime.lower())
    shuffle (L1)
    kelime = "".join (L1)
    print (kelime[0].upper(), kelime[1:], sep="", end=" ")
print()
dizge = input ("\nGeçerli [(090-)551-555-94-64] bir telefon no girin: ")
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
print ("Girdiğiniz telefon numarasının geçerliliği:", kontrol)
