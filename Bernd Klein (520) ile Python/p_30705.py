# coding:iso-8859-9 Türkçe
# p_30705.py: 9 farklı renk ve ağırlıklı misketlerin tekli ve üçlü seçim sonuçlarını ağırlıklarıyla kıyaslama örneği.

import random
import numpy as np
from numpy.random import choice
from collections import Counter

def kaçıncıArada (değerim, bölümler, uçlar_1Mi=True):
    for i in range (0, len (bölümler)):
        if değerim < bölümler[i]: return i-1 if uçlar_1Mi else i
    return -1 if uçlar_1Mi else len (bölümler)

def ağırlıklıTercih (zarYüzleri, gelmeAğırlıkları, kriptoluMu=True):
    if kriptoluMu: x = random.SystemRandom().random()
    else: x = np.random.random()
    gelmeYüzdeleriToplamı = [0] + list (np.cumsum (gelmeAğırlıkları))
    endeks = kaçıncıArada (x, gelmeYüzdeleriToplamı)
    return zarYüzleri[endeks]

def ağırlıklıÖrnekleme (listem, ağırlıkları, k):
    # ağırlıklıTercih ağırlıkları ihtimalinde listem'den her kerede k yegane adetlik küme seçimi yapar...
    seçilenKüme = set()
    listem = list (listem)
    ağırlıkları = list (ağırlıkları) 
    while len (seçilenKüme) < k:
        seçilen = ağırlıklıTercih (listem, ağırlıkları)
        seçilenKüme.add (seçilen)
        endeks = listem.index (seçilen)
        ağırlıkları.pop (endeks) # Seçilenin ağırlığı düşülür...
        listem.remove (seçilen) # Seçilen listeden silinir...
        ağırlıkları = [ x / sum (ağırlıkları) for x in ağırlıkları] # Düşenden dolayı yeniden ağırlıklandırılır...
        # Kümedeki her seçilen tekrar seçilemez...
    return list (seçilenKüme)

def ağırlıklıÖrnekleme2 (listem, ağırlıkları, k): # Alternatif örnekleme...
    seçilenKüme = set()
    listem = list (listem)
    ağırlıkları = list (ağırlıkları)
    while len (seçilenKüme) < k:
        seçilen = ağırlıklıTercih (listem, ağırlıkları)
        if seçilen not in seçilenKüme: seçilenKüme.add (seçilen)
        # Seçilen tekrar seçilmişse kümeye eklenmez...
    return list (seçilenKüme)


misketler = ["kırmızı", "yeşil", "mavi", "sarı", "siyah", "beyaz", "pembe", "turuncu", "kahve"]
ağırlıkları = [1/24, 4/24, 4/24, 2/24, 2/24, 1/24, 3/24, 6/24, 1/24]
# k=1 tekli tercihler için: 1/24=%4.17, 6/24=%25...

m = 3
print ("10 adet ", m, "'erli ağırlıklandırılmış seçilen küme dökümü:", sep="")
for i in range(10): print (ağırlıklıÖrnekleme (misketler, ağırlıkları, m))

print ("\nRenkli misketler ve % seçilebilme ağırlıkları listesi:")
for i in range (len (misketler)): print (misketler [i], ": %", int (ağırlıkları [i] * 1000) / 10.0, sep="", end=", ")

n = 10000
sayaç = 0
sayaç2 = 0
for i in range (n):
    if "turuncu" in ağırlıklıÖrnekleme (misketler, ağırlıkları, 1): sayaç += 1
    if "turuncu" in ağırlıklıÖrnekleme2 (misketler, ağırlıkları, 1): sayaç2 += 1 
print ("\n\n", n, " kerede 2 farklı metodla 1'li turuncu misket seçim yüzdeleri: ", (100 * sayaç / n), ", ", (100 * sayaç2 / n), sep="")

n = 10000
sayaç = 0
sayaç2 = 0
for i in range (n):
    if "turuncu" in ağırlıklıÖrnekleme (misketler, ağırlıkları, 3): sayaç += 1
    if "turuncu" in ağırlıklıÖrnekleme2 (misketler, ağırlıkları, 3): sayaç2 += 1 
print (n, " kerede 2 farklı metodla 3'lü turuncu misket seçim yüzdeleri: ", (100 * sayaç / n), ", ", (100 * sayaç2 / n), sep="")


"""Çıktı:
>python p_30705.py
10 adet 3'erli ağırlıklandırılmış seçilen küme dökümü:
['pembe', 'yeşil', 'mavi']
['turuncu', 'sarı', 'siyah']
['yeşil', 'mavi', 'siyah']
['pembe', 'yeşil', 'mavi']
['turuncu', 'kırmızı', 'siyah']
['turuncu', 'pembe', 'kahve']
['turuncu', 'pembe', 'mavi']
['turuncu', 'pembe', 'beyaz']
['turuncu', 'pembe', 'mavi']
['turuncu', 'pembe', 'yeşil']

Renkli misketler ve % seçilebilme ağırlıkları listesi:
kırmızı: %4.1, yeşil: %16.6, mavi: %16.6, sarı: %8.3, siyah: %8.3, beyaz: %4.1,pembe: %12.5, turuncu: %25.0, kahve: %4.1,

10000 kerede 2 farklı metodla 1'li turuncu misket seçim yüzdeleri: 24.99, 24.24
10000 kerede 2 farklı metodla 3'lü turuncu misket seçim yüzdeleri: 63.23, 64.47
"""