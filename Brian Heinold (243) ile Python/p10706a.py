# coding:iso-8859-9 Türkçe

from random import randint

L = []
for i in range (50): L.append (randint (1,100))
L2 = L[:]
print (L)
print()
for i in range (len(L)): L[i] = L[i]**2
print (L)
print()
sayaç = 0
for k in L2:
    if k > 40: sayaç +=1
print ("50 elemanlı gelişigüzel listede 40'den büyük eleman sayısı:", sayaç)
L3=[]
for i in range (5000): L3.append (randint (0,50))
frekans = []
for i in range (0,51):
    frekans.append (L3.count (i))
    print (i, "frekans:", frekans[i], ", yüzdesi: ", 100*frekans[i]/5000)
print ("\nFrekanslar toplamı:", sum (frekans), ", ortalaması:", round (sum(frekans)/len(frekans), 2))
frekans.sort()
print ("\nEn düşük 2 frekans:", frekans[0], "ve", frekans[1])
print ("En yüksek 2 frekans:", frekans[49], "ve", frekans[50])