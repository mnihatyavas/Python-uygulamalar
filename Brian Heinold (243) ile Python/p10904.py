# coding:iso-8859-9 T�rk�e

from random import randint

print ("Sade Ent harici bir tu�u Ent'larsan�z ��kars�n�z...")
while not input():
    say� = randint (3, 10000)
    i = 2
    while i < say� and say� % i != 0: i+=1
    if i==say�: print (say�, "bir ASAL say�d�r!")
    else: print (say�, "bir asal say� DE��LD�R!")

print ("\nSadece Ent harici bir HARF� Ent'larsan�z ��kars�n�z...")
while not input().isalpha():
    say� = randint (3, 10000)
    for i in range (2,say�):
        if say� % i == 0:
            print (say�, "bir asal say� DE��LD�R!")
            break
    else: print (say�, "bir ASAL say�d�r!")
