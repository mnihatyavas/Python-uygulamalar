# coding:iso-8859-9 T�rk�e

from random import randint
from random import random
from random import shuffle
cevap = input ("Yeni ��renci dosyas� yaratacak m�s�n? ")
if cevap == "E":
    dosya = open ("��renci.txt", "w")
    alfabe = "abcdefghijklmnopqrstuvwxyz"
    say� = 0
    try:
        while not (0 < say� < 1001): say� = int (eval (input ("��renci say�s�n� gir [1->1000]: ")))
    except Exception: say� = randint (1, 1000)
    L = list (alfabe)
    for i in range (say�):
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
L = [sat�r.strip().split ("\t") for sat�r in open ("��renci.txt")]
from pprint import pprint
print (len (L), " ki�ilik ��RENC� listesinin dosyadan d�k�m�:\n", "="*48, sep="")
pprint (L)

dosya = open ("��renci2.txt", "w")
for i in range (len (L)):
    ad = ""
    isim = str (L[i][0]).split (" ");
    for j in range (len (isim)): ad = ad + str (isim[j][0]).upper() + isim[j][1:] + " "
    ad = ad[:len (ad)-1]
    print (ad + "\t" + L[i][1] + "\t" + "551-" + L[i][2], file = dosya)
dosya.close()

print()
L = [sat�r.strip().split ("\t") for sat�r in open ("��renci2.txt")]
print (len (L), " ki�ilik ��RENC�-2 listesinin dosyadan d�k�m�:\n", "="*50, sep="")
pprint (L)

print()
dosya = open ("��renci3.txt", "w")
for i in range (len (L)):
    ad = ""
    isim = str (L[i][0]).split (" ");
    for j in range (len (isim)-1): ad = ad + str (isim[j][0]) + "."
    ad = ad + str (isim[len (isim)-1])
    print (ad + "\t" + L[i][1] + "\t" + L[i][2], file = dosya)
dosya.close()

print()
L = [sat�r.strip().split ("\t") for sat�r in open ("��renci3.txt")]
print (len (L), " ki�ilik ��RENC�-3 listesinin dosyadan d�k�m�:\n", "="*50, sep="")
pprint (L)
