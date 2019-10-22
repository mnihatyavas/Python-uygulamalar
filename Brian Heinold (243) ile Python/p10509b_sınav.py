# coding:iso-8859-9 Türkçe

from random import randint
from math import *

x=randint(-100, 0)
y=randint(1, 100)
z=randint(101, 200)
print ("Değiştokuş: x=", x, ", y=", y, "ve z=", z)
x,y,z=y,z,x
print ("x<->y=", x, ", y<->z=", y, "ve z<->x=", z)
print()
kare_muaf=ideal_kare=0
for i in range (3, 1000):
    bayrak=0
    for j in range (2, i):
        if (i//j)*j==i and trunc (sqrt (j))**2 == j: bayrak=1; break
    if not bayrak: kare_muaf+=1 # ;print (i, "sayısının bölenleri kare-muaf'tır")
    else: ideal_kare+=1 # ;print (i, "sayısının", j, "böleni ideal-kare'dir")
print ("1->1000 arası sayıların", kare_muaf, "adeti kare muaf ve", ideal_kare, "adeti de ideal kare'dir")

küp_muaf=ideal_küp=0
for i in range (3, 1000):
    bayrak=0
    for j in range (2, i):
        if (i//j)*j==i and trunc (pow (j, 1/3))**3 == j: bayrak=1; break
    if not bayrak: küp_muaf+=1 # ;print (i, "sayısının bölenleri küp-muaf'tır")
    else: ideal_küp+=1 # ;print (i, "sayısının", j, "böleni ideal-küp'tür")
print ("1->1000 arası sayıların", küp_muaf, "adeti küp muaf ve", ideal_küp, "adeti de ideal küp'tür")

beşüs_muaf=ideal_beşüs=0
for i in range (3, 1000):
    bayrak=0
    for j in range (2, i):
        if (i//j)*j==i and trunc (pow (j, 1/5))**5 == j: bayrak=1; break
    if not bayrak: beşüs_muaf+=1 # ;print (i, "sayısının bölenleri beşüs-muaf'tır")
    else: ideal_beşüs+=1 # ;print (i, "sayısının", j, "böleni ideal-beşüs'tür")
print ("1->1000 arası sayıların", beşüs_muaf, "adeti beşüs muaf ve", ideal_beşüs, "adeti de ideal beşüs'tür")
print()
büyük1=büyük2=toplam=ortalama=yüz_üstü=sıfır_altı=0
küçük1=küçük2=100
for i in range (10):
    puan = randint (-10, 110)
    if puan < 0: sıfır_altı+=1; puan=0
    if puan > 100: yüz_üstü+=1; puan=100
    toplam+=puan
    if puan > büyük1: büyük1 = puan
    elif puan > büyük2: büyük2 = puan
    if puan < küçük1: küçük1 = puan
    elif puan < küçük2: küçük2 = puan
    if küçük2 < küçük1: küçük2,küçük1=küçük1,küçük2
    if büyük2 > büyük1: büyük2,büyük1=büyük1,büyük2
print ("Öğrencinin toplam 10 notunun sonuçları==>")
print ("Not ortalaması:", round (toplam/10, 2) )
print ("Endüşük 2 notu hariç ortalaması:", round ((toplam-küçük1-küçük2)/8, 2) )
print ("Enbüyük 2 notu:", büyük1, büyük2)
print ("Enküçük 2 notu:", küçük1, küçük2)
print ("Hatalı girilen negatif not sayısı:", sıfır_altı)
print ("Hatalı girilen yüz üstü not sayısı:", yüz_üstü)
print()
sayı = randint (1, 100)
f=1
for i in range (2, sayı+1): f *=i
print (sayı, "faktöriyel:", f)
