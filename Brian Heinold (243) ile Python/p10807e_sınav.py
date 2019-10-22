# coding:iso-8859-9 Türkçe

L1 = [[0]*10 for i in range (8)]
print ("[8x10]'li listemiz:", L1)

from random import randint
for i in range (8):
    for j in range (10):
        L1[i][j] = randint (-10, 50)
print ("Değer atalı listemiz:", L1)

print ("Formatlı listemiz:")
for i in range (len (L1)):
    for j in range (len (L1[0])):
        print ("{:4d}" .format (L1[i][j]), end="")
    print()

print ("Listemizin ortalama değeri:", sum ([L1[i][j] for i in range (len (L1)) for j in range (len (L1[0]))]) / (len (L1) * len (L1[0])) )

from pprint import pprint
print ("pprint'li listemiz:")
pprint (L1)

print ("Listemizin enbüyük elemanı:", max ([L1[i][j] for i in range (len(L1)) for j in range (len(L1[0])) ]))
print ("Listemizin enküçük elemanı:", min ([L1[i][j] for i in range (len(L1)) for j in range (len(L1[0])) ]))
satır = randint (0, len (L1)-1)
kolon = randint (0, len (L1[0])-1)
print ("Listemizin", satır+1, ".satırdaki enbüyük elemanı:", max ([L1[satır][j] for j in range (len(L1[0])) ]))
print ("Listemizin", kolon+1, ".kolondaki enküçük elemanı:", min ([L1[i][kolon] for i in range (len(L1)) ]))

L1 = [[0]*8 for i in range (8)]
for i in range (len(L1)):
    for j in range(len(L1[0])):
        if (j+1)%2 == 1: L1[i][j] = 1
        else: L1[i][j] = 2
pprint (L1)

toplam1 = sum([L1[i][i] for i in range(len(L1))])
toplam2 = sum ([L1[i][i] for i in range (len(L1[0])-1,-1,-1)] )
eşit = (toplam1== toplam2)
for i in range(len(L1)):
    eşit = (toplam1 == sum ([L1[i][j] for j in range(len(L1[0]))] ))
if eşit: print ("[8x8] L1 listemiz sihirli kare (köşegen, satır ve kolonlar toplamı eşit=", toplam1, ") matrisDİR!")
else: print ("[8x8] L1 listemiz sihirli kare matris DEĞİLDİR!")
