# coding:iso-8859-9 Türkçe
# p_30709a.py: Gauss tesadüfi frekans üretici ve matplotlib grafiği örneği.

from random import gauss as g
import matplotlib.pyplot as mp

n = 1000
değerler = []
sıklıklar = {}
while len (değerler) < n:
    değer = g (180, 30) # 180 anadeğer etrafında 30 standart sapmalı tesadüfi ondalık üretme...
    #if 130 < değer < 230: # Üretilenin tümünü kapsat...
    sıklıklar[int (değer)] = sıklıklar.get (int (değer), 0) + 1 # 0-20 arası y-değer üretme...
    değerler.append (değer)

değerler.sort()
print (değerler[:5], değerler[995:]) # Baştan ve sondan 5'er değer [80-288]...
#-----------------------------------------------------------------------------------------------

sıklık = list (sıklıklar.items()) # Sözlüğün anahtar ve değerlerini liste olarak al...
sıklık.sort()
mp.style.use ("dark_background")
mp.plot (*list (zip (*sıklık)))
#mp.savefig ("p_30709ax.png")
mp.show()



"""Çıktı:
>python p_30709.py
[95.3057432432776, 97.02055853091295, 104.63957106331833, 106.14337633959009, 10
9.37793982566741] [254.4796008235056, 254.69487434904192, 256.46660272806764, 26
5.60481507537014, 269.12631757634955]
"""