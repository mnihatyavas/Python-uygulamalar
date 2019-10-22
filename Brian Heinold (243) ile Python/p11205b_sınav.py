# coding:iso-8859-9 T�rk�e

from random import randint
from random import shuffle
cevap = input ("Yeni internet kafe dosyas� yaratacak m�s�n? ")
if cevap == "E":
    dosya = open ("kafe.txt", "w")
    say� = 0
    try:
        while not (0 < say� < 51): say� = int (eval (input ("Masa say�s�n� gir [1->50]: ")))
    except Exception: say� = randint (1, 50)
    for i in range (say�):
        saat1 = 9*60
        while saat1 < 24*60:
            saat2 = randint (saat1, 24*60)
            if randint (0,1) == 0: doluluk = "Bo�"
            else: doluluk = "Dolu"
            print ("MasaNo:{:02d} {:02d}:{:02d} {:02d}:{:02d} {:s}" .format (i+1, saat1//60, saat1%60, saat2//60, saat2%60, doluluk), file = dosya)
            if saat2 >= 23*60+59: break
            else: saat1 = saat2
    dosya.close()

print()
L = [sat�r.strip().split (" ") for sat�r in open ("kafe.txt")]
from pprint import pprint
print ("[09:00-->24:00] aras� toplam: ", len (L), " oturumluk masa listesinin dosyadan d�k�m�:\n", "="*75, sep="")
pprint (L)

print ("\n1 saatten fazla dolu olan oturumlar�n listesi:\n", "="*50, sep="")
for k in L:
    fark = (int (k[2][:2])*60 + int (k[2][-2:])) - (int (k[1][:2])*60 + int (k[1][-2:]))
    if k[3] == "Dolu" and fark >= 60:
        print ("{:s}, {:s} {:s}, S�re: {:3d} dakika = ({:d}:{:02})" .format (k[0], k[2], k[1], fark, fark//60, fark%60) )
