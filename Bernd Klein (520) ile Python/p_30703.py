# coding:iso-8859-9 T�rk�e
# p_30703.py: Hileli a��rl�kl� zarlarla 10Bin at��ta [1,6] gelme y�zdeleri �rne�i.

import numpy as np
import random
from collections import Counter as Saya�

def ka��nc�Arada (x, mesafe):
    for i in range (0, len (mesafe)):
        if x < mesafe[i]: return i-1
    return -1

def a��rl�kl�Tercih (zarY�zleri, gelmeA��rl�klar�, kriptoluMu=True):
    if kriptoluMu: x = random.SystemRandom().random()
    else: x = np.random.random()
    gelmeY�zdeleriToplam� = [0] + list (np.cumsum (gelmeA��rl�klar�))
    endeks = ka��nc�Arada (x, gelmeY�zdeleriToplam�)
    return zarY�zleri [endeks]


zar�nY�zleri = [1, 2, 3, 4, 5, 6]
gelmeA��rl�klar� = [1/12, 1/12, 1/12, 1/12, 2/12, 6/12] # Hileli olas�l�klar toplam�: p+=12/12...
sonu�lar = []

try: kere = abs (int (input ("Zar ka� kez at�ls�n? [Varsay�l�=10 000]: ")))
except: kere = 10000

for _ in range (kere): sonu�lar.append (a��rl�kl�Tercih (zar�nY�zleri, gelmeA��rl�klar�)) # Varsay�l� kriptolu...
zarGelenleri = Saya� (sonu�lar)
for anahtar in zarGelenleri: zarGelenleri [anahtar] = zarGelenleri [anahtar] / kere # 1'e normalle�tirilen gelen zar y�zdeleri...

liste = sorted (list (zarGelenleri.values()) )
print ("\nGelme y�zdeleri: ", liste,
    "\nNormalle�tirilmi� y�zdeler toplam� = 1 mi? ", (sum (liste) > 0.999), sep="")

print ("\nBi�imli ��kt�lar:\n", "-"*62, sep="")
for i in range (len (zar�nY�zleri)):
    print ("Zar: {:}, Normalle�tirilen sonucu: {:6.4f}, Y�zde sonucu: %{:6.2f}" .format ((i+1), liste[i], (liste[i] * 100)) )
print ("-"*62, "\n{:30s}Y�zde sonu�lar� toplam�: %{:5.2f}" .format (" ", (sum (liste) * 100)) )



"""��kt�:
>python p_30703.py
Zar ka� kez at�ls�n? [Varsay�l�=10 000]: 

Gelme y�zdeleri: [0.0786, 0.0833, 0.0842, 0.0886, 0.1664, 0.4989]
Normalle�tirilmi� y�zdeler toplam� = 1 mi? True

Bi�imli ��kt�lar:
--------------------------------------------------------------
Zar: 1, Normalle�tirilen sonucu: 0.0786, Y�zde sonucu: %  7.86
Zar: 2, Normalle�tirilen sonucu: 0.0833, Y�zde sonucu: %  8.33
Zar: 3, Normalle�tirilen sonucu: 0.0842, Y�zde sonucu: %  8.42
Zar: 4, Normalle�tirilen sonucu: 0.0886, Y�zde sonucu: %  8.86
Zar: 5, Normalle�tirilen sonucu: 0.1664, Y�zde sonucu: % 16.64
Zar: 6, Normalle�tirilen sonucu: 0.4989, Y�zde sonucu: % 49.89
--------------------------------------------------------------
                              Y�zde sonu�lar� toplam�: %100.00

>python p_30703.py  ** TEKRAR **
Zar ka� kez at�ls�n? [Varsay�l�=10 000]: 1957

Gelme y�zdeleri: [0.07511497189575882, 0.07613694430250383, 0.0807358201328564, 0.08277976494634645, 0.17015840572304547, 0.515074092999489]
Normalle�tirilmi� y�zdeler toplam� = 1 mi? True

Bi�imli ��kt�lar:
--------------------------------------------------------------
Zar: 1, Normalle�tirilen sonucu: 0.0751, Y�zde sonucu: %  7.51
Zar: 2, Normalle�tirilen sonucu: 0.0761, Y�zde sonucu: %  7.61
Zar: 3, Normalle�tirilen sonucu: 0.0807, Y�zde sonucu: %  8.07
Zar: 4, Normalle�tirilen sonucu: 0.0828, Y�zde sonucu: %  8.28
Zar: 5, Normalle�tirilen sonucu: 0.1702, Y�zde sonucu: % 17.02
Zar: 6, Normalle�tirilen sonucu: 0.5151, Y�zde sonucu: % 51.51
--------------------------------------------------------------
                              Y�zde sonu�lar� toplam�: %100.00
"""