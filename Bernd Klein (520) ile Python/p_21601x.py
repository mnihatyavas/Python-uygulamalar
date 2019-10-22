# coding:iso-8859-9 Türkçe
# p_21601x.py: Martermind usta'kıl oyununda gerekli fonksiyonlar alt-örneği.

import random

def ardılÇarpım (n):
    if n == 0: return 1
    else: return (ardılÇarpım (n-1) * n)

def yerdeğiştirim (birimler):
    n = len (birimler)
    if n==0: yield []
    else:
        for i in range (len (birimler)):
            for r in yerdeğiştirim (birimler [:i]+birimler [i+1:]):
                yield [birimler [i]]+r
                
def kYerdeğiştirim (birimler, n):
    if n==0: yield []
    else:
        for i in range (len (birimler)):
            for r in kYerdeğiştirim (birimler, n-1):
                if (not birimler [i] in r): yield [birimler [i]]+r

def rasgeleYerdeğiştirim (liste):
    uz = len (liste);
    azami = ardılÇarpım (uz);
    endeks = random.randrange (0, azami)
    i = 0
    for r in yerdeğiştirim (liste):
        if i == endeks: return r
        i += 1

def tümRenkler (renkler, konumlar):
    renkler = rasgeleYerdeğiştirim (renkler)
    for r in kYerdeğiştirim (renkler, konumlar): yield (r)