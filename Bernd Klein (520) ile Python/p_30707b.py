# coding:iso-8859-9 Türkçe
# p_30707b.py: Farklı ağırlıklı çoklu cümleleden tümleçlerin verili ve uygulamalı ağırlıkları kıyası örneği.

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

def ağırlıklıKartezyenSeçim (*taranabilenler):
    sonuç = []
    for kelime, ağırlığı in taranabilenler:
        ağırlıklıSeçim = ağırlıklıTercih (kelime, ağırlığı)
        sonuç.append (ağırlıklıSeçim)
    return sonuç

zamir = (["Bu", "Bir", "Herbir", "Her", "Şu", "Tüm"], [0.3, 0.2, 0.1, 0.1, 0.2, 0.1])
sıfat = (["kırmızı", "yeşil", "mavi", "sarı", "gri", "beyaz"], [0.1, 0.3, 0.2, 0.2, 0.2, 0.1])
isim = (["su", "fil", "balık", "ışık", "programlama dili"], [0.3, 0.2, 0.1, 0.1, 0.3])
tümleç = (["mutluluk", "çikolata", "zeka", "hava"], [0.5, 0.2, 0.2, 0.1])
fiil = (["kokuyor", "tadıyor", "düşünüyor", "alıyor"], [0.2, 0.3, 0.3, 0.2])

try: adet = abs (int (input ("Kaç saçmasapan cümle kuracaksın [1000]? ")))
except: adet = 1000

cümleler = []
for i in range (adet):
    cümle = ağırlıklıKartezyenSeçim (zamir, sıfat, isim, tümleç, fiil)
    cümleler.append (" ".join (cümle) + ".")

kelimeler = ["mutluluk", "çikolata", "zeka", "hava"]

say = Counter()
for tümce in cümleler:
    for kelime in kelimeler:
        if kelime in tümce: say[kelime] += 1

kelimeToplamı = sum (say.values())
print ("\nTanımlanan kelime ve ağırlıkları:\n", tümleç, sep="")
print ("\nUygulamada saptanan kelime ve ağırlıkları:")
for anahtar in say: print (anahtar, say [anahtar] / kelimeToplamı)



"""Çıktı:
>python p_30707b.py
Kaç saçmasapan cümle kuracaksın [1000]?

Tanımlanan kelime ve ağırlıkları:
(['mutluluk', 'çikolata', 'zeka', 'hava'], [0.5, 0.2, 0.2, 0.1])

Uygulamada saptanan kelime ve ağırlıkları:
zeka 0.185
mutluluk 0.533
çikolata 0.192
hava 0.09

>python p_30707b.py  ** TEKRAR **
Kaç saçmasapan cümle kuracaksın [1000]? 10000

Tanımlanan kelime ve ağırlıkları:
(['mutluluk', 'çikolata', 'zeka', 'hava'], [0.5, 0.2, 0.2, 0.1])

Uygulamada saptanan kelime ve ağırlıkları:
mutluluk 0.5025
hava 0.0997
çikolata 0.1957
zeka 0.2021
"""