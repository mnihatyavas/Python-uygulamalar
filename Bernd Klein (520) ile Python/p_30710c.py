# coding:iso-8859-9 T�rk�e
# p_30710c.py: Jenerat�r �rete�le tesad�filerin a��rl���n� y�zde ellileme �rne�i.

import random

def tesad�fiBirS�f�r (a):
    while True:
        x = random.random()
        yield 1 if x < a else 0

def �ret (tesad�fi�rete�, n):
    for i in range (n): yield next (tesad�fi�rete�)

def y�zdeEllici (birS�f�rlar):
    while True:
        bit1 = next (birS�f�rlar)
        bit2 = next (birS�f�rlar)
        if bit1 + bit2 == 1:
            bit3 = next (birS�f�rlar)
            yield 1 if bit2 + bit3 == 1 else 0
        
def y�zdeEllici2 (birS�f�rlar):
    bit1 = next (birS�f�rlar)
    bit2 = next (birS�f�rlar)
    bit3 = next (birS�f�rlar)
    while True:
        if bit1 + bit2 == 1: yield 1 if bit2 + bit3 == 1 else 0
        bit1, bit2, bit3 = bit2, bit3, next (birS�f�rlar)


try: kere = abs (int (input ("Ka� adet tesad�fi say� �retsin [100 000]? ")))
except: kere = 100000

try: a��rl�k = abs (eval (input ("[0->1] a��rl��� ka� olsun [0.85]? ")))
except: a��rl�k = 0.85
if a��rl�k > 1: a��rl�k = 0.85

print ("\nSonu�-1: orijinal %", (a��rl�k * 1000) / 10, " a��rl�kl� ", kere, " adet 0/1'in ortalamas�: %", int ((sum (x for x in �ret (y�zdeEllici (tesad�fiBirS�f�r (a��rl�k)), kere)) / kere) * 10000000) / 100000.0, sep="")
print ("Sonu�-2: orijinal %", (a��rl�k * 1000) / 10, " a��rl�kl� ", kere, " adet 0/1'in ortalamas�: %", int ((sum (x for x in �ret (y�zdeEllici (tesad�fiBirS�f�r (a��rl�k)), kere)) / kere) * 10000000) / 100000.0, sep="")



"""��kt�:
>python p_30710c.py
Ka� adet tesad�fi say� �retsin [100 000]?
[0->1] a��rl��� ka� olsun [0.85]?

Sonu�-1: orijinal %85.0 a��rl�kl� 100000 adet 0/1'in ortalamas�: %49.869
Sonu�-2: orijinal %85.0 a��rl�kl� 100000 adet 0/1'in ortalamas�: %50.043

>python p_30710c.py  ** TEKRAR **
Ka� adet tesad�fi say� �retsin [100 000]? 10000
[0->1] a��rl��� ka� olsun [0.85]? 0.25

Sonu�-1: orijinal %25.0 a��rl�kl� 10000 adet 0/1'in ortalamas�: %49.08399
Sonu�-2: orijinal %25.0 a��rl�kl� 10000 adet 0/1'in ortalamas�: %50.0
"""