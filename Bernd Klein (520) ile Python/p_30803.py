# coding:iso-8859-9 Türkçe
# p_30803.py: Ağırlıklı karşılıklı seçilen yegane elemanların biçimli dökümü örneği.

from p_30801 import karşılıklıSeçim as ks, ağırlıklıKarşılıklıSeçim as aks

def bireşimci (veriler, ağırlıkları=None, biçimlemeFonksiyonu=None, tekrarlanabilirSeçimMi=True):
    def tercih (veriler, ağırlıkları):
        if ağırlıkları: return aks (*zip (veriler, ağırlıkları))
        else: return ks (*veriler)

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


ağırlıklıAdlar = [("Hatice", 60), ("Süheyla", 12) , ("Zeliha", 8), ("Nihat", 35), ("Songül", 37), ("Nedim", 29), ("Sevim", 45),
    ("Nur", 7), ("Yücel", 19), ("Serap", 52), ("Sema", 45), ("Fatih", 48), ("Selda", 37), ("Canan", 17), ("Zafer", 25), ("Belkıs", 8),
    ("Hilal", 33), ("Atilla", 42)]

ağırlıklıSoyadlar = [("Yavaş", 15), ("Küçükbay", 7), ("Kaçar", 4), ("Candan", 37), ("Özbay", 43), ("Göktürk", 49),
    ("Eskici", 3), ("Aydan", 19), ("Çiller", 23), ("Akşener", 17), ("Çiçek", 72), ("Öztürk", 95), ("Amanat", 3), ("Hastürk", 71),
    ("Kölük", 12), ("Fırat", 47), ("Havlucu", 34), ("Özen", 51)] # Liste uzunlukları aynı olmak zorunda değil...

adlar, ağırlıkları = zip (*ağırlıklıAdlar)
ağırlıkToplamı = sum (ağırlıkları)
adlarınAğırlıkları = [x / ağırlıkToplamı for x in ağırlıkları]
soyadlar, ağırlıkları = zip (*ağırlıklıSoyadlar)
ağırlıkToplamı = sum (ağırlıkları)
soyadlarınAğırlıkları = [x / ağırlıkToplamı for x in ağırlıkları]
ağırlıkları = (adlarınAğırlıkları, soyadlarınAğırlıkları)

eleman = bireşimci (
    (adlar, soyadlar),
    ağırlıkları = ağırlıkları,
    biçimlemeFonksiyonu=lambda x: " ".join (x),
    tekrarlanabilirSeçimMi=False)
eleman = eleman()

try: sayı = abs (int (input ("Kaç eleman seçilecek [15]? ")))
except: sayı = 15

print ("\nAğırlıklı karşılıklı seçilen yegane ", sayı, " eleman listesi:", "\n", "-"*54, sep="")
for _ in range (sayı): print ((_+1), ": ", next (eleman), sep="")



"""Çıktı:
>python p_30803.py
Kaç eleman seçilecek [15]?

Ağırlıklı karşılıklı seçilen yegane 15 eleman listesi:
------------------------------------------------------
1: Canan Candan
2: Hatice Çiller
3: Hatice Öztürk
4: Hatice Candan
5: Sevim Hastürk
6: Selda Çiçek
7: Nihat Çiçek
8: Süheyla Yavaş
9: Songül Öztürk
10: Hilal Öztürk
11: Zeliha Hastürk
12: Serap Öztürk
13: Hatice Özbay
14: Serap Çiçek
15: Atilla Havlucu

>python p_30803.py  ** TEKRAR **
Kaç eleman seçilecek [15]? 2

Ağırlıklı karşılıklı seçilen yegane 2 eleman listesi:
------------------------------------------------------
1: Hilal Özen
2: Atilla Hastürk
"""