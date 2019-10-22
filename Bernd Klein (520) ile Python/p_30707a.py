# coding:iso-8859-9 Türkçe
# p_30707a.py: Farklı ağırlıklı zamir, sıfat, isim, tümleç ve fiillerden tesadüfi cümleler kurma örneği.

import random
import numpy as np

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

try: adet = abs (int (input ("Kaç saçmasapan cümle kuracaksın [10]? ")))
except: adet = 10

for i in range (adet):
    cümle = ağırlıklıKartezyenSeçim (zamir, sıfat, isim, tümleç, fiil)
    print ((i+1), ". ", " ".join (cümle) + ".", sep="")

"""Çıktı:
>python p_30707.py
Kaç saçmasapan cümle kuracaksın [10]?
1. Bir gri ışık mutluluk tadıyor.
2. Şu sarı su mutluluk düşünüyor.
3. Bu gri fil mutluluk alıyor.
4. Herbir yeşil balık hava tadıyor.
5. Bir sarı fil mutluluk alıyor.
6. Şu yeşil su hava düşünüyor.
7. Herbir gri balık çikolata alıyor.
8. Bu yeşil balık zeka alıyor.
9. Herbir kırmızı fil çikolata tadıyor.
10. Bir sarı fil hava düşünüyor.

>python p_30707.py  ** TEKRAR **
Kaç saçmasapan cümle kuracaksın [10]? 3
1. Şu yeşil ışık çikolata tadıyor.
2. Bir mavi su mutluluk kokuyor.
3. Tüm mavi ışık mutluluk tadıyor.
"""