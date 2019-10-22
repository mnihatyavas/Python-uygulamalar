# coding:iso-8859-9 T�rk�e
# p_30705.py: 9 farkl� renk ve a��rl�kl� misketlerin tekli ve ��l� se�im sonu�lar�n� a��rl�klar�yla k�yaslama �rne�i.

import random
import numpy as np
from numpy.random import choice
from collections import Counter

def ka��nc�Arada (de�erim, b�l�mler, u�lar_1Mi=True):
    for i in range (0, len (b�l�mler)):
        if de�erim < b�l�mler[i]: return i-1 if u�lar_1Mi else i
    return -1 if u�lar_1Mi else len (b�l�mler)

def a��rl�kl�Tercih (zarY�zleri, gelmeA��rl�klar�, kriptoluMu=True):
    if kriptoluMu: x = random.SystemRandom().random()
    else: x = np.random.random()
    gelmeY�zdeleriToplam� = [0] + list (np.cumsum (gelmeA��rl�klar�))
    endeks = ka��nc�Arada (x, gelmeY�zdeleriToplam�)
    return zarY�zleri[endeks]

def a��rl�kl��rnekleme (listem, a��rl�klar�, k):
    # a��rl�kl�Tercih a��rl�klar� ihtimalinde listem'den her kerede k yegane adetlik k�me se�imi yapar...
    se�ilenK�me = set()
    listem = list (listem)
    a��rl�klar� = list (a��rl�klar�) 
    while len (se�ilenK�me) < k:
        se�ilen = a��rl�kl�Tercih (listem, a��rl�klar�)
        se�ilenK�me.add (se�ilen)
        endeks = listem.index (se�ilen)
        a��rl�klar�.pop (endeks) # Se�ilenin a��rl��� d���l�r...
        listem.remove (se�ilen) # Se�ilen listeden silinir...
        a��rl�klar� = [ x / sum (a��rl�klar�) for x in a��rl�klar�] # D��enden dolay� yeniden a��rl�kland�r�l�r...
        # K�medeki her se�ilen tekrar se�ilemez...
    return list (se�ilenK�me)

def a��rl�kl��rnekleme2 (listem, a��rl�klar�, k): # Alternatif �rnekleme...
    se�ilenK�me = set()
    listem = list (listem)
    a��rl�klar� = list (a��rl�klar�)
    while len (se�ilenK�me) < k:
        se�ilen = a��rl�kl�Tercih (listem, a��rl�klar�)
        if se�ilen not in se�ilenK�me: se�ilenK�me.add (se�ilen)
        # Se�ilen tekrar se�ilmi�se k�meye eklenmez...
    return list (se�ilenK�me)


misketler = ["k�rm�z�", "ye�il", "mavi", "sar�", "siyah", "beyaz", "pembe", "turuncu", "kahve"]
a��rl�klar� = [1/24, 4/24, 4/24, 2/24, 2/24, 1/24, 3/24, 6/24, 1/24]
# k=1 tekli tercihler i�in: 1/24=%4.17, 6/24=%25...

m = 3
print ("10 adet ", m, "'erli a��rl�kland�r�lm�� se�ilen k�me d�k�m�:", sep="")
for i in range(10): print (a��rl�kl��rnekleme (misketler, a��rl�klar�, m))

print ("\nRenkli misketler ve % se�ilebilme a��rl�klar� listesi:")
for i in range (len (misketler)): print (misketler [i], ": %", int (a��rl�klar� [i] * 1000) / 10.0, sep="", end=", ")

n = 10000
saya� = 0
saya�2 = 0
for i in range (n):
    if "turuncu" in a��rl�kl��rnekleme (misketler, a��rl�klar�, 1): saya� += 1
    if "turuncu" in a��rl�kl��rnekleme2 (misketler, a��rl�klar�, 1): saya�2 += 1 
print ("\n\n", n, " kerede 2 farkl� metodla 1'li turuncu misket se�im y�zdeleri: ", (100 * saya� / n), ", ", (100 * saya�2 / n), sep="")

n = 10000
saya� = 0
saya�2 = 0
for i in range (n):
    if "turuncu" in a��rl�kl��rnekleme (misketler, a��rl�klar�, 3): saya� += 1
    if "turuncu" in a��rl�kl��rnekleme2 (misketler, a��rl�klar�, 3): saya�2 += 1 
print (n, " kerede 2 farkl� metodla 3'l� turuncu misket se�im y�zdeleri: ", (100 * saya� / n), ", ", (100 * saya�2 / n), sep="")


"""��kt�:
>python p_30705.py
10 adet 3'erli a��rl�kland�r�lm�� se�ilen k�me d�k�m�:
['pembe', 'ye�il', 'mavi']
['turuncu', 'sar�', 'siyah']
['ye�il', 'mavi', 'siyah']
['pembe', 'ye�il', 'mavi']
['turuncu', 'k�rm�z�', 'siyah']
['turuncu', 'pembe', 'kahve']
['turuncu', 'pembe', 'mavi']
['turuncu', 'pembe', 'beyaz']
['turuncu', 'pembe', 'mavi']
['turuncu', 'pembe', 'ye�il']

Renkli misketler ve % se�ilebilme a��rl�klar� listesi:
k�rm�z�: %4.1, ye�il: %16.6, mavi: %16.6, sar�: %8.3, siyah: %8.3, beyaz: %4.1,pembe: %12.5, turuncu: %25.0, kahve: %4.1,

10000 kerede 2 farkl� metodla 1'li turuncu misket se�im y�zdeleri: 24.99, 24.24
10000 kerede 2 farkl� metodla 3'l� turuncu misket se�im y�zdeleri: 63.23, 64.47
"""