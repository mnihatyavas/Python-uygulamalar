# coding:iso-8859-9 T�rk�e

from random import randint
liste=[]
for i in range (randint (2,50)): liste.append (randint (0,10))
print ("Listemizdeki saya� eleman say�s�:", len (liste))
print ("Listemizdeki son eleman�n de�eri:", liste[len (liste) -1])
print ("Listemizdeki elemanlar:", liste)
liste2 = liste[:]
liste2.sort()
print ("S�ral� listemizdeki elemanlar:", liste2)
liste2.reverse()
print ("Ters s�ral� listemizdeki elemanlar:", liste2)
if 5 in liste2:
    print ("Evet, 5 listemizde mevcut!")
    print ("   ve listemizde saya�", liste2.count (5), "adet 5 var.")
else: print ("Hay�r, 5 listemizde mevcut de�il!")
liste2 = liste[:]
print ("Listemizden ��kar�lan ilk ve son eleman de�erleri:", liste2.pop (0), liste2.pop (len (liste2)-1))
liste2.sort()
print ("S�ral� listemizdeki kalan", len (liste2), "elemanlar:", liste2)
liste2 = liste[:]
liste2.sort()
saya� = 0
for i in liste2:
    if i < 5: saya� +=1
    else: break
print ("Orijinal listemizde 5 de�erinden k���k eleman say�s�:", saya�)
print ("Liste elemanlar� toplam� ve ortalamas�:", sum (liste2), round (sum(liste2)/len(liste2), 2))
print ("Listemizdeki enb�y�k 2 eleman de�erleri:", liste2[len(liste2)-1], liste2[len(liste2)-2])
print ("Listemizdeki enk���k 2 eleman de�erleri:", liste2[0], liste2[1])
saya� = 0
for i in liste2:
    if i % 2 == 0: saya� +=1
print ("Listemizdeki �ift de�erli elemanlar�n say�s�:", saya�)
liste2 = [8, 9, 10]
liste2[1] = 17
liste2.append (4); liste2.append (5); liste2.append (6)
del liste2[0] # veya liste2.remove (liste2[0]) veya liste2.pop (0)
liste2.sort()
liste2 = liste2*2
liste2.insert (3, 17)
print ("[8,9,10]'dan i�lenmi� listemizin son d�k�m�:", liste2)
for i in range (len (liste2)):
    if liste2[i] > 10: liste2[i] = 10
print ("10'dan b�y�kleri 10'la�an listemiz:", liste2)
