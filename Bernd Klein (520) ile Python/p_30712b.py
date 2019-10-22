# coding:iso-8859-9 Türkçe
# p_30712b.py: İngilteredeki üniversitelere öğrenci kayıtları örneği.

import random
import numpy as np
from collections import Counter

def kaçıncıArada (değerim, bölümler, uçlar_1Mi=True):
    for i in range (0, len (bölümler)):
        if değerim < bölümler[i]: return i-1 if uçlar_1Mi else i
    return -1 if uçlar_1Mi else len (bölümler)

def ağırlıklıTercih (ibareler, gelmeAğırlıkları, kriptoluMu=True):
    if kriptoluMu: x = random.SystemRandom().random()
    else: x = np.random.random()
    gelmeYüzdeleriToplamı = [0] + list (np.cumsum (gelmeAğırlıkları))
    endeks = kaçıncıArada (x, gelmeYüzdeleriToplamı)
    return ibareler[endeks]

def veridosyasınıİşle (dosyaAdı):
    üniversiteler = []
    kayıtlılar = []
    with open (dosyaAdı) as dosya:
        toplamKayıtlı = 0
        dosya.readline()
        for satır in dosya:
            üniversite, kayıtlı = satır.split (", ")
            üniversite = üniversite[1:-1]
            kayıtlı = eval (kayıtlı)
            kayıtlılar.append (kayıtlı)
            üniversiteler.append (üniversite)
            toplamKayıtlı += kayıtlı
    return (üniversiteler, kayıtlılar, toplamKayıtlı)


üniversiteler, kayıtlılar, toplamÖğrenci = veridosyasınıİşle ("p_30712bx.txt")
sayı = len (üniversiteler)
print ("İngilteredeki toplam ", sayı, " üniversite ve kayıtlı öğrenci sayıları dökümü:",
    "\n", "-"*70, sep="")
for i in range (sayı):
    print ((i+1), ") ", üniversiteler[i], sep="", end=": ")
    print (kayıtlılar[i])
print ("-"*70, "\nTüm üniversitelerdeki toplam öğrenci sayısı: ", toplamÖğrenci, sep="")

oranlaştırılanKayıtlar = [kayıtlı / toplamÖğrenci for kayıtlı in kayıtlılar]
# Hayali bir gelişigüzel ağırlıklı tercih kaydı yapalım:
print ("\nAğırlıklı tercih yöntemiyle tesadüfi bir üniversite seçimi: ", ağırlıklıTercih (üniversiteler, oranlaştırılanKayıtlar), sep="")

try: toplam = abs (int (input ("\nToplam kaç farazi öğrenciyi tüm üniversitelere ağırlıklı kaydedelim [100 000]? ")))
except: toplam = 100000

orantılıKayıtlar = []
for i in range (toplam): orantılıKayıtlar.append (ağırlıklıTercih (üniversiteler, oranlaştırılanKayıtlar) )
#orantılıKayıtlar.sort() # Üniversite adlarını a->z sıralar...
say = Counter (orantılıKayıtlar)

print ("\nİngilteredeki toplam ", sayı, " üniversiteye ", toplam, " adet öğrenci dağıtımı:", "\n", "-"*66, sep="")
i = 1
for a in say:
    print (i, ") ", a, ": ", say[a], sep="")
    i +=1



"""Çıktı:
>python p_30712b.py
İngilteredeki toplam 20 üniversite ve kayıtlı öğrenci sayıları dökümü:
----------------------------------------------------------------------
1) Open University in England: 123490
2) University of Manchester: 37925
3) University of Nottingham: 33270
4) Sheffield Hallam University: 33100
5) University of Birmingham: 32335
6) Manchester Metropolitan University: 32160
7) University of Leeds: 30975
8) Cardiff University: 30180
9) University of South Wales: 29195
10) University College London: 28430
11) King's College London: 27645
12) University of Edinburgh: 27625
13) Northumbria University: 27565
14) University of Glasgow: 27390
15) University of Plymouth: 27203
16) Coventry University: 27002
17) University of the West of England: 26734
18) University of Central Lancashire: 26265
19) Nottingham Trent University: 26221
20) University of Sheffield: 25908
----------------------------------------------------------------------
Tüm üniversitelerdeki toplam öğrenci sayısı: 680618

Ağırlıklı tercih yöntemiyle tesadüfi bir üniversite seçimi: Nottingham Trent University

Toplam kaç farazi öğrenciyi tüm üniversitelere ağırlıklı kaydedelim [100 000]?

İngilteredeki toplam 20 üniversiteye 100000 adet öğrenci dağıtımı:
------------------------------------------------------------------
1) King's College London: 4111
2) Cardiff University: 4362
3) University of the West of England: 3956
4) University of South Wales: 4295
5) Sheffield Hallam University: 4941
6) University of Sheffield: 3712
7) University of Manchester: 5637
8) University College London: 4261
9) Open University in England: 17981
10) University of Plymouth: 3955
11) Northumbria University: 4045
12) University of Birmingham: 4728
13) University of Central Lancashire: 3810
14) University of Edinburgh: 4018
15) University of Nottingham: 5009
16) University of Glasgow: 3972
17) Manchester Metropolitan University: 4739
18) Coventry University: 3981
19) Nottingham Trent University: 3889
20) University of Leeds: 4598
"""