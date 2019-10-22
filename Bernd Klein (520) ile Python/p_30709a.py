# coding:iso-8859-9 T�rk�e
# p_30709a.py: Gauss tesad�fi frekans �retici ve matplotlib grafi�i �rne�i.

from random import gauss as g
import matplotlib.pyplot as mp

n = 1000
de�erler = []
s�kl�klar = {}
while len (de�erler) < n:
    de�er = g (180, 30) # 180 anade�er etraf�nda 30 standart sapmal� tesad�fi ondal�k �retme...
    #if 130 < de�er < 230: # �retilenin t�m�n� kapsat...
    s�kl�klar[int (de�er)] = s�kl�klar.get (int (de�er), 0) + 1 # 0-20 aras� y-de�er �retme...
    de�erler.append (de�er)

de�erler.sort()
print (de�erler[:5], de�erler[995:]) # Ba�tan ve sondan 5'er de�er [80-288]...
#-----------------------------------------------------------------------------------------------

s�kl�k = list (s�kl�klar.items()) # S�zl���n anahtar ve de�erlerini liste olarak al...
s�kl�k.sort()
mp.style.use ("dark_background")
mp.plot (*list (zip (*s�kl�k)))
#mp.savefig ("p_30709ax.png")
mp.show()



"""��kt�:
>python p_30709.py
[95.3057432432776, 97.02055853091295, 104.63957106331833, 106.14337633959009, 10
9.37793982566741] [254.4796008235056, 254.69487434904192, 256.46660272806764, 26
5.60481507537014, 269.12631757634955]
"""