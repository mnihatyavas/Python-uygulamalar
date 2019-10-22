# coding:iso-8859-9 Türkçe

from random import randint
from random import shuffle
cevap = input ("Yeni öğrenci dosyası yaratacak mısın? ")
if cevap == "E":
    dosya = open ("öğrenci.txt", "w")
    alfabe = "abcdefghijklmnoöprstuvyz"
    sayı = 0
    try:
        while not (0 < sayı < 1001): sayı = int (eval (input ("Öğrenci sayısını gir [1->1000]: ")))
    except Exception: sayı = randint (1, 1000)
    for i in range (sayı):
        L = list (alfabe)
        shuffle (L)
        ad = "".join (L)
        ad = ad[0].upper() + "." + ad[1].upper() + ad[2:11]
        print (ad, randint (0, 100), randint (0, 100), randint (0, 100), file = dosya)
    dosya.close()

print()
L = [satır.strip().split (" ") for satır in open ("öğrenci.txt")]
from pprint import pprint
print (len (L), " kişilik öğrenci listesinin dosyadan dökümü:\n", "="*45, sep="")
pprint (L)

print()
L.sort()
print (len (L), " kişilik öğrenci listesinin A->Z dökümü:\n", "="*45, sep="")
pprint (L)

print()
sayı = 1
print (len (L), " kişilik öğrenci listesinin A->Z formatlı dökümü:\n", "-"*53, sep="")
print ("SıraNo Ad Soyad     Quiz  Ödev Final Ortalama\n", "="*44, sep="")
for k in L:
    print ("{:4d}   {:12s} {:3d}   {:3d}  {:3d}   {:6.2f}" .format (sayı, k[0], int(k[1]), int(k[2]), int(k[3]), (eval (k[1]) * 0.30 + eval (k[2]) * 0.10 + eval (k[3]) * 0.60)) )
    sayı +=1
print ("-"*44)
print ("{:4d} Ortalamalar: {:6.2f}{:6.2f}{:6.2f} {:6.2f}" .format (
    sum ([1 for i in range (len (L))]),
    sum ([int (L[i][1]) for i in range (len (L))]) / len (L),
    sum ([int (L[i][2]) for i in range (len (L))]) / len (L),
    sum ([int (L[i][3]) for i in range (len (L))]) / len (L),
    sum ([int (L[i][1]) for i in range (len (L))]) / len (L) * 0.30 + sum ([int (L[i][2]) for i in range (len (L))]) / len (L) * 0.10 + sum ([int (L[i][3]) for i in range (len (L))]) / len (L) * 0.60) )
