# coding:iso-8859-9 T�rk�e
# p_30710b.py: Jenerat�r �rete�le a��rl�k nisbetinde tesad�fi s�f�r ve bir �retme �rne�i.

import random

def tesad�fiBirS�f�r (a):
    while True:
        x = random.random()
        yield 1 if x < a else 0

def �ret (tesad�fi�rete�, n):
    for i in range (n): yield next (tesad�fi�rete�)

try: kere = abs (int (input ("Ka� adet tesad�fi say� �retsin [1 000 000]? ")))
except: kere = 1000000

try: a��rl�k = abs (eval (input ("[0->1] a��rl��� ka� olsun [0.50]? ")))
except: a��rl�k = 0.5
if a��rl�k > 1: a��rl�k = 0.5

print ("\nSonu�: %", (a��rl�k * 1000) / 10, " a��rl�kl� ", kere, " adet 0/1'in ortalamas�: %", (sum (_ for _ in �ret (tesad�fiBirS�f�r (a��rl�k), kere)) / kere) * 1000 / 10, sep="")



"""��kt�:
>python p_30710b.py
Ka� adet tesad�fi say� �retsin [1 000 000]? 100
[0->1] a��rl��� ka� olsun [0.50]? 0.85

Sonu�: %85.0 a��rl�kl� 100 adet 0/1'in ortalamas�: %87.0

>python p_30710b.py  ** TEKRAR **
Ka� adet tesad�fi say� �retsin [1 000 000]? 10000
[0->1] a��rl��� ka� olsun [0.50]? 0.257

Sonu�: %25.7 a��rl�kl� 10000 adet 0/1'in ortalamas�: %25.779999999999994

>python p_30710b.py  ** TEKRAR **
Ka� adet tesad�fi say� �retsin [1 000 000]?
[0->1] a��rl��� ka� olsun [0.50]?

Sonu�: %50.0 a��rl�kl� 1000000 adet 0/1'in ortalamas�: %50.0561
"""