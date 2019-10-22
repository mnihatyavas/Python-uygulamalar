# coding:iso-8859-9 T�rk�e
# p_30707b.py: Farkl� a��rl�kl� �oklu c�mleleden t�mle�lerin verili ve uygulamal� a��rl�klar� k�yas� �rne�i.

import random
import numpy as np
from collections import Counter

def ka��nc�Arada (de�erim, b�l�mler, u�lar_1Mi=True):
    for i in range (0, len (b�l�mler)):
        if de�erim < b�l�mler[i]: return i-1 if u�lar_1Mi else i
    return -1 if u�lar_1Mi else len (b�l�mler)

def a��rl�kl�Tercih (ibareler, gelmeA��rl�klar�, kriptoluMu=True):
    if kriptoluMu: x = random.SystemRandom().random()
    else: x = np.random.random()
    gelmeY�zdeleriToplam� = [0] + list (np.cumsum (gelmeA��rl�klar�))
    endeks = ka��nc�Arada (x, gelmeY�zdeleriToplam�)
    return ibareler[endeks]

def a��rl�kl�KartezyenSe�im (*taranabilenler):
    sonu� = []
    for kelime, a��rl��� in taranabilenler:
        a��rl�kl�Se�im = a��rl�kl�Tercih (kelime, a��rl���)
        sonu�.append (a��rl�kl�Se�im)
    return sonu�

zamir = (["Bu", "Bir", "Herbir", "Her", "�u", "T�m"], [0.3, 0.2, 0.1, 0.1, 0.2, 0.1])
s�fat = (["k�rm�z�", "ye�il", "mavi", "sar�", "gri", "beyaz"], [0.1, 0.3, 0.2, 0.2, 0.2, 0.1])
isim = (["su", "fil", "bal�k", "���k", "programlama dili"], [0.3, 0.2, 0.1, 0.1, 0.3])
t�mle� = (["mutluluk", "�ikolata", "zeka", "hava"], [0.5, 0.2, 0.2, 0.1])
fiil = (["kokuyor", "tad�yor", "d���n�yor", "al�yor"], [0.2, 0.3, 0.3, 0.2])

try: adet = abs (int (input ("Ka� sa�masapan c�mle kuracaks�n [1000]? ")))
except: adet = 1000

c�mleler = []
for i in range (adet):
    c�mle = a��rl�kl�KartezyenSe�im (zamir, s�fat, isim, t�mle�, fiil)
    c�mleler.append (" ".join (c�mle) + ".")

kelimeler = ["mutluluk", "�ikolata", "zeka", "hava"]

say = Counter()
for t�mce in c�mleler:
    for kelime in kelimeler:
        if kelime in t�mce: say[kelime] += 1

kelimeToplam� = sum (say.values())
print ("\nTan�mlanan kelime ve a��rl�klar�:\n", t�mle�, sep="")
print ("\nUygulamada saptanan kelime ve a��rl�klar�:")
for anahtar in say: print (anahtar, say [anahtar] / kelimeToplam�)



"""��kt�:
>python p_30707b.py
Ka� sa�masapan c�mle kuracaks�n [1000]?

Tan�mlanan kelime ve a��rl�klar�:
(['mutluluk', '�ikolata', 'zeka', 'hava'], [0.5, 0.2, 0.2, 0.1])

Uygulamada saptanan kelime ve a��rl�klar�:
zeka 0.185
mutluluk 0.533
�ikolata 0.192
hava 0.09

>python p_30707b.py  ** TEKRAR **
Ka� sa�masapan c�mle kuracaks�n [1000]? 10000

Tan�mlanan kelime ve a��rl�klar�:
(['mutluluk', '�ikolata', 'zeka', 'hava'], [0.5, 0.2, 0.2, 0.1])

Uygulamada saptanan kelime ve a��rl�klar�:
mutluluk 0.5025
hava 0.0997
�ikolata 0.1957
zeka 0.2021
"""