# coding:iso-8859-9 Türkçe
# p_30801.py: Ad ve soyad listelerinden karşılıklı ağırlıksız seçimi örneği.

import random
import numpy as np
from random import choice

def ağırlıklıÖrnekleme2 (listem, ağırlıkları, k):
    seçilenKüme = set()
    listem = list (listem)
    ağırlıkları = list (ağırlıkları)
    while len (seçilenKüme) < k:
        seçilen = ağırlıklıTercih (listem, ağırlıkları)
        if seçilen not in seçilenKüme: seçilenKüme.add (seçilen)
        # Seçilen tekrar seçilmişse kümeye eklenmez...
    return list (seçilenKüme)

def ağırlıklıTercih (veriler, gelmeAğırlıkları, kriptoluMu=True):
    if kriptoluMu: x = random.SystemRandom().random()
    else: x = np.random.random()
    gelmeYüzdeleriToplamı = [0] + list (np.cumsum (gelmeAğırlıkları))
    endeks = kaçıncıArada (x, gelmeYüzdeleriToplamı)
    return veriler[endeks]

def kaçıncıArada (değerim, bölümler, uçlar_1Mi=True):
    for i in range (0, len (bölümler)):
        if değerim < bölümler[i]: return i-1 if uçlar_1Mi else i
    return -1 if uçlar_1Mi else len (bölümler)

def karşılıklıSeçim (*taranabilenler):
    sonuç = []
    for listem in taranabilenler: sonuç.append (choice (listem))
    return sonuç

def ağırlıklıKarşılıklıSeçim (*taranabilenler):
    sonuç = []
    for veri, ağırlığı in taranabilenler:
        ağırlıklıSeçim = ağırlıklıTercih (veri, ağırlığı)
        sonuç.append (ağırlıklıSeçim)
    return sonuç

def bireşimci (veriler, ağırlıkları=None, biçimlemeFonksiyonu=None, tekrarlanabilirSeçimMi=True):
    def tercih (veriler, ağırlıkları):
        if ağırlıkları: return ağırlıklıKarşılıklıSeçim (*zip (veriler, ağırlıkları))
        else: return karşılıklıSeçim (*veriler)
    def bireşimle():
        if not tekrarlanabilirSeçimMi: belle = set()
        while True:
            yeniSeçilen = tercih (veriler, ağırlıkları)
            if not tekrarlanabilirSeçimMi:
                seçilen = str (yeniSeçilen)
                while seçilen in belle:
                    yeniSeçilen = tercih (veriler, ağırlıkları)
                    seçilen = str (yeniSeçilen)
                belle.add (seçilen)
            if biçimlemeFonksiyonu: yield biçimlemeFonksiyonu (yeniSeçilen)
            else: yield yeniSeçilen
    return bireşimle


if __name__ == "__main__":
    adlar = ["Hatice", "Süheyla", "Zeliha", "Nihat", "Songül", "Nedim", "Sevim",
        "Nur", "Yücel", "Serap", "Sema", "Fatih", "Selda", "Canan", "Zafer", "Belkıs",
        "Hilal", "Atilla"]
    soyadlar = ["Yavaş", "Küçükbay", "Kaçar", "Candan", "Özbay", "Göktürk",
        "Eskici", "Aydan", "Çiller", "Akşener", "Çiçek", "Öztürk", "Amanat", "Hastürk",
        "Kölük", "Fırat", "Havlucu", "Özen"] # Liste uzunlukları aynı olmak zorunda değil...

    try: sayı = abs (int (input ("Kaç eleman seçilecek [15]? ")))
    except: sayı = 15

    elemanlar = set()
    while len (elemanlar) < sayı:
        eleman = karşılıklıSeçim (adlar, soyadlar)
        elemanlar.add (" ".join (eleman))
    print (elemanlar)



"""Çıktı:
>python p_30801.py
Kaç eleman seçilecek [15]?
{'Hilal Havlucu', 'Belkıs Çiçek', 'Nedim Kölük', 'Zafer Akşener', 'Hilal Hastürk',
'Süheyla Çiller', 'Atilla Candan', 'Atilla Öztürk', 'Zeliha Özen', 'Selda Aydan',
'Belkıs Hastürk', 'Zeliha Küçükbay', 'Selda Havlucu', 'Sema Çiçek', 'CananEskici'}

>python p_30801.py  ** TEKRAR **
Kaç eleman seçilecek [15]? 20
{'Hilal Küçükbay', 'Canan Hastürk', 'Nedim Eskici', 'Nihat Özen', 'Hilal Göktürk',
'Selda Çiçek', 'Songül Hastürk', 'Songül Kaçar', 'Sevim Küçükbay', 'Nedim Özen',
'Sema Akşener', 'Zeliha Özbay', 'Fatih Aydan', 'Zeliha Öztürk', 'Süheyla Çiller',
'Zeliha Özen', 'Nedim Kölük', 'Canan Fırat', 'Sema Özbay', 'Belkıs Eskici'}
"""