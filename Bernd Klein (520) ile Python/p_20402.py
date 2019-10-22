# coding:iso-8859-9 Türkçe
# p_20402.py: 10 ayrı sicimi başlatıp, 5 sn duraksatıp, sonra sürdürme örneği.

import time
from threading import Thread as İp # threading: Python-3

def uyutucu (i):
    print ("Sicim no: %d, 5 saniyeliğine uyuklar." % i)
    time.sleep (5)
    print ("Sicim no: %d uyanır." % i)

for i in range (10):
    t = İp (target = uyutucu, args = (i,) )
    t.start()



"""Çıktı:
>python p_20402.py
Sicim no: 0, 5 saniyeliğine uyuklar.
Sicim no: 1, 5 saniyeliğine uyuklar.
Sicim no: 2, 5 saniyeliğine uyuklar.
Sicim no: 3, 5 saniyeliğine uyuklar.
Sicim no: 4, 5 saniyeliğine uyuklar.
Sicim no: 5, 5 saniyeliğine uyuklar.
Sicim no: 6, 5 saniyeliğine uyuklar.
Sicim no: 7, 5 saniyeliğine uyuklar.
Sicim no: 8, 5 saniyeliğine uyuklar.
Sicim no: 9, 5 saniyeliğine uyuklar.
Sicim no: 0 uyanır.
Sicim no: 1 uyanır.
Sicim no: 2 uyanır.
Sicim no: 3 uyanır.
Sicim no: 4 uyanır.
Sicim no: 5 uyanır.
Sicim no: 6 uyanır.
Sicim no: 7 uyanır.
Sicim no: 8 uyanır.
Sicim no: 9 uyanır.
"""