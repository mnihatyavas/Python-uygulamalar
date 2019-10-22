# coding:iso-8859-9 Türkçe
# p_30802.py: Ad ve soyadların karşılıklı ağırlıksız yegane biçimli seçim dökümü örneği.

import p_30801 as p381

adlar = ["Hatice", "Süheyla", "Zeliha", "Nihat", "Songül", "Nedim", "Sevim",
    "Nur", "Yücel", "Serap", "Sema", "Fatih", "Selda", "Canan", "Zafer", "Belkıs",
    "Hilal", "Atilla"]
soyadlar = ["Yavaş", "Küçükbay", "Kaçar", "Candan", "Özbay", "Göktürk",
    "Eskici", "Aydan", "Çiller", "Akşener", "Çiçek", "Öztürk", "Amanat", "Hastürk",
    "Kölük", "Fırat", "Havlucu", "Özen"] # Liste uzunlukları aynı olmak zorunda değil...

def bireşimci (veriler, ağırlıkları=None, biçimlemeFonksiyonu=None, tekrarSeçilebilsinMi=True):
    def bireşimle():
        if not tekrarSeçilebilsinMi: hatırla = set()
        while True:
            seçilen = p381.karşılıklıSeçim (*veriler)
            if not tekrarSeçilebilsinMi: # hatırla kümesindeyse olmayanını dene...
                tekrarSeçilen = str (seçilen)
                while tekrarSeçilen in hatırla:
                    seçilen = p381.karşılıklıSeçim (*veriler)
                    tekrarSeçilen = str (seçilen)
                hatırla.add (tekrarSeçilen) # yegane yeniyi hatırla kümesine ekle...
            if biçimlemeFonksiyonu: yield biçimlemeFonksiyonu (seçilen)
            else: yield seçilen # biçimsiz sade liste elemanları...
    return bireşimle


eleman = bireşimci (
    (adlar, soyadlar), # Tüple içi listeler...
    biçimlemeFonksiyonu=lambda x: " ".join(x), # Liste, tırnak ve virgülü biçimler...
    tekrarSeçilebilsinMi=False) # Seçimler tekrarsız yegane olsun...
#eleman = eleman() # Bireşimci fonksiyonu değişken adıymışcasına kullanılabilir...

try: sayı = abs (int (input ("Kaç eleman seçilecek [15]? ")))
except: sayı = 15

print ("\nAd soyad listesinden karşılıklı tesadüfi seçilen ", sayı, " eleman listesi:", "\n", "-"*67, sep="")
for i in range (sayı): print ((i+1), ": ", next (eleman()), sep="")



"""Çıktı:
>python p_30802.py
Kaç eleman seçilecek [15]?

Ad soyad listesinden karşılıklı tesadüfi seçilen 15 eleman listesi:
-------------------------------------------------------------------
1: Zafer Akşener
2: Sema Fırat
3: Zeliha Göktürk
4: Nedim Özen
5: Selda Özen
6: Serap Amanat
7: Nedim Göktürk
8: Fatih Çiçek
9: Canan Çiller
10: Zafer Öztürk
11: Sevim Özbay
12: Fatih Çiçek
13: Sema Candan
14: Belkıs Göktürk
15: Serap Eskici
"""