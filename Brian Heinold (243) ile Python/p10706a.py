# coding:iso-8859-9 T�rk�e

from random import randint

L = []
for i in range (50): L.append (randint (1,100))
L2 = L[:]
print (L)
print()
for i in range (len(L)): L[i] = L[i]**2
print (L)
print()
saya� = 0
for k in L2:
    if k > 40: saya� +=1
print ("50 elemanl� geli�ig�zel listede 40'den b�y�k eleman say�s�:", saya�)
L3=[]
for i in range (5000): L3.append (randint (0,50))
frekans = []
for i in range (0,51):
    frekans.append (L3.count (i))
    print (i, "frekans:", frekans[i], ", y�zdesi: ", 100*frekans[i]/5000)
print ("\nFrekanslar toplam�:", sum (frekans), ", ortalamas�:", round (sum(frekans)/len(frekans), 2))
frekans.sort()
print ("\nEn d���k 2 frekans:", frekans[0], "ve", frekans[1])
print ("En y�ksek 2 frekans:", frekans[49], "ve", frekans[50])