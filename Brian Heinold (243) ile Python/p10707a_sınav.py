# coding:iso-8859-9 Türkçe

from random import randint
liste=[]
for i in range (randint (2,50)): liste.append (randint (0,10))
print ("Listemizdeki sayaç eleman sayısı:", len (liste))
print ("Listemizdeki son elemanın değeri:", liste[len (liste) -1])
print ("Listemizdeki elemanlar:", liste)
liste2 = liste[:]
liste2.sort()
print ("Sıralı listemizdeki elemanlar:", liste2)
liste2.reverse()
print ("Ters sıralı listemizdeki elemanlar:", liste2)
if 5 in liste2:
    print ("Evet, 5 listemizde mevcut!")
    print ("   ve listemizde sayaç", liste2.count (5), "adet 5 var.")
else: print ("Hayır, 5 listemizde mevcut değil!")
liste2 = liste[:]
print ("Listemizden çıkarılan ilk ve son eleman değerleri:", liste2.pop (0), liste2.pop (len (liste2)-1))
liste2.sort()
print ("Sıralı listemizdeki kalan", len (liste2), "elemanlar:", liste2)
liste2 = liste[:]
liste2.sort()
sayaç = 0
for i in liste2:
    if i < 5: sayaç +=1
    else: break
print ("Orijinal listemizde 5 değerinden küçük eleman sayısı:", sayaç)
print ("Liste elemanları toplamı ve ortalaması:", sum (liste2), round (sum(liste2)/len(liste2), 2))
print ("Listemizdeki enbüyük 2 eleman değerleri:", liste2[len(liste2)-1], liste2[len(liste2)-2])
print ("Listemizdeki enküçük 2 eleman değerleri:", liste2[0], liste2[1])
sayaç = 0
for i in liste2:
    if i % 2 == 0: sayaç +=1
print ("Listemizdeki çift değerli elemanların sayısı:", sayaç)
liste2 = [8, 9, 10]
liste2[1] = 17
liste2.append (4); liste2.append (5); liste2.append (6)
del liste2[0] # veya liste2.remove (liste2[0]) veya liste2.pop (0)
liste2.sort()
liste2 = liste2*2
liste2.insert (3, 17)
print ("[8,9,10]'dan işlenmiş listemizin son dökümü:", liste2)
for i in range (len (liste2)):
    if liste2[i] > 10: liste2[i] = 10
print ("10'dan büyükleri 10'laşan listemiz:", liste2)
