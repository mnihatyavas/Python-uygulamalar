# coding:iso-8859-9 Türkçe

from random import randint
from random import shuffle
cevap = input ("Yeni internet kafe dosyası yaratacak mısın? ")
if cevap == "E":
    dosya = open ("kafe.txt", "w")
    sayı = 0
    try:
        while not (0 < sayı < 51): sayı = int (eval (input ("Masa sayısını gir [1->50]: ")))
    except Exception: sayı = randint (1, 50)
    for i in range (sayı):
        saat1 = 9*60
        while saat1 < 24*60:
            saat2 = randint (saat1, 24*60)
            if randint (0,1) == 0: doluluk = "Boş"
            else: doluluk = "Dolu"
            print ("MasaNo:{:02d} {:02d}:{:02d} {:02d}:{:02d} {:s}" .format (i+1, saat1//60, saat1%60, saat2//60, saat2%60, doluluk), file = dosya)
            if saat2 >= 23*60+59: break
            else: saat1 = saat2
    dosya.close()

print()
L = [satır.strip().split (" ") for satır in open ("kafe.txt")]
from pprint import pprint
print ("[09:00-->24:00] arası toplam: ", len (L), " oturumluk masa listesinin dosyadan dökümü:\n", "="*75, sep="")
pprint (L)

print ("\n1 saatten fazla dolu olan oturumların listesi:\n", "="*50, sep="")
for k in L:
    fark = (int (k[2][:2])*60 + int (k[2][-2:])) - (int (k[1][:2])*60 + int (k[1][-2:]))
    if k[3] == "Dolu" and fark >= 60:
        print ("{:s}, {:s} {:s}, Süre: {:3d} dakika = ({:d}:{:02})" .format (k[0], k[2], k[1], fark, fark//60, fark%60) )
