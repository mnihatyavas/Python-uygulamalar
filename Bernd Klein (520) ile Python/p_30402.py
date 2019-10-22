# coding:iso-8859-9 Türkçe
# p_30402.py: Python ve numpy işlem süratlerinin timeit.Timer() ve time.time() ile tespiti örneği.

import numpy as np
from timeit import Timer as T
#import time
from time import time as zaman

dizi = np.random.randint (0, 100, 1000) # [0->100) arası 1000 adet tamsayı üretir...
liste = list (dizi)

def topla1(): dizi + 2
def topla2(): [değer + 2 for değer in liste]

nesne1 = T ("topla1()", "from __main__ import topla1")
nesne2 = T ("topla2()", "from __main__ import topla2")

zaman1 = nesne1.timeit (1000) # fonksiyonu 1000 kez işletir...
zaman2 = nesne2.timeit (1000)

print ("1000 kez tekrarlamalı Python ve Numpy toplama işlemi hızları ('timeit' ile):")
print ("Python:", zaman2)
print ("Numpy:", zaman1)
print ("Numpy Python'dan", (zaman2 / zaman1), "misli süratlidir.")
print ("-"*75)
#---------------------------------------------------------------------------------------------------

def topla1():
    t = zaman()
    for i in range (1000): dizi + 2
    return (zaman() - t)

def topla2():
    t = zaman()
    for i in range (1000): [değer + 2 for değer in liste]
    return (zaman() - t)

zaman1 = topla1(); zaman2 = topla2()

print ("\n1000 kez tekrarlı Python ve Numpy toplama işlemi hızları ('time.time()' ile):")
print ("Python:", zaman2)
print ("Numpy:", zaman1)
print ("Numpy Python'dan", (zaman2 / zaman1), "misli süratlidir.")



"""Çıktı:
>python p_30402.py
1000 kez tekrarlamalı Python ve Numpy toplama işlemi hızları ('timeit' ile):
Python: 2.166223377
Numpy: 0.030437674999999942
Numpy Python'dan 71.16914734781827 misli süratlidir.
---------------------------------------------------------------------------

1000 kez tekrarlı Python ve Numpy toplama işlemi hızları ('time.time()' ile):
Python: 3.1668057441711426
Numpy: 0.04680013656616211
Numpy Python'dan 67.66659194881147 misli süratlidir.
"""