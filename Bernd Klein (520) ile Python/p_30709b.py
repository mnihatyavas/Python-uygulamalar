# coding:iso-8859-9 Türkçe
# p_30709b.py: Normalvariate tesadüfi frekans üretici ve matplotlib grafiği örneği.

from random import normalvariate as nv
import matplotlib.pyplot as mp

n = 1000
değerler = []
sıklıklar = {}
while len (değerler) < n:
    değer = nv (180, 30) # 180 anadeğer etrafında 30 standart sapmalı tesadüfi ondalık üretme...
    #if 130 < değer < 230: # Üretilenin tümünü kapsat...
    sıklıklar[int (değer)] = sıklıklar.get (int (değer), 0) + 1 # 0-20 arası y-değer üretme...
    değerler.append (değer)

değerler.sort()
print (değerler[:5], değerler[995:]) # Baştan ve sondan 5'er değer [70-290]...
#-----------------------------------------------------------------------------------------------

sıklık = list (sıklıklar.items()) # Sözlüğün anahtar ve değerlerini liste olarak al...
sıklık.sort()
mp.style.use ("dark_background")
mp.plot (*list (zip (*sıklık)))
#mp.savefig ("p_30709bx.png")
mp.show()



"""Çıktı:
>python p_30709b.py
[73.45953976893655, 83.52152337277587, 97.82315286011804, 98.6410332823605, 99.5
6370046942924] [261.6905756509782, 263.62056222573585, 265.47875343956065, 278.7
066865707825, 281.2144583467016]
"""