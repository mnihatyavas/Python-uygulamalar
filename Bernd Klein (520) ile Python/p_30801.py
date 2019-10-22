# coding:iso-8859-9 T�rk�e
# p_30801.py: Ad ve soyad listelerinden kar��l�kl� a��rl�ks�z se�imi �rne�i.

import random
import numpy as np
from random import choice

def a��rl�kl��rnekleme2 (listem, a��rl�klar�, k):
    se�ilenK�me = set()
    listem = list (listem)
    a��rl�klar� = list (a��rl�klar�)
    while len (se�ilenK�me) < k:
        se�ilen = a��rl�kl�Tercih (listem, a��rl�klar�)
        if se�ilen not in se�ilenK�me: se�ilenK�me.add (se�ilen)
        # Se�ilen tekrar se�ilmi�se k�meye eklenmez...
    return list (se�ilenK�me)

def a��rl�kl�Tercih (veriler, gelmeA��rl�klar�, kriptoluMu=True):
    if kriptoluMu: x = random.SystemRandom().random()
    else: x = np.random.random()
    gelmeY�zdeleriToplam� = [0] + list (np.cumsum (gelmeA��rl�klar�))
    endeks = ka��nc�Arada (x, gelmeY�zdeleriToplam�)
    return veriler[endeks]

def ka��nc�Arada (de�erim, b�l�mler, u�lar_1Mi=True):
    for i in range (0, len (b�l�mler)):
        if de�erim < b�l�mler[i]: return i-1 if u�lar_1Mi else i
    return -1 if u�lar_1Mi else len (b�l�mler)

def kar��l�kl�Se�im (*taranabilenler):
    sonu� = []
    for listem in taranabilenler: sonu�.append (choice (listem))
    return sonu�

def a��rl�kl�Kar��l�kl�Se�im (*taranabilenler):
    sonu� = []
    for veri, a��rl��� in taranabilenler:
        a��rl�kl�Se�im = a��rl�kl�Tercih (veri, a��rl���)
        sonu�.append (a��rl�kl�Se�im)
    return sonu�

def bire�imci (veriler, a��rl�klar�=None, bi�imlemeFonksiyonu=None, tekrarlanabilirSe�imMi=True):
    def tercih (veriler, a��rl�klar�):
        if a��rl�klar�: return a��rl�kl�Kar��l�kl�Se�im (*zip (veriler, a��rl�klar�))
        else: return kar��l�kl�Se�im (*veriler)
    def bire�imle():
        if not tekrarlanabilirSe�imMi: belle = set()
        while True:
            yeniSe�ilen = tercih (veriler, a��rl�klar�)
            if not tekrarlanabilirSe�imMi:
                se�ilen = str (yeniSe�ilen)
                while se�ilen in belle:
                    yeniSe�ilen = tercih (veriler, a��rl�klar�)
                    se�ilen = str (yeniSe�ilen)
                belle.add (se�ilen)
            if bi�imlemeFonksiyonu: yield bi�imlemeFonksiyonu (yeniSe�ilen)
            else: yield yeniSe�ilen
    return bire�imle


if __name__ == "__main__":
    adlar = ["Hatice", "S�heyla", "Zeliha", "Nihat", "Song�l", "Nedim", "Sevim",
        "Nur", "Y�cel", "Serap", "Sema", "Fatih", "Selda", "Canan", "Zafer", "Belk�s",
        "Hilal", "Atilla"]
    soyadlar = ["Yava�", "K���kbay", "Ka�ar", "Candan", "�zbay", "G�kt�rk",
        "Eskici", "Aydan", "�iller", "Ak�ener", "�i�ek", "�zt�rk", "Amanat", "Hast�rk",
        "K�l�k", "F�rat", "Havlucu", "�zen"] # Liste uzunluklar� ayn� olmak zorunda de�il...

    try: say� = abs (int (input ("Ka� eleman se�ilecek [15]? ")))
    except: say� = 15

    elemanlar = set()
    while len (elemanlar) < say�:
        eleman = kar��l�kl�Se�im (adlar, soyadlar)
        elemanlar.add (" ".join (eleman))
    print (elemanlar)



"""��kt�:
>python p_30801.py
Ka� eleman se�ilecek [15]?
{'Hilal Havlucu', 'Belk�s �i�ek', 'Nedim K�l�k', 'Zafer Ak�ener', 'Hilal Hast�rk',
'S�heyla �iller', 'Atilla Candan', 'Atilla �zt�rk', 'Zeliha �zen', 'Selda Aydan',
'Belk�s Hast�rk', 'Zeliha K���kbay', 'Selda Havlucu', 'Sema �i�ek', 'CananEskici'}

>python p_30801.py  ** TEKRAR **
Ka� eleman se�ilecek [15]? 20
{'Hilal K���kbay', 'Canan Hast�rk', 'Nedim Eskici', 'Nihat �zen', 'Hilal G�kt�rk',
'Selda �i�ek', 'Song�l Hast�rk', 'Song�l Ka�ar', 'Sevim K���kbay', 'Nedim �zen',
'Sema Ak�ener', 'Zeliha �zbay', 'Fatih Aydan', 'Zeliha �zt�rk', 'S�heyla �iller',
'Zeliha �zen', 'Nedim K�l�k', 'Canan F�rat', 'Sema �zbay', 'Belk�s Eskici'}
"""