# coding:iso-8859-9 T�rk�e
# p_20402.py: 10 ayr� sicimi ba�lat�p, 5 sn duraksat�p, sonra s�rd�rme �rne�i.

import time
from threading import Thread as �p # threading: Python-3

def uyutucu (i):
    print ("Sicim no: %d, 5 saniyeli�ine uyuklar." % i)
    time.sleep (5)
    print ("Sicim no: %d uyan�r." % i)

for i in range (10):
    t = �p (target = uyutucu, args = (i,) )
    t.start()



"""��kt�:
>python p_20402.py
Sicim no: 0, 5 saniyeli�ine uyuklar.
Sicim no: 1, 5 saniyeli�ine uyuklar.
Sicim no: 2, 5 saniyeli�ine uyuklar.
Sicim no: 3, 5 saniyeli�ine uyuklar.
Sicim no: 4, 5 saniyeli�ine uyuklar.
Sicim no: 5, 5 saniyeli�ine uyuklar.
Sicim no: 6, 5 saniyeli�ine uyuklar.
Sicim no: 7, 5 saniyeli�ine uyuklar.
Sicim no: 8, 5 saniyeli�ine uyuklar.
Sicim no: 9, 5 saniyeli�ine uyuklar.
Sicim no: 0 uyan�r.
Sicim no: 1 uyan�r.
Sicim no: 2 uyan�r.
Sicim no: 3 uyan�r.
Sicim no: 4 uyan�r.
Sicim no: 5 uyan�r.
Sicim no: 6 uyan�r.
Sicim no: 7 uyan�r.
Sicim no: 8 uyan�r.
Sicim no: 9 uyan�r.
"""