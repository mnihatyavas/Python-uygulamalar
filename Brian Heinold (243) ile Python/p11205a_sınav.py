# coding:iso-8859-9 T�rk�e

from random import randint
from random import shuffle
cevap = input ("Yeni ��renci dosyas� yaratacak m�s�n? ")
if cevap == "E":
    dosya = open ("��renci.txt", "w")
    alfabe = "abcdefghijklmno�prstuvyz"
    say� = 0
    try:
        while not (0 < say� < 1001): say� = int (eval (input ("��renci say�s�n� gir [1->1000]: ")))
    except Exception: say� = randint (1, 1000)
    for i in range (say�):
        L = list (alfabe)
        shuffle (L)
        ad = "".join (L)
        ad = ad[0].upper() + "." + ad[1].upper() + ad[2:11]
        print (ad, randint (0, 100), randint (0, 100), randint (0, 100), file = dosya)
    dosya.close()

print()
L = [sat�r.strip().split (" ") for sat�r in open ("��renci.txt")]
from pprint import pprint
print (len (L), " ki�ilik ��renci listesinin dosyadan d�k�m�:\n", "="*45, sep="")
pprint (L)

print()
L.sort()
print (len (L), " ki�ilik ��renci listesinin A->Z d�k�m�:\n", "="*45, sep="")
pprint (L)

print()
say� = 1
print (len (L), " ki�ilik ��renci listesinin A->Z formatl� d�k�m�:\n", "-"*53, sep="")
print ("S�raNo Ad Soyad     Quiz  �dev Final Ortalama\n", "="*44, sep="")
for k in L:
    print ("{:4d}   {:12s} {:3d}   {:3d}  {:3d}   {:6.2f}" .format (say�, k[0], int(k[1]), int(k[2]), int(k[3]), (eval (k[1]) * 0.30 + eval (k[2]) * 0.10 + eval (k[3]) * 0.60)) )
    say� +=1
print ("-"*44)
print ("{:4d} Ortalamalar: {:6.2f}{:6.2f}{:6.2f} {:6.2f}" .format (
    sum ([1 for i in range (len (L))]),
    sum ([int (L[i][1]) for i in range (len (L))]) / len (L),
    sum ([int (L[i][2]) for i in range (len (L))]) / len (L),
    sum ([int (L[i][3]) for i in range (len (L))]) / len (L),
    sum ([int (L[i][1]) for i in range (len (L))]) / len (L) * 0.30 + sum ([int (L[i][2]) for i in range (len (L))]) / len (L) * 0.10 + sum ([int (L[i][3]) for i in range (len (L))]) / len (L) * 0.60) )
