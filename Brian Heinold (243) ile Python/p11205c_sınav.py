# coding:iso-8859-9 Türkçe

from random import randint
from random import random
from random import shuffle
cevap = input ("Yeni öğrenci dosyası yaratacak mısın? ")
if cevap == "E":
    dosya = open ("öğrenci.txt", "w")
    alfabe = "abcdefghijklmnopqrstuvwxyz"
    sayı = 0
    try:
        while not (0 < sayı < 1001): sayı = int (eval (input ("Öğrenci sayısını gir [1->1000]: ")))
    except Exception: sayı = randint (1, 1000)
    L = list (alfabe)
    for i in range (sayı):
        if random() >= 0.75: isim = 3
        else: isim = 2
        ad = ""
        for j in range (isim):
            shuffle (L)
            ad = ad + "".join (L)[:randint (3, 10)] + " "
        ad = ad[:len (ad)-1]
        L1 = ad.split (" ")
        print (ad + "\t" + L1[len (L1)-1] + "@eposta.com.tr" + "\t" + "555-" + str (randint (1000, 9999)), file = dosya)
    dosya.close()

print()
L = [satır.strip().split ("\t") for satır in open ("öğrenci.txt")]
from pprint import pprint
print (len (L), " kişilik ÖĞRENCİ listesinin dosyadan dökümü:\n", "="*48, sep="")
pprint (L)

dosya = open ("öğrenci2.txt", "w")
for i in range (len (L)):
    ad = ""
    isim = str (L[i][0]).split (" ");
    for j in range (len (isim)): ad = ad + str (isim[j][0]).upper() + isim[j][1:] + " "
    ad = ad[:len (ad)-1]
    print (ad + "\t" + L[i][1] + "\t" + "551-" + L[i][2], file = dosya)
dosya.close()

print()
L = [satır.strip().split ("\t") for satır in open ("öğrenci2.txt")]
print (len (L), " kişilik ÖĞRENCİ-2 listesinin dosyadan dökümü:\n", "="*50, sep="")
pprint (L)

print()
dosya = open ("öğrenci3.txt", "w")
for i in range (len (L)):
    ad = ""
    isim = str (L[i][0]).split (" ");
    for j in range (len (isim)-1): ad = ad + str (isim[j][0]) + "."
    ad = ad + str (isim[len (isim)-1])
    print (ad + "\t" + L[i][1] + "\t" + L[i][2], file = dosya)
dosya.close()

print()
L = [satır.strip().split ("\t") for satır in open ("öğrenci3.txt")]
print (len (L), " kişilik ÖĞRENCİ-3 listesinin dosyadan dökümü:\n", "="*50, sep="")
pprint (L)
