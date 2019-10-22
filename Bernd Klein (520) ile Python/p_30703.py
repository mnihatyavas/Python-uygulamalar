# coding:iso-8859-9 Türkçe
# p_30703.py: Hileli ağırlıklı zarlarla 10Bin atışta [1,6] gelme yüzdeleri örneği.

import numpy as np
import random
from collections import Counter as Sayaç

def kaçıncıArada (x, mesafe):
    for i in range (0, len (mesafe)):
        if x < mesafe[i]: return i-1
    return -1

def ağırlıklıTercih (zarYüzleri, gelmeAğırlıkları, kriptoluMu=True):
    if kriptoluMu: x = random.SystemRandom().random()
    else: x = np.random.random()
    gelmeYüzdeleriToplamı = [0] + list (np.cumsum (gelmeAğırlıkları))
    endeks = kaçıncıArada (x, gelmeYüzdeleriToplamı)
    return zarYüzleri [endeks]


zarınYüzleri = [1, 2, 3, 4, 5, 6]
gelmeAğırlıkları = [1/12, 1/12, 1/12, 1/12, 2/12, 6/12] # Hileli olasılıklar toplamı: p+=12/12...
sonuçlar = []

try: kere = abs (int (input ("Zar kaç kez atılsın? [Varsayılı=10 000]: ")))
except: kere = 10000

for _ in range (kere): sonuçlar.append (ağırlıklıTercih (zarınYüzleri, gelmeAğırlıkları)) # Varsayılı kriptolu...
zarGelenleri = Sayaç (sonuçlar)
for anahtar in zarGelenleri: zarGelenleri [anahtar] = zarGelenleri [anahtar] / kere # 1'e normalleştirilen gelen zar yüzdeleri...

liste = sorted (list (zarGelenleri.values()) )
print ("\nGelme yüzdeleri: ", liste,
    "\nNormalleştirilmiş yüzdeler toplamı = 1 mi? ", (sum (liste) > 0.999), sep="")

print ("\nBiçimli çıktılar:\n", "-"*62, sep="")
for i in range (len (zarınYüzleri)):
    print ("Zar: {:}, Normalleştirilen sonucu: {:6.4f}, Yüzde sonucu: %{:6.2f}" .format ((i+1), liste[i], (liste[i] * 100)) )
print ("-"*62, "\n{:30s}Yüzde sonuçları toplamı: %{:5.2f}" .format (" ", (sum (liste) * 100)) )



"""Çıktı:
>python p_30703.py
Zar kaç kez atılsın? [Varsayılı=10 000]: 

Gelme yüzdeleri: [0.0786, 0.0833, 0.0842, 0.0886, 0.1664, 0.4989]
Normalleştirilmiş yüzdeler toplamı = 1 mi? True

Biçimli çıktılar:
--------------------------------------------------------------
Zar: 1, Normalleştirilen sonucu: 0.0786, Yüzde sonucu: %  7.86
Zar: 2, Normalleştirilen sonucu: 0.0833, Yüzde sonucu: %  8.33
Zar: 3, Normalleştirilen sonucu: 0.0842, Yüzde sonucu: %  8.42
Zar: 4, Normalleştirilen sonucu: 0.0886, Yüzde sonucu: %  8.86
Zar: 5, Normalleştirilen sonucu: 0.1664, Yüzde sonucu: % 16.64
Zar: 6, Normalleştirilen sonucu: 0.4989, Yüzde sonucu: % 49.89
--------------------------------------------------------------
                              Yüzde sonuçları toplamı: %100.00

>python p_30703.py  ** TEKRAR **
Zar kaç kez atılsın? [Varsayılı=10 000]: 1957

Gelme yüzdeleri: [0.07511497189575882, 0.07613694430250383, 0.0807358201328564, 0.08277976494634645, 0.17015840572304547, 0.515074092999489]
Normalleştirilmiş yüzdeler toplamı = 1 mi? True

Biçimli çıktılar:
--------------------------------------------------------------
Zar: 1, Normalleştirilen sonucu: 0.0751, Yüzde sonucu: %  7.51
Zar: 2, Normalleştirilen sonucu: 0.0761, Yüzde sonucu: %  7.61
Zar: 3, Normalleştirilen sonucu: 0.0807, Yüzde sonucu: %  8.07
Zar: 4, Normalleştirilen sonucu: 0.0828, Yüzde sonucu: %  8.28
Zar: 5, Normalleştirilen sonucu: 0.1702, Yüzde sonucu: % 17.02
Zar: 6, Normalleştirilen sonucu: 0.5151, Yüzde sonucu: % 51.51
--------------------------------------------------------------
                              Yüzde sonuçları toplamı: %100.00
"""