# coding:iso-8859-9 Türkçe
# p_30712c.py: 4 prensin son 4'ü favori 11 amazon kız adayla günbegün değişen ağırlıkla evlilik ihtimali örneği.

import random
import numpy as np
from time import process_time as pt

def ağırlıklıÖrnekleme2 (listem, ağırlıkları, k):
    seçilenKüme = set()
    listem = list (listem)
    ağırlıkları = list (ağırlıkları)
    while len (seçilenKüme) < k:
        seçilen = ağırlıklıTercih (listem, ağırlıkları)
        if seçilen not in seçilenKüme: seçilenKüme.add (seçilen)
        # Seçilen tekrar seçilmişse kümeye eklenmez...
    return list (seçilenKüme)

def ağırlıklıTercih (zarYüzleri, gelmeAğırlıkları, kriptoluMu=True):
    if kriptoluMu: x = random.SystemRandom().random()
    else: x = np.random.random()
    gelmeYüzdeleriToplamı = [0] + list (np.cumsum (gelmeAğırlıkları))
    endeks = kaçıncıArada (x, gelmeYüzdeleriToplamı)
    return zarYüzleri[endeks]

def kaçıncıArada (değerim, bölümler, uçlar_1Mi=True):
    for i in range (0, len (bölümler)):
        if değerim < bölümler[i]: return i-1 if uçlar_1Mi else i
    return -1 if uçlar_1Mi else len (bölümler)


amazonAdaylar = ["Airla", "Barbara", "Eos", "Glykeria", "Hanna", "Helen",
    "Agathangelos", "Iokaste", "Medousa", "Sofronia", "Andromeda"]
"""3 farklı yöntem işlem süresini gittikce kısaltır...
değişenAğırlıklar = [1 / len (amazonAdaylar) for _ in range (len (amazonAdaylar))] # 11'i de eşit=1/11...

from fractions import Fraction
değişenAğırlıklar = [Fraction (1, 11) for _ in range (len (amazonAdaylar))]
"""
değişenAğırlıklar = np.full (11, 1 / len (amazonAdaylar))
PytheussesFavorileri = {"Iokaste", "Medousa", "Sofronia", "Andromeda"}

try: kere = abs (int (input ("Hergün seçilecek 4'lü çekiliş sayısı [1 000]? ")))
except: kere = 1000

sayaç = 0
ihtimal = 1 / 330 # %03 (binde 3)...
geçenGünler = 0
faktör1 = 1 / 13 # Hergün favori olmayan ilk yediliden düşülecek ağırlık...
faktör2 = 1 / 12 # Hergün favori son dörtlüsüne eklenecek ağırlık...
başlat = pt()

print ("\nBaşlangıç ağırlıklar: %", [int (a * 10000) / 100 for a in değişenAğırlıklar])
while ihtimal < 0.9: # yüzde 90 (hergün 1 döngü)...
    for i in range (kere): # İstenen, 1000 tesadüfi seçimden enaz 900 favori dörtlü kümesi çıkması...
        seçilenDörtlü = ağırlıklıÖrnekleme2 (amazonAdaylar, değişenAğırlıklar, 4)
        if set (seçilenDörtlü) == PytheussesFavorileri: sayaç += 1
    ihtimal = sayaç / kere # ihtimal=900/1000: son...
    sayaç = 0
    değişenAğırlıklar[:7] = [ ağır - ağır*faktör1 for ağır in değişenAğırlıklar[:7] ]
    değişenAğırlıklar[7:] = [ ihtimal + ihtimal*faktör2 for ihtimal in değişenAğırlıklar[7:] ]
    değişenAğırlıklar = [ a / sum (değişenAğırlıklar) for a in değişenAğırlıklar]
    geçenGünler += 1

print ("Sonuç ağırlıklar: %", [int (a * 10000) / 100 for a in değişenAğırlıklar])
print ("İşlem süresi (sn):", int ((pt() - başlat) * 100) / 100)
print ("Pytheusses'un %90 emin olabilmesi için geçen gün sayısı: ", geçenGünler)



"""Çıktı:
>python p_30712c.py
Hergün seçilecek 4'lü çekiliş sayısı [1 000]? 1

Başlangıç ağırlıklar: % [9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09]
Sonuç ağırlıklar: % [3.72, 3.72, 3.72, 3.72, 3.72, 3.72, 3.72, 18.47, 18.47, 18.47, 18.47]
İşlem süresi (sn): 0.04
Pytheusses'un %90 emin olabilmesi için geçen gün sayısı:  10

>python p_30712c.py  ** TEKRAR **
Hergün seçilecek 4'lü çekiliş sayısı [1 000]? 10

Başlangıç ağırlıklar: % [9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09]
Sonuç ağırlıklar: % [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 23.94, 23.94, 23.94, 23.94]
İşlem süresi (sn): 0.98
Pytheusses'un %90 emin olabilmesi için geçen gün sayısı:  23

>python p_30712c.py  ** TEKRAR **
Hergün seçilecek 4'lü çekiliş sayısı [1 000]? 100

Başlangıç ağırlıklar: % [9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09]
Sonuç ağırlıklar: % [0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 24.74, 24.74, 24.74, 24.74]
İşlem süresi (sn): 6.13
Pytheusses'un %90 emin olabilmesi için geçen gün sayısı:  32

>python p_30712c.py  ** TEKRAR **
Hergün seçilecek 4'lü çekiliş sayısı [1 000]?

Başlangıç ağırlıklar: % [9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09, 9.09]
Sonuç ağırlıklar: % [0.17, 0.17, 0.17, 0.17, 0.17, 0.17, 0.17, 24.69, 24.69, 24.69, 24.69]
İşlem süresi (sn): 44.19
Pytheusses'un %90 emin olabilmesi için geçen gün sayısı:  31
"""