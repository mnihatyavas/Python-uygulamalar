# coding:iso-8859-9 T�rk�e
# p_30709b.py: Normalvariate tesad�fi frekans �retici ve matplotlib grafi�i �rne�i.

from random import normalvariate as nv
import matplotlib.pyplot as mp

n = 1000
de�erler = []
s�kl�klar = {}
while len (de�erler) < n:
    de�er = nv (180, 30) # 180 anade�er etraf�nda 30 standart sapmal� tesad�fi ondal�k �retme...
    #if 130 < de�er < 230: # �retilenin t�m�n� kapsat...
    s�kl�klar[int (de�er)] = s�kl�klar.get (int (de�er), 0) + 1 # 0-20 aras� y-de�er �retme...
    de�erler.append (de�er)

de�erler.sort()
print (de�erler[:5], de�erler[995:]) # Ba�tan ve sondan 5'er de�er [70-290]...
#-----------------------------------------------------------------------------------------------

s�kl�k = list (s�kl�klar.items()) # S�zl���n anahtar ve de�erlerini liste olarak al...
s�kl�k.sort()
mp.style.use ("dark_background")
mp.plot (*list (zip (*s�kl�k)))
#mp.savefig ("p_30709bx.png")
mp.show()



"""��kt�:
>python p_30709b.py
[73.45953976893655, 83.52152337277587, 97.82315286011804, 98.6410332823605, 99.5
6370046942924] [261.6905756509782, 263.62056222573585, 265.47875343956065, 278.7
066865707825, 281.2144583467016]
"""