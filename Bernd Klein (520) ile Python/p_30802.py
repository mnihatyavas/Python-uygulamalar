# coding:iso-8859-9 T�rk�e
# p_30802.py: Ad ve soyadlar�n kar��l�kl� a��rl�ks�z yegane bi�imli se�im d�k�m� �rne�i.

import p_30801 as p381

adlar = ["Hatice", "S�heyla", "Zeliha", "Nihat", "Song�l", "Nedim", "Sevim",
    "Nur", "Y�cel", "Serap", "Sema", "Fatih", "Selda", "Canan", "Zafer", "Belk�s",
    "Hilal", "Atilla"]
soyadlar = ["Yava�", "K���kbay", "Ka�ar", "Candan", "�zbay", "G�kt�rk",
    "Eskici", "Aydan", "�iller", "Ak�ener", "�i�ek", "�zt�rk", "Amanat", "Hast�rk",
    "K�l�k", "F�rat", "Havlucu", "�zen"] # Liste uzunluklar� ayn� olmak zorunda de�il...

def bire�imci (veriler, a��rl�klar�=None, bi�imlemeFonksiyonu=None, tekrarSe�ilebilsinMi=True):
    def bire�imle():
        if not tekrarSe�ilebilsinMi: hat�rla = set()
        while True:
            se�ilen = p381.kar��l�kl�Se�im (*veriler)
            if not tekrarSe�ilebilsinMi: # hat�rla k�mesindeyse olmayan�n� dene...
                tekrarSe�ilen = str (se�ilen)
                while tekrarSe�ilen in hat�rla:
                    se�ilen = p381.kar��l�kl�Se�im (*veriler)
                    tekrarSe�ilen = str (se�ilen)
                hat�rla.add (tekrarSe�ilen) # yegane yeniyi hat�rla k�mesine ekle...
            if bi�imlemeFonksiyonu: yield bi�imlemeFonksiyonu (se�ilen)
            else: yield se�ilen # bi�imsiz sade liste elemanlar�...
    return bire�imle


eleman = bire�imci (
    (adlar, soyadlar), # T�ple i�i listeler...
    bi�imlemeFonksiyonu=lambda x: " ".join(x), # Liste, t�rnak ve virg�l� bi�imler...
    tekrarSe�ilebilsinMi=False) # Se�imler tekrars�z yegane olsun...
#eleman = eleman() # Bire�imci fonksiyonu de�i�ken ad�ym��cas�na kullan�labilir...

try: say� = abs (int (input ("Ka� eleman se�ilecek [15]? ")))
except: say� = 15

print ("\nAd soyad listesinden kar��l�kl� tesad�fi se�ilen ", say�, " eleman listesi:", "\n", "-"*67, sep="")
for i in range (say�): print ((i+1), ": ", next (eleman()), sep="")



"""��kt�:
>python p_30802.py
Ka� eleman se�ilecek [15]?

Ad soyad listesinden kar��l�kl� tesad�fi se�ilen 15 eleman listesi:
-------------------------------------------------------------------
1: Zafer Ak�ener
2: Sema F�rat
3: Zeliha G�kt�rk
4: Nedim �zen
5: Selda �zen
6: Serap Amanat
7: Nedim G�kt�rk
8: Fatih �i�ek
9: Canan �iller
10: Zafer �zt�rk
11: Sevim �zbay
12: Fatih �i�ek
13: Sema Candan
14: Belk�s G�kt�rk
15: Serap Eskici
"""