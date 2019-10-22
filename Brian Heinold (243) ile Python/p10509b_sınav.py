# coding:iso-8859-9 T�rk�e

from random import randint
from math import *

x=randint(-100, 0)
y=randint(1, 100)
z=randint(101, 200)
print ("De�i�toku�: x=", x, ", y=", y, "ve z=", z)
x,y,z=y,z,x
print ("x<->y=", x, ", y<->z=", y, "ve z<->x=", z)
print()
kare_muaf=ideal_kare=0
for i in range (3, 1000):
    bayrak=0
    for j in range (2, i):
        if (i//j)*j==i and trunc (sqrt (j))**2 == j: bayrak=1; break
    if not bayrak: kare_muaf+=1 # ;print (i, "say�s�n�n b�lenleri kare-muaf't�r")
    else: ideal_kare+=1 # ;print (i, "say�s�n�n", j, "b�leni ideal-kare'dir")
print ("1->1000 aras� say�lar�n", kare_muaf, "adeti kare muaf ve", ideal_kare, "adeti de ideal kare'dir")

k�p_muaf=ideal_k�p=0
for i in range (3, 1000):
    bayrak=0
    for j in range (2, i):
        if (i//j)*j==i and trunc (pow (j, 1/3))**3 == j: bayrak=1; break
    if not bayrak: k�p_muaf+=1 # ;print (i, "say�s�n�n b�lenleri k�p-muaf't�r")
    else: ideal_k�p+=1 # ;print (i, "say�s�n�n", j, "b�leni ideal-k�p't�r")
print ("1->1000 aras� say�lar�n", k�p_muaf, "adeti k�p muaf ve", ideal_k�p, "adeti de ideal k�p't�r")

be��s_muaf=ideal_be��s=0
for i in range (3, 1000):
    bayrak=0
    for j in range (2, i):
        if (i//j)*j==i and trunc (pow (j, 1/5))**5 == j: bayrak=1; break
    if not bayrak: be��s_muaf+=1 # ;print (i, "say�s�n�n b�lenleri be��s-muaf't�r")
    else: ideal_be��s+=1 # ;print (i, "say�s�n�n", j, "b�leni ideal-be��s't�r")
print ("1->1000 aras� say�lar�n", be��s_muaf, "adeti be��s muaf ve", ideal_be��s, "adeti de ideal be��s't�r")
print()
b�y�k1=b�y�k2=toplam=ortalama=y�z_�st�=s�f�r_alt�=0
k���k1=k���k2=100
for i in range (10):
    puan = randint (-10, 110)
    if puan < 0: s�f�r_alt�+=1; puan=0
    if puan > 100: y�z_�st�+=1; puan=100
    toplam+=puan
    if puan > b�y�k1: b�y�k1 = puan
    elif puan > b�y�k2: b�y�k2 = puan
    if puan < k���k1: k���k1 = puan
    elif puan < k���k2: k���k2 = puan
    if k���k2 < k���k1: k���k2,k���k1=k���k1,k���k2
    if b�y�k2 > b�y�k1: b�y�k2,b�y�k1=b�y�k1,b�y�k2
print ("��rencinin toplam 10 notunun sonu�lar�==>")
print ("Not ortalamas�:", round (toplam/10, 2) )
print ("End���k 2 notu hari� ortalamas�:", round ((toplam-k���k1-k���k2)/8, 2) )
print ("Enb�y�k 2 notu:", b�y�k1, b�y�k2)
print ("Enk���k 2 notu:", k���k1, k���k2)
print ("Hatal� girilen negatif not say�s�:", s�f�r_alt�)
print ("Hatal� girilen y�z �st� not say�s�:", y�z_�st�)
print()
say� = randint (1, 100)
f=1
for i in range (2, say�+1): f *=i
print (say�, "fakt�riyel:", f)
