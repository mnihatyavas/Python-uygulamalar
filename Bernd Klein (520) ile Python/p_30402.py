# coding:iso-8859-9 T�rk�e
# p_30402.py: Python ve numpy i�lem s�ratlerinin timeit.Timer() ve time.time() ile tespiti �rne�i.

import numpy as np
from timeit import Timer as T
#import time
from time import time as zaman

dizi = np.random.randint (0, 100, 1000) # [0->100) aras� 1000 adet tamsay� �retir...
liste = list (dizi)

def topla1(): dizi + 2
def topla2(): [de�er + 2 for de�er in liste]

nesne1 = T ("topla1()", "from __main__ import topla1")
nesne2 = T ("topla2()", "from __main__ import topla2")

zaman1 = nesne1.timeit (1000) # fonksiyonu 1000 kez i�letir...
zaman2 = nesne2.timeit (1000)

print ("1000 kez tekrarlamal� Python ve Numpy toplama i�lemi h�zlar� ('timeit' ile):")
print ("Python:", zaman2)
print ("Numpy:", zaman1)
print ("Numpy Python'dan", (zaman2 / zaman1), "misli s�ratlidir.")
print ("-"*75)
#---------------------------------------------------------------------------------------------------

def topla1():
    t = zaman()
    for i in range (1000): dizi + 2
    return (zaman() - t)

def topla2():
    t = zaman()
    for i in range (1000): [de�er + 2 for de�er in liste]
    return (zaman() - t)

zaman1 = topla1(); zaman2 = topla2()

print ("\n1000 kez tekrarl� Python ve Numpy toplama i�lemi h�zlar� ('time.time()' ile):")
print ("Python:", zaman2)
print ("Numpy:", zaman1)
print ("Numpy Python'dan", (zaman2 / zaman1), "misli s�ratlidir.")



"""��kt�:
>python p_30402.py
1000 kez tekrarlamal� Python ve Numpy toplama i�lemi h�zlar� ('timeit' ile):
Python: 2.166223377
Numpy: 0.030437674999999942
Numpy Python'dan 71.16914734781827 misli s�ratlidir.
---------------------------------------------------------------------------

1000 kez tekrarl� Python ve Numpy toplama i�lemi h�zlar� ('time.time()' ile):
Python: 3.1668057441711426
Numpy: 0.04680013656616211
Numpy Python'dan 67.66659194881147 misli s�ratlidir.
"""