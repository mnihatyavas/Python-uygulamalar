# coding:iso-8859-9 T�rk�e
# p_30707a.py: Farkl� a��rl�kl� zamir, s�fat, isim, t�mle� ve fiillerden tesad�fi c�mleler kurma �rne�i.

import random
import numpy as np

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

try: adet = abs (int (input ("Ka� sa�masapan c�mle kuracaks�n [10]? ")))
except: adet = 10

for i in range (adet):
    c�mle = a��rl�kl�KartezyenSe�im (zamir, s�fat, isim, t�mle�, fiil)
    print ((i+1), ". ", " ".join (c�mle) + ".", sep="")

"""��kt�:
>python p_30707.py
Ka� sa�masapan c�mle kuracaks�n [10]?
1. Bir gri ���k mutluluk tad�yor.
2. �u sar� su mutluluk d���n�yor.
3. Bu gri fil mutluluk al�yor.
4. Herbir ye�il bal�k hava tad�yor.
5. Bir sar� fil mutluluk al�yor.
6. �u ye�il su hava d���n�yor.
7. Herbir gri bal�k �ikolata al�yor.
8. Bu ye�il bal�k zeka al�yor.
9. Herbir k�rm�z� fil �ikolata tad�yor.
10. Bir sar� fil hava d���n�yor.

>python p_30707.py  ** TEKRAR **
Ka� sa�masapan c�mle kuracaks�n [10]? 3
1. �u ye�il ���k �ikolata tad�yor.
2. Bir mavi su mutluluk kokuyor.
3. T�m mavi ���k mutluluk tad�yor.
"""