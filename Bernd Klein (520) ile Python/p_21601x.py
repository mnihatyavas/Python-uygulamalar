# coding:iso-8859-9 T�rk�e
# p_21601x.py: Martermind usta'k�l oyununda gerekli fonksiyonlar alt-�rne�i.

import random

def ard�l�arp�m (n):
    if n == 0: return 1
    else: return (ard�l�arp�m (n-1) * n)

def yerde�i�tirim (birimler):
    n = len (birimler)
    if n==0: yield []
    else:
        for i in range (len (birimler)):
            for r in yerde�i�tirim (birimler [:i]+birimler [i+1:]):
                yield [birimler [i]]+r
                
def kYerde�i�tirim (birimler, n):
    if n==0: yield []
    else:
        for i in range (len (birimler)):
            for r in kYerde�i�tirim (birimler, n-1):
                if (not birimler [i] in r): yield [birimler [i]]+r

def rasgeleYerde�i�tirim (liste):
    uz = len (liste);
    azami = ard�l�arp�m (uz);
    endeks = random.randrange (0, azami)
    i = 0
    for r in yerde�i�tirim (liste):
        if i == endeks: return r
        i += 1

def t�mRenkler (renkler, konumlar):
    renkler = rasgeleYerde�i�tirim (renkler)
    for r in kYerde�i�tirim (renkler, konumlar): yield (r)